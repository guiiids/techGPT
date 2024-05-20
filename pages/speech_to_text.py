import os
import streamlit as st
from openai import OpenAI
import openai

# Get the API key from the environment variable


my_api_key = st.secrets["api_keys"]["OPENAI_API_KEY"]

client = OpenAI(api_key=my_api_key)

# Path to the audio file
audio_file_path = 'files/audio/smart_alerts.mp3'

# Open the audio file
with open(audio_file_path, "rb") as audio_file:
    # Transcribe the audio using OpenAI's Whisper model
    transcription = openai.Audio.transcribe(
        model="whisper-1",
        file=audio_file
    )

    # Extract the transcribed text
    transcribed_text = transcription['text']

    # Save the transcription to a text file
    with open('transcription.txt', 'w') as file:
        file.write(transcribed_text)

print("Transcription saved to transcription.txt")
