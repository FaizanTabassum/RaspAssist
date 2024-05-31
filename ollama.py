import os
import speech_recognition as sr
import pyttsx3
import requests
import json
import base64
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
from picamera2 import Picamera2
import time

def capture_image(filename):
    # Initialize the camera
    picam2 = Picamera2()

    # Configure the camera settings
    picam2.start()

    # Allow the camera to warm up
    time.sleep(2)

    # Capture the image
    picam2.capture_file(filename)

    # Stop the camera
    picam2.stop()
    print(f"Image saved")

# Load environment variables from .env file
load_dotenv()

# Define the API endpoints and keys
OLLAMA_URL = os.getenv("OLLAMA_URL")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Initialize text-to-speech engine
engine = pyttsx3.init()


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


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


def speak_response(text):
    engine.say(text)
    engine.runAndWait()


def handle_text_query(query):
    payload = {
        'model': 'llama3',
        'prompt': query,
        'stream': False,
        'eval_count': 50
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        response_text = response_data['response']
        print("Response:", response_text)
        speak_response(response_text)
    else:
        print(f"Received response with status code: {response.status_code}")
        print(response.text)


def handle_image_query(image_path, query):
    encoded_image = encode_image_to_base64(image_path)
    payload = {
        "model": "llava",
        "prompt": query,
        "stream": False,
        "images": [encoded_image]
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        response_text = response_data['response']
        print("Response:", response_text)
        speak_response(response_text)
    else:
        print(f"Received response with status code: {response.status_code}")
        print(response.text)


def main():
    while True:
        print("Listening to your query...")
        query = recognize_speech()
        if query:
            if "picture" in query.lower():
                capture_image("image.jpg")
                # Replace 'image.jpg' with your image file name
                image_path = os.path.join(
                    os.path.dirname(__file__), 'image.jpg')
                query_parts = query.split("picture", 1)
                image_query = query_parts[1].strip() if len(
                    query_parts) > 1 else ""
                handle_image_query(image_path, image_query)
            else:
                handle_text_query(query)


if __name__ == "__main__":
    main()
