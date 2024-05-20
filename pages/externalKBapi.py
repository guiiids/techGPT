from flask import Flask, request, jsonify
import requests
from elasticsearch import Elasticsearch
import json
import os
import streamlit as st
from openai import OpenAI
import openai


# Get the API key from the environment variable

my_api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)
st.title("External KB API")

# Your external KB URL
KB_URL = "https://help.ilab.agilent.com/"

# Your FAQs JSONL file
FAQS_JSONL = "faqs.jsonl"

# Load FAQs from JSONL
def load_faqs():
    faqs = []
    with open(FAQS_JSONL, 'r') as f:
        for line in f:
            faqs.append(json.loads(line))
    return faqs

faqs = load_faqs()

# Fetch article from external KB
def fetch_kb_article(query):
    response = requests.get(f"{KB_URL}/search?q={query}")
    return response.json()

# Generate a response using GPT
def generate_completion(query):
    response = client.chat.completions.create(
        engine="gpt-4o",
        prompt=f"{context}\nUser Query: {query}\nAssistant:",
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # return response.choices[0].text.strip()
    response_content = response.choices[0].message.content

# Endpoint for handling user queries
@app.route('/query', methods=['POST'])
def handle_query():
    user_query = request.json.get('query')

    # Check FAQs first
    for faq in faqs:
        if user_query.lower() in faq['question'].lower():
            return jsonify({'response': faq['answer']})

    # If not in FAQs, search KB
    kb_response = fetch_kb_article(user_query)
    if kb_response:
        return jsonify({'response': kb_response})

    # If not found in KB, use GPT
    gpt_response = generate_completion(user_query)
    return jsonify({'response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)

# Generate a response using GPT
def generate_completion(query, context):
    response = client.chat.completions.create(
        engine="gpt-4o",
        prompt=f"{context}\nUser Query: {query}\nAssistant:",
        max_tokens=250,
        n=1,
        stop=None,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # return response.choices[0].text.strip()
    response_content = response.choices[0].message.content

# Endpoint for handling user queries
@app.route('/query', methods=['POST'])
def handle_query():
    user_query = request.json.get('query')

    # Check FAQs first
    for faq in faqs:
        if user_query.lower() in faq['question'].lower():
            return jsonify({'response': faq['answer']})

    # Search KB
    kb_results = search_kb(user_query)
    if kb_results:
        relevant_sections = extract_relevant_section(kb_results, user_query)
        if relevant_sections:
            context = "\n".join(relevant_sections[:3])  # Use top 3 relevant sections
            gpt_response = generate_completion(user_query, context)
            return jsonify({'response': gpt_response})

    # If not found in KB, use GPT directly
    gpt_response = generate_completion(user_query, "")
    return jsonify({'response': gpt_response})

if __name__ == '__main__':
    app.run(debug=True)
