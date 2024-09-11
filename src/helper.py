import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv
import os
from gtts import gTTS

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY  # setting as tempory environment variable

def voice_input():
    r = sr.Recognizer()
    audio = ""
    
    # Correct instantiation of Microphone with parentheses
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry! Could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")
def text_to_speech(text):
    tts = gTTS(text=text,lang="en")
    tts.save("speech.mp3")

def llm_model_object(user_text):
    model = "models/gemini-pro"

    response = model.generate_content(user_text)
    result = response.text

    return result
