import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os 
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("api_key")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)



# Function to generate audio from text
def generate_audio(text):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a teacher assistant, skilled in teaching a skill and code threw story and comedy"},
            {"role": "user", "content": text}
        ]
        )


    completion = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=completion.choices[0].message.content,
    )
    return completion

# Streamlit UI
st.title("AI Story Teacher App")
st.sidebar.title("About the App")
st.sidebar.info(
    "This app generates audio from text using OpenAI's GPT-3 model. "
    "It can be used to create narrations or audio stories from text input."
)

user_input = st.text_area("Enter text to convert to audio:")

if st.button("Generate Audio"):
    if user_input:
        st.text("Processing...")
        response = generate_audio(user_input)
        with st.spinner("Generating audio..."):
            response.stream_to_file("output.mp3")
        st.success("Audio generated successfully!")
    else:
        st.error("Please enter some text.")

# Download link for the generated audio
if st.button("Download Audio"):
    if Path("output.mp3").is_file():
        st.audio("output.mp3", format="audio/mp3")
        with open("output.mp3", "rb") as f:
            st.download_button(
                label="Click here to download",
                data=f,
                file_name="output.mp3",
                mime="audio/mp3",
            )
    else:
        st.error("No audio generated yet.")