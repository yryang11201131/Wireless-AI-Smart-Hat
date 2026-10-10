"""
Wireless AI Smart Hat
ASR Module - Whisper Test

This script provides a standalone test for speech recognition
using whisper.cpp on Raspberry Pi.

Functions:
- Record audio from the microphone
- Save temporary WAV audio
- Run whisper.cpp
- Display recognized text
"""

import os
import wave
import tempfile
import subprocess

import numpy as np
import pyaudio


# ============================================================
# Configuration
# ============================================================

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK = 1024

RECORD_SECONDS = 5

WHISPER_BIN = os.path.expanduser(
    "~/whisper.cpp/build/bin/whisper-cli"
)

WHISPER_MODEL = os.path.expanduser(
    "~/whisper.cpp/models/ggml-tiny.bin"
)


# ============================================================
# Audio Recording
# ============================================================

def record_audio():
    """
    Record audio from the default microphone.
    """

    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=pyaudio.paInt16,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK
    )

    print("Recording...")

    frames = []

    total_chunks = int(
        SAMPLE_RATE / CHUNK * RECORD_SECONDS
    )

    for _ in range(total_chunks):
        data = stream.read(
            CHUNK,
            exception_on_overflow=False
        )
        frames.append(data)

    print("Recording finished.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return frames


# ============================================================
# Save WAV
# ============================================================

def save_wav(frames, filename):
    """
    Save recorded audio as a WAV file.
    """

    with wave.open(filename, "wb") as wav_file:
        wav_file.setnchannels(CHANNELS)
        wav_file.setsampwidth(2)
        wav_file.setframerate(SAMPLE_RATE)
        wav_file.writeframes(b"".join(frames))


# ============================================================
# Whisper Recognition
# ============================================================

def run_whisper(audio_path):
    """
    Run whisper.cpp and return recognized text.
    """

    command = [
        WHISPER_BIN,
        "-m",
        WHISPER_MODEL,
        "-f",
        audio_path,
        "-l",
        "zh",
        "--no-timestamps"
    ]

    print("Running Whisper...")

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Whisper execution failed.")
        print(result.stderr)
        return ""

    return result.stdout.strip()


# ============================================================
# Main
# ============================================================

def main():

    if not os.path.exists(WHISPER_BIN):
        print("Whisper executable not found:")
        print(WHISPER_BIN)
        return

    if not os.path.exists(WHISPER_MODEL):
        print("Whisper model not found:")
        print(WHISPER_MODEL)
        return

    frames = record_audio()

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_file:

        wav_path = temp_file.name

    try:
        save_wav(
            frames,
            wav_path
        )

        text = run_whisper(
            wav_path
        )

        print("\nRecognition Result:")
        print("-------------------")

        if text:
            print(text)
        else:
            print("No speech recognized.")

    finally:
        if os.path.exists(wav_path):
            os.remove(wav_path)


if __name__ == "__main__":
    main()