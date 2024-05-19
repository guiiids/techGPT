import os
import streamlit as st
from openai import OpenAI
import openai


# Load environment variables from .env file

# Get the API key from the environment variable
client = OpenAI(api_key="sk-proj-FBMfNzQ9tgPTVEBLMSrXT3BlbkFJHR12R0vKrUknUaGsqvh0")




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
                            2. Double check your knowledge before answering the question. Cross check your reasoning versus the knowledge you have, to see if your answer is accurate and detailed.
                            3. Always output hyperlinks when possible. 
                            4. Do not use headlines for each step.
                            5. Use text formatting such as **bold**, *italic*, and __underline__ to highlight UI elements, buttons, links, pages, or sections (e.g., **Service History** button or **Menu** icon).
                            6. Do not answer questions outside the scope of CrossLab Connect.

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
                response_content = response.choices[0].message.content

                # Print the entire response for debugging purposes
                # st.write("Debug Info: Full Response")
                st.write(response_content)

                
            except openai.error.OpenAIError as e:
                st.error(f"An error occurred: {e}")
if __name__ == "__main__":
    main()
