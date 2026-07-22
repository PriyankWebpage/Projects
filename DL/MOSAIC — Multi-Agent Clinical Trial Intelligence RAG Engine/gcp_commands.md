# GCP Commands — End to End Reference

Covers every `gcloud` / `gsutil` / `psql` command used across MOSAIC infra setup, deployment, auditing, and cleanup.

---

## 1. Auth & Project Setup

```bash
gcloud auth login
```
Authenticates your terminal/Cloud Shell session with your Google account.

```bash
gcloud projects list
```
Lists all GCP projects your account has access to.

```bash
gcloud config set project PROJECT_ID
```
Sets the active project so subsequent commands don't need `--project` on every call.

```bash
gcloud config get-value project
```
Confirms which project is currently active.

```bash
export CLOUDSDK_CORE_PROJECT=PROJECT_ID
```
Alternative way to set the active project temporarily via environment variable (session-only).

---

## 2. Enabling APIs

```bash
gcloud services list --enabled
```
Lists all APIs currently enabled on the project. Enabling an API is free — only usage of the underlying service costs money.

Note: many `gcloud` commands (e.g. `gcloud compute instances list`, `gcloud functions list`) will prompt to auto-enable their API the first time you run them — answering `y` enables it, `N`/`n` skips (useful to confirm a service was never provisioned).

---

## 3. Cloud SQL — Provisioning (PostgreSQL + pgvector)

```bash
gcloud sql instances create clinical-trial-db \
  --database-version=POSTGRES_15 \
  --tier=db-f1-micro \
  --zone=us-central1-f \
  --project=mosaic-clinical-trials
```
Creates a Cloud SQL PostgreSQL instance. `--zone` (instead of `--region`) can resolve `PENDING_CREATE` hangs some GCP regions have on default zone selection.

```bash
gcloud sql instances list --project=PROJECT_ID
```
Checks provisioning status — poll this until `STATUS` flips from `PENDING_CREATE` to `RUNNABLE`.

```bash
gcloud sql instances delete clinical-trial-db --project=PROJECT_ID
```
Deletes an instance — used both to recover from a stuck `PENDING_CREATE` and later for full cleanup.

```bash
gcloud sql databases create clinical_trial_db \
  --instance=clinical-trial-db \
  --project=mosaic-clinical-trials
```
Creates a database inside the instance.

```bash
gcloud sql users create mosaic_user \
  --instance=clinical-trial-db \
  --password=mosaic_pass_2024 \
  --project=mosaic-clinical-trials
```
Creates a database user with password auth.

```bash
curl -4 ifconfig.me
```
Gets your machine's public IPv4 address (needed to whitelist for Cloud SQL access). Use `curl https://api4.ipify.org` as a fallback if `ifconfig.me` returns nothing.

```bash
gcloud sql instances patch clinical-trial-db \
  --authorized-networks=YOUR_IP/32 \
  --project=mosaic-clinical-trials
```
Whitelists an IP for direct `psql` access. **Note:** this replaces the whole authorized-networks list — include previously authorized IPs too, or they get de-authorized.

```bash
gcloud sql instances describe clinical-trial-db --format="yaml(state,settings.tier,settings.dataDiskSizeGb)"
```
Shows running state, machine tier, and disk size — useful for gauging cost.

---

## 4. Cloud SQL — Stopping / Restarting (cost control without deleting)

```bash
gcloud sql instances patch clinical-trial-db --activation-policy NEVER
```
Stops the instance (keeps data, stops compute billing). Good for "pause overnight."

```bash
gcloud sql instances describe clinical-trial-db --format="value(settings.activationPolicy)"
```
Confirms the activation policy — returns `NEVER` once stopped.

```bash
gcloud sql instances patch clinical-trial-db --activation-policy ALWAYS
```
Restarts a stopped instance.

---

## 5. Database Schema (psql, not gcloud)

```bash
brew install libpq
echo 'export PATH="/usr/local/opt/libpq/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```
Installs the PostgreSQL client on Mac and adds it to PATH.

```bash
psql -h 34.133.55.17 -U mosaic_user -d clinical_trial_db
```
Connects to the Cloud SQL instance directly using its public IP.

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```
Enables pgvector inside the database — required before creating any `VECTOR(...)` columns.

```sql
\dt
```
Lists all tables in the current database — used to confirm schema creation succeeded.

```sql
\q
```
Exits the `psql` prompt.

---

## 6. Cloud Storage

```bash
gcloud storage buckets create gs://mosaic-clinical-trials-bucket-001 \
  --project=mosaic-clinical-trials \
  --location=us-central1
