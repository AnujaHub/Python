import speech_recognition as sr
import webbrowser
import pyttsx3
# import musicLib

engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open github" in c.lower():
        webbrowser.open("https://www.github.com")
    else:
        speak("Command not recognized. Please try again.")

    
# good practice as it runs only when file is executed directly 
if __name__ == "__main__":
    speak("Initializing Assistant...")
    r = sr.Recognizer()
    
    while True:
        try:
            # Use the microphone as source
                # with sr.Microphone() as source:
                #      print("Listening...")
                    #  r.adjust_for_ambient_noise(source, duration=1)
                    #  audio = r.listen(source)
                    #  wake = r.recognize_google(audio)

                    #  if(wake.lower() == "siri"):
                    #      speak(" Yes , how may i help you")
                 

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