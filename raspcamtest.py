import os
import time
import requests
import json
from picamera import PiCamera

# Set up the Raspberry Pi camera
camera = PiCamera()

# Define the Llama API endpoint
API_URL = os.getenv("OLLAMA_URL")

# Function to capture photo and send it to Llama API


def capture_and_process_photo():
    # Capture a photo
    image_path = "/home/pi/photo.jpg"
    camera.start_preview()
    time.sleep(2)  # Allow the camera to adjust to light levels
    camera.capture(image_path)
    camera.stop_preview()

    # Send the photo to Llama API
    with open(image_path, "rb") as file:
        files = {"file": file}
        payload = {
            'model': 'llama3',
            'stream': False,
            'eval_count': 50  # Adjust the number of tokens for shorter replies
        }
        response = requests.post(API_URL, files=files, data=payload)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Process the response JSON
            response_data = json.loads(response.text)
            response_text = response_data['response']
            print("Llama Response:", response_text)
        else:
            print(
                f"Received response with status code: {response.status_code}")
            print(response.text)

# Main function


def main():
    # Capture and process the photo
    capture_and_process_photo()


# Execute the main function
if __name__ == "__main__":
    main()
