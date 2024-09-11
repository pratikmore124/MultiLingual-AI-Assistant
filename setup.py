from setuptools import find_packages,setup

setup(
    name='multilingual assistant',
    version="0.0.1",
    author="Partik More",
    author_email="pratikmore124@gmail.com",
    packages=find_packages(),
    install_requires = ["SpeechRecognition",
    "pinwin",
    "pyaudio",
    "gTTS",
    "google-generativeai",
    "python-dotenv",
    "streamlit"]
)