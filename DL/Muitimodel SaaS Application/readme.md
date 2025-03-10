![image](https://github.com/user-attachments/assets/861404da-d50f-4bf0-86cb-9175a97936ce)

# Multimodel SaaS Application for Sentiment Analysis

This project focuses on building a multimodal AI model for video sentiment and emotion analysis using PyTorch. The model takes videos as input and predicts the sentiment and emotion of the content. The solution involves training the model with multiple features like text, video, and audio encoding, performing multimodal fusion, and classifying the sentiment and emotion.

Once trained, the model is deployed using AWS SageMaker and is available for inference via an API in a SaaS application. The SaaS is built with the T3 Stack (Next.js, React, Tailwind, Auth.js), enabling users to run inference on their videos while managing monthly quotas.

## Features
Multimodal AI Model: Predicts sentiment and emotion from videos using a combination of:
- Text encoding
- Video encoding
- Audio encoding
- Multimodal fusion
- Sentiment and Emotion Classification
- AWS SageMaker Deployment: Trained model deployed with SageMaker Endpoints for scalability and reliability.
- SaaS Web Application: Built with Next.js, React, Tailwind, and Auth.js, users can upload videos and get predictions.
- API Integration: Expose model inference through API endpoints.
- Quota Management: Manage monthly quotas for users to control usage.

## Technologies Used
Backend:

- PyTorch: For model training and inference.
- AWS SageMaker: For model deployment and scalability.
- FastAPI (or another lightweight framework): For building API routes to connect the model with the front-end.

Frontend:
- Next.js: For SSR (Server-side rendering) and static generation.
- React: For building dynamic user interfaces.
- Tailwind CSS: For styling the application.
- Auth.js: For handling authentication and user management.

Other:
- AWS S3: For storing video files.
- API Gateway: For setting up endpoints for the SaaS API.

## Results

https://github.com/user-attachments/assets/c408b3bb-b6de-4883-bf55-3c08af708829

Once a user uploads a video to the SaaS platform, the system processes it through multiple AI models to extract and analyze different modalities (text, audio, and video). The final output provides insights into the sentiment and emotional content of the video.

Step-by-Step Processing of the Uploaded Video
### Preprocessing

- Extract Video Frames: Keyframes are extracted to analyze facial expressions and visual cues.
- Extract Audio: Speech and tonal variations are analyzed for sentiment.
- Transcribe Speech to Text: Converts spoken words into text using speech recognition.
- Feature Engineering: Converts raw data (text, audio, video) into embeddings.

### Multimodal Fusion & Prediction

- The extracted features from text, audio, and video are combined using multimodal fusion techniques.
- A trained deep learning model (using PyTorch) predicts the overall sentiment (positive, neutral, or negative) and the specific emotions (e.g., happy, sad, angry, surprised, etc.).

### Generating Results
- The model outputs a sentiment score (e.g., Positive: 0.85, Neutral: 0.10, Negative: 0.05)for all the dialogs in the video.
- The emotion distribution is also provided (e.g., 60% Joy, 20% Surprise, 15% Neutral, 5% Sadness).
