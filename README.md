# Puter ElevenLabs Python Wrapper

A lightweight Python wrapper for using ElevenLabs Text-to-Speech (TTS) via the [Puter.com](https://puter.com) API.

## Features

- **Simple API**: Synthesize speech with just a few lines of code.
- **Environment Integration**: Automatic loading of authentication tokens from `.env` files.
- **Customizable**: Full control over text, voice IDs, and models.
- **Modern Compatibility**: Includes 2026-compliant headers and User-Agents for reliable API access.

## Installation

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install requests python-dotenv
   ```

## Configuration

Create a `.env` file in your project root and add your Puter authentication token:

```env
AUTH=your_puter_auth_token_here
```

## Usage

### Basic Example

```python
from puter_elevenlabs import PuterElevenLabs

# Initialize the client (automatically loads AUTH from .env)
client = PuterElevenLabs()

# Synthesize text
audio_data = client.synthesize("Hello! This is a test of the ElevenLabs wrapper.")

# Save to file
with open("output.mp3", "wb") as f:
    f.write(audio_data)
```

### Advanced Usage

You can specify custom voices and models:

```python
audio_data = client.synthesize(
    text="Custom voice test.",
    voice_id="pMsXg91YvYl8mInSIsAs", # Example Voice ID
    model="eleven_multilingual_v2"   # Example Model
)
```

## API Reference

### `PuterElevenLabs(auth_token=None)`
- **auth_token**: Optional. If not provided, the wrapper looks for `AUTH` in your environment or `.env` file.

### `client.synthesize(text, voice_id="...", model="...")`
- **text**: The string you want to convert to speech.
- **voice_id**: The ElevenLabs voice ID (default: Rachel `21m00Tcm4TlvDq8ikWAM`).
- **model**: The ElevenLabs model (default: `eleven_turbo_v2_5`).
- **Returns**: `bytes` (raw MP3 data).

## License

MIT
