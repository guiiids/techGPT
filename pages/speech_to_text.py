import os
import time
import streamlit as st
from openai import OpenAI
import openai

# Get the API key from the environment variable


my_api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)
st.title("Speech-To-Text Helper")

# Path to the audio file
audio_file_path = 'files/audio/smart_alerts.mp3'

# Open the audio file
with open(audio_file_path, "rb") as audio_file:
    # Transcribe the audio using OpenAI's Whisper model
    transcription.text = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

    # Extract the transcribed text
    transcribed_text = transcription.text
    st.write(transcribed_text)

    # Save the transcription to a text file
    with open('transcription.txt', 'w') as file:
        file.write(transcribed_text)
        
    with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

print("Transcription saved to transcription.txt")
