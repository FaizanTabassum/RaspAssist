# RaspAssist

RaspAssist is a Python project that uses speech recognition to take voice input from the user, sends the input to an AI model hosted on a server, and uses ElevenLabs to generate and play the audio response.

## Features

- Voice input using speech recognition
- Text-to-speech output using ElevenLabs
- Integration with a hosted AI model for generating responses

## Prerequisites

- Python 3.x
- `speech_recognition` module
- `requests` module
- `elevenlabs` module
- `dotenv` module

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/RaspAssist.git
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

4. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your API keys:

   ```sh
   ELEVENLABS_API_KEY=your_elevenlabs_api_key
   OLLAMA_URL=https://your_ngrok_url
   ```

## Usage

1. Run the main script:

   ```sh
   python ollamatest.py
   ```

2. Follow the prompts to speak your query.

## Additional Resources

- [Ollama Docker Image](https://hub.docker.com/r/ollama/ollama): Information on how to use the Ollama Docker image.
- [ElevenLabs API Documentation](https://elevenlabs.io/docs/api-reference/getting-started): Learn how to use the ElevenLabs API.
- [Ngrok](https://dashboard.ngrok.com/get-started/setup/windows): You can find the Ngrok commands here.
- [Ngrok Tutorial](https://www.youtube.com/watch?v=Tg84mhnAhuA): A video tutorial on how to use Ngrok.

