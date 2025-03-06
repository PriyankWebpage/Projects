import json
import os
import sys
import boto3
import streamlit as st
import pickle
import time
from langchain.chains import RetrievalQAWithSourcesChain
import nltk
from datetime import datetime
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
## We will be suing Titan Embeddings Model To generate Embedding

from langchain_aws import BedrockEmbeddings
from langchain_community.llms import Bedrock

## Data Ingestion

import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader

# Vector Embedding And Vector Store

from langchain_community.vectorstores import FAISS

## LLm Models
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

# take environment variables from .env (especially openai api key)
from dotenv import load_dotenv
load_dotenv()  

## Bedrock Clients
bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)


## Data ingestion 

def data_ingestion(urls):
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder = st.empty()
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    return docs

## Vector Embedding and vector store

def get_vector_store(docs):
    main_placeholder = st.empty()
    main_placeholder.text("Converting data into vectors ...✅✅✅")
    vectorstore_faiss=FAISS.from_documents(
        docs,
        bedrock_embeddings
    )
    vectorstore_faiss.save_local("faiss_index")

def get_claude_llm():
    ##create the Anthropic Model
    llm=Bedrock(model_id="anthropic.claude-v2:1",client=bedrock,
                model_kwargs={'max_tokens_to_sample':300})
    
    return llm

def get_llama2_llm():
    ##create the Anthropic Model
    llm=Bedrock(model_id="meta.llama3-8b-instruct-v1:0",client=bedrock,
                model_kwargs={'max_gen_len':512})
    
    return llm

prompt_template = """

Human: Use the following pieces of context to provide a 
concise answer to the question at the end but usse atleast summarize with 
100 words with detailed explaantions. If you don't know the answer, 
just say that you don't know, don't try to make up an answer.
<context>
{context}
</context

Question: {question}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

def get_response_llm(llm,vectorstore_faiss,query):
    qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore_faiss.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    ),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)
    answer=qa(query)
    # print("******************Templete*********************",qa)
    # print("******************Answer*********************",answer)
    return answer['result']

def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket = s3_bucket, Key = s3_key, Body =generate_blog )
        print("Data saved to s3")

    except Exception as e:
        print("Error when saving the code to s3")

def main():
    st.title("ArticleBot: News Research Tool 📈")
    st.sidebar.title("News Article URLs")
    urls = []
    
    if 'answer' not in st.session_state:
        st.session_state.answer = ''


    for i in range(3):
        url = st.sidebar.text_input(f"URL {i+1}")
        urls.append(url)
    
    with st.sidebar:    
        if st.button("Process URLs"):
            with st.spinner("Processing..."):
                docs = data_ingestion(urls)
                get_vector_store(docs)
                st.success("Done")


    main_placeholder = st.empty()
    
    st.header("Chat with Articles using AWS Bedrock💁")

    user_question = st.text_input("Ask a Question from the Websites")

    

    if st.button("Claude Output"):
        with st.spinner("Processing..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings,allow_dangerous_deserialization=True)
            llm=get_claude_llm()
            st.session_state.answer = get_response_llm(llm, faiss_index, user_question)
            st.write(st.session_state.answer)
            print(st.session_state.answer)
            st.success("Done")


    if st.button("Llama3 Output"):
        with st.spinner("Processing..."):
            faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings,allow_dangerous_deserialization=True)
            llm=get_llama2_llm()
            st.session_state.answer = get_response_llm(llm, faiss_index, user_question)
            st.write(st.session_state.answer)
            print(st.session_state.answer)
            st.success("Done")

    if st.button('Save Data'):
        if st.session_state.answer:
            current_time=datetime.now().strftime('%H%M%S')
            s3_key=f"output/{current_time}.txt"
            s3_bucket='articlebots'
            save_blog_details_s3(s3_key,s3_bucket,st.session_state.answer)
            st.success("Data is Saved on to the cloud")
            st.session_state.answer = ''
        else:
            st.error("Please generate data before you save it")
    


if __name__ == "__main__":
    main()
