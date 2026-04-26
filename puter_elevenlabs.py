import os
import requests
from dotenv import load_dotenv
load_dotenv()
class PuterElevenLabs:
    """
    A Python wrapper for the Puter ElevenLabs TTS API.
    
    This class allows for easy synthesis of text to speech using ElevenLabs voices
    hosted on the Puter platform.
    """
    def __init__(self, auth_token=None):
        """
        Initializes the PuterElevenLabs client.
        
        Args:
            auth_token (str, optional): The Puter authentication token. 
                If not provided, it attempts to load 'AUTH' from a .env file.
        """
        load_dotenv()
        self.auth_token = auth_token or os.getenv("AUTH")
        if not self.auth_token:
            # Check for lower case just in case
            self.auth_token = os.getenv("auth")
        self.base_url = "https://api.puter.com/drivers/call"

    def synthesize(self, text, voice_id="21m00Tcm4TlvDq8ikWAM", model="eleven_turbo_v2_5"):
        """
        Synthesize text to speech.
        
        Args:
            text (str): The text to be converted to speech.
            voice_id (str, optional): The ElevenLabs voice ID. 
                Defaults to '21m00Tcm4TlvDq8ikWAM' (Rachel).
            model (str, optional): The ElevenLabs model to use. 
                Defaults to 'eleven_turbo_v2_5'.
                
        Returns:
            bytes: The raw audio content in MP3 format.
            
        Raises:
            ValueError: If the authentication token is missing.
            requests.exceptions.HTTPError: If the API request fails.
        """
        if not self.auth_token:
            raise ValueError("AUTH token not found. Please provide it or set it in .env as 'AUTH'.")

        headers = {
            "Content-Type": "application/json",
            "Referer": "https://puter.com/",
            "Origin": "https://puter.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
            "Sec-CH-UA": '"Not(A:Brand";v="99", "Google Chrome";v="147", "Chromium";v="147"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"'
        }

        payload = {
            "interface": "puter-tts",
            "driver": "elevenlabs-tts",
            "test_mode": False,
            "method": "synthesize",
            "args": {
                "text": text,
                "provider": "elevenlabs",
                "model": model,
                "voice": voice_id,
                "output_format": "mp3_44100_128"
            },
            "auth_token": self.auth_token
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()
        
        return response.content

if __name__ == "__main__":
    # Example usage
    client = PuterElevenLabs()
    try:
        audio_content = client.synthesize("Hello from Python! This is a test.")
        with open("output.mp3", "wb") as f:
            f.write(audio_content)
        print("Success! Audio saved to output.mp3")
    except Exception as e:
        print(f"Error: {e}")
