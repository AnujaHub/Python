
import speech_recognition as sr
import webbrowser
import pyttsx3
import win32com.client
import musicLib
import time



speaker = win32com.client.Dispatch("SAPI.SpVoice")


def speak(text):
    speaker.Speak(text)

def processCommand(c):
    c = command.lower() 

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