![image](https://github.com/user-attachments/assets/1d4296c6-4dfb-4e09-90f7-937195f8e8aa)


# News Research ChatBot using AWS BedRock

## Overview

News Research ChatBot is a powerful tool that allows users to research and summarize news articles using AWS BedRock's AI models. It utilizes advanced language models such as Claude and Llama3 for generating insights and FAISS for vector-based search.

## Features

- Extracts and processes text from news articles based on provided URLs.

- Uses AWS BedRock's Titan Embeddings for generating vector representations.

- Implements FAISS for efficient similarity search and retrieval.

- Supports Anthropic's Claude and Meta's Llama3 models for AI-generated responses.

- Provides an interactive UI using Streamlit.

- Saves generated responses to AWS S3.

## Tech Stack

- AWS BedRock - For AI model inference

- FAISS - Vector similarity search

- Streamlit - User interface

- boto3 - AWS SDK for Python

- LangChain - Orchestration of LLMs and embeddings

- Python - Programming language

## Usage

- Run the Streamlit app: streamlit run app.py

- Enter news article URLs in the sidebar.

- Click "Process URLs" to ingest data and generate embeddings.

- Ask questions related to the articles in the input field.

- Choose between "Claude Output" and "Llama3 Output" for responses.

- Optionally, save the response to AWS S3.

## Results
<img width="1352" alt="Screenshot 2025-03-06 at 6 37 29 PM" src="https://github.com/user-attachments/assets/5b6dd54c-90e1-4e6b-953c-ac5a319af64b" />



