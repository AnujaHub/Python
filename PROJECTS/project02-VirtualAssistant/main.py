import speech_recognition as sr
import webbrowser
import pyttsx3
import win32com.client
import musicLib
import time
from dotenv import load_dotenv
import os
import requests


speaker = win32com.client.Dispatch("SAPI.SpVoice")
load_dotenv("../../env/.env")
newsApi = os.getenv("NEWS_API")

def speak(text):
    speaker.Speak(text)

def processCommand(c):
    c = c.lower() 

    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
    }

    for key , url in sites.items():
        if key in c:
            webbrowser.open(url)
            speak(f"Opening {key}")
            return
        
    if c.startswith("play"):
        song = " ".join(c.split(" ")[1:])
        if song in musicLib.music:
            webbrowser.open(musicLib.music[song])
            speak(f"Playing {song} on Spotify")
        else:
            speak("song not found")
        return 

    if "news" in c:
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?q=latest&apiKey={newsApi}&pageSize=5")
            print(r.status_code)
            r.raise_for_status()
            news_data = r.json()
            articles = news_data.get('articles', [])
            if articles:
                for article in articles:
                    speak(article['title'])
            else:
                speak("No news articles found.")
        except requests.exceptions.RequestException:
            speak("Sorry, I could not fetch the news.")
        return
    
    speak("Command not recognized. Please try again.")

    
# good practice as it runs only when file is executed directly 
if __name__ == "__main__":
    speak("Initializing Assistant...")
    r = sr.Recognizer()
    
    while True:
        try:
            # Use the microphone as source
                with sr.Microphone() as source:
                     print("Listening...")
                     r.adjust_for_ambient_noise(source, duration=1)
                     audio = r.listen(source)
                     wake = r.recognize_google(audio)

                if(wake.lower() == "siri"):
                    speak(" Yes , how may i help you")
                    time.sleep(0.6)

                       # listening for command
                    with sr.Microphone() as source:
                        print("Siri Activated...")
                        audio = r.listen(source)
                        command = r.recognize_google(audio)
                        processCommand(command)
                        
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")