import googletrans
import speech_recognition as sr
import gtts
import playsound

from pydub import AudioSegment

# Convert to mono and downsample to 16000 Hz
def convert_audio(input_file, output_file):
    sound = AudioSegment.from_wav(input_file)
    sound = sound.set_channels(1)  # Convert to mono
    sound = sound.set_frame_rate(16000)  # Downsample to 16000 Hz
    sound.export(output_file, format="wav")

# Usage
input_file = "extracted_audio.wav"
output_file = "extracted_audio_fixed.wav"

convert_audio(input_file, output_file)

# Now proceed with your speech recognition on "extracted_audio_fixed.wav"








recognizer = sr.Recognizer()

audio_File = "extracted_audio.wav"  # Make sure this file exists and is in the correct format


import wave

with wave.open(audio_File, 'rb') as f:
    print(f.getnchannels())  # Number of audio channels
    print(f.getsampwidth())  # Sample width in bytes
    print(f.getframerate())  # Sample rate
    print(f.getnframes())    # Number of frames




try:
    with sr.AudioFile(audio_File) as source:
        audio = recognizer.record(source)
    
    # Convert audio to text using Google's recognition API
    english_text = recognizer.recognize_google(audio)
    print("Recognized text: ", english_text)
    
    # Translate the recognized text into Hindi using googletrans
    translator = googletrans.Translator()  # Fixed the typo here
    translation = translator.translate(english_text, dest="hi")
    translated_text = translation.text
    print("Translated text (Hindi): ", translated_text)
    
    # Convert translated text into Hindi audio using gTTS
    converted_audio = gtts.gTTS(translated_text, lang="hi")
    converted_audio.save("convertedAudio.mp3")
    
    # Play the converted audio in Hindi
    playsound.playsound("convertedAudio.mp3")
    
except sr.UnknownValueError:
    print("Sorry, could not understand the audio!")
except sr.RequestError as e:
    print(f"Request error from Google API: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
