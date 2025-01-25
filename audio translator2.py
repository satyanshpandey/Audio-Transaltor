# Importing necessary libraries
import googletrans  # Google Translation API
import speech_recognition as sr  # Speech recognition module
import gtts  # Google Text-to-Speech for converting text to speech
import playsound  # Plays the audio files

from pydub import AudioSegment  # Pydub module for audio file manipulation

# Function to convert audio to mono and downsample to 16000 Hz
def convert_audio(input_file, output_file):
    # Audio file ko load karna
    sound = AudioSegment.from_wav(input_file)  # .wav file se audio ko read karna
    sound = sound.set_channels(1)  # Mono mein convert karna (1 channel)
    sound = sound.set_frame_rate(16000)  # Sample rate ko 16000 Hz pe set karna
    sound.export(output_file, format="wav")  # Output file ko save karna

# Usage of the function
input_file = "extracted_audio.wav"  # Input file, ensure the correct file path
output_file = "extracted_audio_fixed.wav"  # Output file path after conversion

convert_audio(input_file, output_file)  # Calling the function to convert the file

# Ab hum "extracted_audio_fixed.wav" pe speech recognition karenge

recognizer = sr.Recognizer()  # Speech recognition ka recognizer object bana rahe hain

audio_File = "extracted_audio.wav"  # Audio file jo hum use karenge

# Audio file ki properties ko check karte hain
import wave  # 'wave' module ko import kar rahe hain audio ke properties dekhne ke liye

# Audio file ko open karna aur uski properties ko print karna
with wave.open(audio_File, 'rb') as f:
    print(f.getnchannels())  # Channels (mono ya stereo) ka count
    print(f.getsampwidth())  # Sample width (in bytes)
    print(f.getframerate())  # Sample rate (Hz mein)
    print(f.getnframes())    # Total frames ka count

# Ab hum audio ko text mein convert karne ki koshish karenge
try:
    with sr.AudioFile(audio_File) as source:  # Audio file ko source banake recognize karna
        audio = recognizer.record(source)  # Audio ko record karna
    
    # Google ki API se audio ko text mein convert karna
    english_text = recognizer.recognize_google(audio)  # Audio ko Google API se text mein convert karna
    print("Recognized text: ", english_text)  # Recognized text print karna
    
    # Jo text recognize kiya usse Hindi mein translate karna
    translator = googletrans.Translator()  # Googletrans ke Translator object ko create kar rahe hain
    translation = translator.translate(english_text, dest="hi")  # Text ko Hindi mein translate karna
    translated_text = translation.text  # Translated text ko store karna
    print("Translated text (Hindi): ", translated_text)  # Translated text print karna
    
    # Translated text ko Hindi audio mein convert karna
    converted_audio = gtts.gTTS(translated_text, lang="hi")  # Hindi mein text-to-speech conversion
    converted_audio.save("convertedAudio.mp3")  # Converted audio ko file mein save karna
    
    # Ab hum converted Hindi audio ko play karenge
    playsound.playsound("convertedAudio.mp3")  # Converted audio ko play karna
    
except sr.UnknownValueError:  # Agar audio samajh nahi aaya
    print("Sorry, could not understand the audio!")
except sr.RequestError as e:  # Agar Google API se request ka error aaye
    print(f"Request error from Google API: {e}")
except Exception as e:  # Kisi aur error ko handle karna
    print(f"An error occurred: {e}")
