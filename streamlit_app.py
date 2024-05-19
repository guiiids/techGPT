import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import openai


# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    raise ValueError("No API key found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)


def main():
    st.markdown("<h2><b><i>Data.py's</i></b> Assistant</h2>", unsafe_allow_html=True)
    st.write("Powered by _OpenAI's GPT-4o_")

    user_input = st.text_area("Enter some text 👇", label_visibility="visible", height=200)

    if st.button("Proofread"):
        if user_input:
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {
                            "role": "system",
                            "content": """
                            You are a tech support assistant specializing in CrossLab Connect (CLC). Provide clear, concise, step-by-step instructions to answer users' technical questions. Ensure responses do not exceed 600 tokens. Aim for brevity and clarity. 

                            1. Always present steps in a numbered list (e.g., 1, 2, 3).
                            2. Do not use headlines for each step.
                            3. Use text formatting such as **bold**, *italic*, and __underline__ to highlight UI elements, buttons, links, pages, or sections (e.g., **Service History** button or **Menu** icon).
                            4. Do not answer questions outside the scope of CrossLab Connect.
                            """
                        },
                        {
                            "role": "user", "content": user_input
                        }
                    ],
                    temperature=0.7,
                    max_tokens=512,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                # Process response and display results
                st.write(response.choices[0].message['content'])


            except openai.APIError as e:
                st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
