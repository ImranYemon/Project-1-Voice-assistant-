# Imports for the program
import speech_recognition as sr 
import webbrowser
import pyttsx3 

# Objects
recognizer =  sr.Recognizer()
engine = pyttsx3.init()
# Functions
def speak (text):
    engine.say(text)
    engine.runAndWait()

def process_command(c) :
    # Google
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    # Facebook
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com/")
    # Youtube
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    # Instagram
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com/")
    # LinkedIn
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com/")

# Starting for the program
if __name__ == "__main__":
    speak("Initializing ...")

# lestening for the weke word 
    while True :
        r = sr.Recognizer()
# Getting the source form the microphone 
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source , timeout=3 , phrase_time_limit=2 )
                print("recognizing ...")

            Word = r.recognize_google(audio)
    # Program will activated when the Wake up word Imran called. 
            if (Word.lower() == "imran") :
                speak ("Yes brother , tell me what can I do for you ?")

                with sr.Microphone() as source:
                    print("Activated...")
                    audio = r.listen(source )
                    command = r.recognize_google(audio)

                process_command(command)
                


        except Exception as e:
            print("error; {0}".format(e))