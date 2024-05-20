import requests
import json
import streamlit as st
from openai import OpenAI

# Get the API key from the environment variable
my_api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]
client = OpenAI(api_key=my_api_key)

st.title("External KB API")

# Your external KB URL
KB_URL = "https://help.ilab.agilent.com/"

# Your FAQs JSONL file
FAQS_JSONL = "files/dataset/faqs.jsonl"

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
    response_content = response.choices[0].message.content
    return response_content

# Main function to handle user queries
def main():
    user_query = st.text_input("Enter your query:")
    
    if st.button("Get Response"):
        # Check FAQs first
        for faq in faqs:
            if user_query.lower() in faq['question'].lower():
                st.write(f"Response: {faq['answer']}")
                return
        
        # Search KB
        kb_response = fetch_kb_article(user_query)
        if kb_response:
            st.write(f"Response: {kb_response}")
            return
        
        # If not found in KB, use GPT directly
        gpt_response = generate_completion(user_query, "")
        st.write(f"Response: {gpt_response}")

if __name__ == '__main__':
    main()
