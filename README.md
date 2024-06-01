# RaspAssist

RaspAssist is a Python project that uses speech recognition to take voice input from the user, sends the input to an AI model (llama3 and llava) hosted on a server, and uses TTS to generate and play the audio response.
It also has image processing capabillities so you can show it whats around you and ask any questions regarding your surrounding or what the camera sees.
Its basically a Rabit R1 clone but better and faster and the best part is the model itself runs on your own server.

## Features

- Voice input using speech recognition
- Text-to-speech output
- Integration with a hosted AI model for generating responses for both voice and image prompts

## Materials

- Raspberry pi any version which has wifi capabillities we will be using the pi4 modelB 8 Gb
- Raspberry pi cam v2
- USB microphone
- TFT touch display
- powerbank

## Prerequisites

- Python 3.x
- `speech_recognition` module
- `requests` module
- `dotenv` module

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/FaizanTabassum/RaspAssist.git
   ```

2. Navigate to the project directory:

   ```sh
   cd RaspAssist
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   However if we cant install the camera library using a virtual environment so we need to use the following method:

   use pip's argument `--break-system-packages`,
   add following lines to `~/.config/pip/pip.conf`:
   ```sh
   [global]
   break-system-packages = true
   ```

   Install the required Python packages using the above method:

   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys:

   ```sh
   OLLAMA_URL=https://your_ngrok_url
   ```
5. youl need to configure the mic and the lcd display, i have linked the following pages to do that at the bottom
   
## Usage

1. Run the main script:

   ```sh
   python ollama.py
   ```

2. Follow the prompts to speak your query, if you mention the word "picture" your query the model will take a picture from the camera and whatever you say after the word picture it will concider as the query or prompt for that image.

## Additional Resources

- [Display setup](https://core-electronics.com.au/guides/small-screens-raspberry-pi/): Information on how to setup the display.
- [Ollama Docker Image](https://hub.docker.com/r/ollama/ollama): Information on how to use the Ollama Docker image.
- [Generate Ollama request](https://github.com/ollama/ollama/blob/main/docs/api.md):How to do the API calls
- [Ngrok](https://dashboard.ngrok.com/get-started/setup/windows): You can find the Ngrok commands here.
- [Ngrok Tutorial](https://www.youtube.com/watch?v=Tg84mhnAhuA): A video tutorial on how to use Ngrok.

