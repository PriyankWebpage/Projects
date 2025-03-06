
![Thumbnail](https://github.com/user-attachments/assets/bfb4a976-0023-4fb2-9f7b-a15383f5c81d)


# Fashion Recommender System
This project aims to provide personalized fashion recommendations to users by analyzing input images and suggesting visually similar clothing items. Leveraging deep learning techniques and computer vision, the system enhances the online shopping experience by guiding users toward products that align with their style preferences.

# Introduction
With the rapid growth of e-commerce, consumers are presented with an overwhelming number of fashion choices. This Fashion Recommender System addresses this challenge by analyzing user-provided images to suggest similar fashion items, thereby simplifying the decision-making process and enhancing user satisfaction.

# Features
- Image-Based Recommendations: Users can upload an image of a clothing item, and the system will recommend visually similar products.
- Interactive Interface: A user-friendly web application built using Streamlit allows for seamless interaction.
- Efficient Retrieval: Utilizes a combination of Convolutional Neural Networks (CNNs) and Nearest Neighbors algorithms to ensure accurate and quick recommendations.

# Dataset
The system is trained on the Fashion Product Images Dataset, which contains images and metadata of various fashion items. This dataset provides a diverse range of clothing categories, facilitating robust model training.

# Model Architecture
The recommendation engine employs a two-stage approach:
- *Feature Extraction*: A pre-trained ResNet50 model, fine-tuned on the fashion dataset, extracts feature embeddings from product images.
- *Similarity Matching*: The extracted features are indexed using the Nearest Neighbors algorithm with cosine similarity to find and recommend items similar to the user's input image.

# Usage
After installation, you can run the application locally:
- Start the Streamlit application
- Upload an image: Use the web interface to upload a clothing item image.
- View recommendations: The system will display a list of visually similar items based on the uploaded image.

# Results

### Jeans Suggestion

- Upload Image – The user uploads a picture of jeans.
- AI Analyzes Image – The system detects key features like color, style, and fabric.
- Finds Similar Items – It compares the uploaded image with a fashion database.
- Shows Recommendations – The system displays jeans that look similar, suggesting different styles, colors, or brands.
- User Interaction – The user can refine choices based on preferences like fit or color.

https://github.com/user-attachments/assets/2d678811-fdba-4803-8586-995bae7df0fb

### T-Shirt Suggestion

- Upload Image – The user uploads a picture of a T-shirt.
- AI Analyzes Image – The system detects key features like color, design, fabric, and sleeve length.
- Finds Similar Items – It compares the uploaded image with a fashion database.
- Shows Recommendations – The system displays similar T-shirts, suggesting different colors, patterns, or brands.
- User Interaction – The user can refine choices, like selecting plain, graphic, or polo T-shirts.

https://github.com/user-attachments/assets/87011c28-25b8-41ac-96ae-2e0d41662126