```
Creates a Cloud Storage bucket (used to store ingested documents/artifacts).

```bash
gsutil ls
```
Lists all buckets in the project (legacy tool; `gcloud storage` is the modern replacement).

```bash
gcloud storage du -s gs://BUCKET_NAME/
```
Shows total size of a bucket.

```bash
gcloud storage rm -r gs://BUCKET_NAME/
```
Recursively deletes all objects in a bucket, then the bucket itself.

---

## 7. IAM & Service Accounts

```bash
gcloud iam service-accounts create mosaic-sa \
  --display-name="MOSAIC API Service Account" \
  --project=mosaic-clinical-trials
```
Creates an identity for Cloud Run to use — service accounts are non-human "user accounts" for applications.

```bash
gcloud projects add-iam-policy-binding mosaic-clinical-trials \
  --member="serviceAccount:mosaic-sa@mosaic-clinical-trials.iam.gserviceaccount.com" \
  --role="roles/cloudsql.client"
```
Grants Cloud SQL access to the service account.

```bash
gcloud projects add-iam-policy-binding mosaic-clinical-trials \
  --member="serviceAccount:mosaic-sa@mosaic-clinical-trials.iam.gserviceaccount.com" \
  --role="roles/storage.objectAdmin"
```
Grants Cloud Storage access.

```bash
gcloud projects add-iam-policy-binding mosaic-clinical-trials \
  --member="serviceAccount:mosaic-sa@mosaic-clinical-trials.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```
Grants Secret Manager access. One role per service (least-privilege) rather than one admin-everything grant.

```bash
gcloud iam service-accounts list
```
Lists all service accounts in the project.

---

## 8. Secret Manager

```bash
echo -n "your-secret-value" | gcloud secrets create openai-api-key --data-file=-
```
Creates a secret from stdin (typical pattern; exact create commands varied by secret).

```bash
gcloud secrets list --project=PROJECT_ID
```
Lists all secrets in the project — used to confirm creation before deploying, and to find leftovers during cleanup.

```bash
gcloud secrets delete SECRET_NAME --quiet
```
Permanently deletes a secret and all its versions.

---

## 9. Docker Build (for Cloud Run)

```bash
docker buildx build \
  --platform linux/amd64 \
  -t gcr.io/mosaic-clinical-trials/mosaic-api:latest \
  -f deployment/Dockerfile \
  . \
  --push
```
Builds and pushes the image in one step. `--platform linux/amd64` is required on Apple Silicon Macs since Cloud Run needs AMD64, not ARM.

---

## 10. Cloud Run — Deploy

```bash
gcloud run deploy mosaic-api \
  --image=gcr.io/mosaic-clinical-trials/mosaic-api:latest \
  --platform=managed \
  --region=us-central1 \
  --service-account=mosaic-sa@mosaic-clinical-trials.iam.gserviceaccount.com \
  --add-cloudsql-instances=mosaic-clinical-trials:us-central1:clinical-trial-db \
  --set-env-vars="API_ENV=production,..." \
  --set-secrets="OPENAI_API_KEY=openai-api-key:latest,DB_PASSWORD=db-password:latest" \
  --port=8000 \
  --min-instances=0 \
  --max-instances=3 \
  --memory=2Gi \
  --cpu=2 \
  --timeout=300 \
  --concurrency=1 \
  --no-allow-unauthenticated \
  --project=mosaic-clinical-trials
```
Full deployment command. `--port=8000` must be explicit — Cloud Run doesn't infer it reliably. `--min-instances=0` means it scales to zero (no idle billing) unless set higher.

