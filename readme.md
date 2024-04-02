# AI Story Teacher App

The AI Story Teacher App is a web application that generates audio narration from text input using OpenAI's GPT-3 model. It can be used to convert written text into spoken audio, making it useful for creating narrations, audio stories, or generating speech from any textual content.

## How to Use

1. Enter the text you want to convert to audio in the text area provided.
2. Click on the "Generate Audio" button to generate audio from the entered text.
3. Once the audio is generated, you can listen to it directly on the app or download it as an MP3 file by clicking the "Download Audio" button.

## About the App

This app utilizes OpenAI's GPT-3 model for text-to-speech conversion. It provides a simple and intuitive interface for generating audio from text, making it accessible for various purposes such as storytelling, content creation, or accessibility for visually impaired users.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [OpenAI](https://pypi.org/project/openai/)

## Setup

1. Clone this repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory and add your OpenAI API key in the following format:
```env
api_key=YOUR_API_KEY_HERE
```

4. Run the Streamlit app using the command `streamlit run main.py`.
5. Access the app in your web browser at the provided URL.


## License

This project is licensed under the [MIT License](LICENSE).
