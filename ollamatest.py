import speech_recognition as sr
import pyttsx3
import requests
import json
from elevenlabs import play  # for generate and speak
from elevenlabs.client import ElevenLabs
# from elevenlabs import stream  # for stream

client = ElevenLabs(
    api_key="bd22d7ba346ff621923887bf18f7781a",  # Defaults to ELEVEN_API_KEY
)

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
        print("Could not request results; {0}".format(e))
        return ""

# Function to speak the response


def speak_response(textaudio):
    # engine = pyttsx3.init()
    # engine.say(text)
    # engine.runAndWait()

    # this is to first generate then speak
    audio = client.generate(
        text=textaudio,
        voice="Rachel",
        model="eleven_multilingual_v2",

    )
    play(audio)

    # this is to stream the audio in realtime as its being generated
    # audio_stream = client.generate(
    #     text=textaudio,
    #     stream=True
    # )
# stream(audio_stream)


# Define the API endpoint
url = 'http://localhost:11434/api/generate'

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
        response = requests.post(url, json=payload)

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
                f'Received response with status code: {response.status_code}')
            print(response.text)
