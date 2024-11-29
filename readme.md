# Text-to-Speech (TTS) Project

This project converts text from a file into speech using the Google Text-to-Speech (gTTS) library.

## Requirements

- Python 3.x
- gTTS library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/PrathamX595/testtospeech.git
    ```
2. Navigate to the project directory:
    ```sh
    cd <Your-directory>
    ```
3. Install the required library:
    ```sh
    pip install gtts
    ```

## Usage

1. Add the text you want to convert to speech in the `speak.txt` file.
2. Run the `tts.py` script:
    ```sh
    python tts.py
    ```
3. The script will generate an `talking.mp3` file and play it automatically.
4. we can most definitely make the script so that it accepts input from user

## Files

- `tts.py`: The main script that performs the text-to-speech conversion.
- `speak.txt`: The text file containing the text to be converted to speech.