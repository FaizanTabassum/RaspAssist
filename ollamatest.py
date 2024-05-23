import os
import speech_recognition as sr
import pyttsx3
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the API endpoint
OLLAMA_URL = os.getenv("OLLAMA_URL")

# Function to recognize speech


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Function to speak the response


def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


while True:
    # Get user query
    query = recognize_speech()
    if query:
        # Define the payload
        payload = {
            'model': 'llama3',
            'prompt': query,
            'stream': False,
            'eval_count': 50  # Adjust the number of tokens for shorter replies
        }

        # Send the POST request
        response = requests.post(OLLAMA_URL, json=payload)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Process the response JSON
            response_data = json.loads(response.text)
            response_text = response_data['response']
            print("Response:", response_text)

            # Speak the response
            speak_response(response_text)

            # Listen for the next query
            continue
        else:
            print(
                f"Received response with status code: {response.status_code}")
            print(response.text)
