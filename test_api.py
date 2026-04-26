from puter_elevenlabs import PuterElevenLabs

def test_synthesis():
    print("Testing Puter ElevenLabs Wrapper...")
    client = PuterElevenLabs()
    
    try:
        # Using the requested parameters
        text = "Hello! This is a test of the Puter ElevenLabs wrapper."
        voice_id = "21m00Tcm4TlvDq8ikWAM"
        model = "eleven_turbo_v2_5"
        
        print(f"Synthesizing: '{text}' using voice '{voice_id}' and model '{model}'")
        audio_content = client.synthesize(text, voice_id=voice_id, model=model)
        
        with open("test_output.mp3", "wb") as f:
            f.write(audio_content)
            
        print("Success! Test audio saved to test_output.mp3")
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == "__main__":
    test_synthesis()