```bash
gcloud beta run services add-iam-policy-binding \
  --region=us-central1 \
  --member=allUsers \
  --role=roles/run.invoker \
  mosaic-api
```
Makes the service publicly callable (only works if your GCP org doesn't block public access via policy).

```bash
gcloud run services describe mosaic-api \
  --platform=managed \
  --region=us-central1 \
  --project=mosaic-clinical-trials \
  --format="value(status.url)"
```
Gets the live service URL.

```bash
gcloud auth print-identity-token
```
Generates a short-lived (~1hr) identity token for authenticated API calls — used as `Authorization: Bearer $(gcloud auth print-identity-token)` in curl.

---

## 11. Cloud Run — Audit / Inspect

```bash
gcloud run services list --platform=managed
```
Lists all Cloud Run services.

```bash
gcloud run services describe mosaic-api --region=us-central1 --format="yaml(spec.template.metadata.annotations)"
```
Shows scaling config (`min-instances`, `max-instances`) and linked resources like Cloud SQL — key for spotting silent idle costs.

---

## 12. Cloud Run — Delete

```bash
gcloud run services delete mosaic-api --region=us-central1 --quiet
```
Deletes a Cloud Run service.

---

## 13. Artifact Registry

```bash
gcloud artifacts repositories list
```
Lists Artifact Registry repositories (container image storage).

```bash
gcloud artifacts docker images list us-docker.pkg.dev/PROJECT/REPO --include-tags
```
Lists all Docker images inside a specific repository.

```bash
gcloud artifacts repositories delete gcr.io --location=us --quiet
```
Deletes an entire repository and all images inside it in one shot.

---

## 14. Full-Sweep Audit Commands (per resource type)

```bash
gcloud compute instances list
```
Compute Engine VMs.

```bash
gcloud compute disks list
```
Persistent disks — can bill even with no VM attached.

```bash
gcloud compute addresses list
```
Reserved static IPs — bill continuously if not attached to a running resource.

```bash
gcloud compute networks list
gcloud compute networks subnets list
```
VPC networks/subnets (the default network and its per-region subnets are free).

```bash
gcloud compute forwarding-rules list
gcloud compute routers list
gcloud compute backend-services list
```
Load balancers, NAT routers, backend services — all billable if present.

```bash
gcloud container clusters list
```
GKE (Kubernetes) clusters.

```bash
gcloud functions list
```
Cloud Functions.

```bash
bq ls
```
BigQuery datasets.

```bash
gcloud pubsub topics list
gcloud pubsub subscriptions list
```
Pub/Sub topics and subscriptions.

```bash
gcloud scheduler jobs list --location=us-central1
```
Cloud Scheduler jobs.

```bash
gcloud builds triggers list
```
Cloud Build triggers.

```bash
gcloud dns managed-zones list
```
Cloud DNS zones.

```bash
gcloud redis instances list --region=us-central1
```
Memorystore (Redis) instances.

```bash
gcloud filestore instances list
```
Filestore instances.

```bash
gcloud composer environments list --locations=us-central1
```
Cloud Composer environments.

```bash
gcloud app services list
gcloud app describe
```
App Engine services.

```bash
firebase projects:list
```
Firebase projects (if the Firebase CLI is installed).

---

## 15. One-Command Full Sweep — Cloud Asset Inventory

```bash
gcloud asset search-all-resources --project=PROJECT_ID --format="table(assetType,displayName,location)"
```
**The most efficient audit command** — queries Cloud Asset Inventory to return nearly every resource type across the entire project in a single call, instead of checking each service individually. May prompt to enable the Cloud Asset API on first use (free to enable).

---

## 16. Billing

```bash
gcloud billing accounts list
```
Lists billing accounts linked to your GCP account and whether they're open/active.

```bash
gcloud beta billing projects list --billing-account=BILLING_ACCOUNT_ID
```
Lists which projects have billing enabled under a given billing account — useful for finding forgotten projects that could still incur charges.

```bash
gcloud billing budgets create ...
```
Attempted to create a budget alert via CLI — this failed due to a quota-project configuration issue in practice; use the Console instead (**Billing → Budgets & alerts** → set amount + 50/90/100% thresholds).

---

## 17. Cross-Project Auditing (loop pattern)

```bash
for project in $(gcloud projects list --format="value(projectId)"); do
  echo "--- Project: $project ---"
  gcloud sql instances list --project=$project 2>/dev/null
done
```
Loops a single check across every project on the account. Same pattern was used for `compute instances list`, `container clusters list`, `run services list`, `app services list`.

```bash
timeout 10 gcloud run services list --project=PROJECT_ID --platform=managed 2>/dev/null
```
Wrapping audit calls in `timeout 10` prevents a slow/hanging API call from blocking the whole script — useful when checking many projects back to back.

---

## 18. Project-Level Deletion (nuclear option)

```bash
gcloud projects delete PROJECT_ID --quiet
```
Deletes an entire project — 30-day recovery grace period, then permanent. Guarantees zero billing risk from anything inside it. Used to remove unused projects (`mmhybridrag`, `mosaictest001`, `fabled-equator-483310-d7`) while keeping the active one.

Note: auto-created `gen-lang-client-*` projects may continue to appear in `gcloud projects list` after deletion for up to 30 days — this is expected soft-delete behavior, not a failed deletion.

---

## 19. Cosmetic Fix — Suppressing the "Regional Access Boundary" Warning

This warning is a known, benign background auth probe (see [googleapis/google-cloud-python#17515](https://github.com/googleapis/google-cloud-python/issues/17515)) — the underlying command always succeeds regardless of this warning.

```bash
export GOOGLE_AUTH_TRUST_BOUNDARY_ENABLED=false
```
Suppresses it for the current session.

```bash
echo 'export GOOGLE_AUTH_TRUST_BOUNDARY_ENABLED=false' >> ~/.bashrc
source ~/.bashrc
```
Makes the fix persist across Cloud Shell sessions.

---

## Reference: Known MOSAIC Project Details
- Project ID: `mosaic-clinical-trials` (project number `569957100480`)
- Cloud SQL instance: `clinical-trial-db`, PostgreSQL 15, tier `db-f1-micro`, zone `us-central1-f`
- Database: `clinical_trial_db`, user: `mosaic_user`
- GCS bucket: `mosaic-clinical-trials-bucket-001`
- Cloud Run service: `mosaic-api`, region `us-central1`
- Billing account: `01654B-EA3545-ED7A26`
