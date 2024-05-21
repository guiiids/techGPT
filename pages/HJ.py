import streamlit as st
import requests


# Function to query Help Juice API
def query_helpjuice_api(api_key, query):
    url = "https://api.helpjuice.com/v1/articles/search"
    headers = {

        "Authorization": f"Bearer {api_key}",

        "Content-Type": "application/json"

    }
    params = {

        "query": query

    }
    response = requests.get(url, headers=headers, params=params)

    return response.json() if response.status_code == 200 else None


# Streamlit App

st.title("Help Juice API Query")

st.write("Search for articles related to Invoices")

api_key = st.text_input("Enter your Help Juice API Key", type="password")

query = "Invoices"

if st.button("Search"):

    if api_key:

        results = query_helpjuice_api(api_key, query)

        if results:

            st.write("Search Results:")

            for article in results['articles']:
                st.subheader(article['title'])

                st.write(article['content'][:200] + "...")  # Display a snippet of the content

                st.write(f"[Read more]({article['url']})")

        else:

            st.error("Failed to retrieve results or no results found.")

    else:

        st.error("API Key is required!")

# To run the Streamlit app, save this script and execute: streamlit run script_name.py
