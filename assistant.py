import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import sys

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("🎙️ Neeharika:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎧 Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("🗣️ You said:", command)
            return command
    except sr.WaitTimeoutError:
        talk("No voice detected.")
    except sr.UnknownValueError:
        talk("Sorry , I didn’t catch that.")
    except sr.RequestError:
        talk("Network issue with Google service.")
    except Exception as e:
        talk(f"Error: {str(e)}")
    return ""

def run_neeha():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "").strip()
        try:
            talk(f"Playing {song} on YouTube 🎶")
            pywhatkit.playonyt(song)
        except:
            talk("Couldn't play that song. Something went wrong.")

    elif "what's the time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time} ⏰")

    elif "who is uday codes" in command or "who is uday_codes" in command:
        info = (
            "Uday, known as uday_codes on Instagram, is a coding content creator. "
            "He teaches Python projects in Telugu and runs udaycodes.in 💻"
        )
        talk(info)

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "open chrome" in command:
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        try:
            talk("Opening VS Code 💻")
            os.system("code")
        except:
            talk("VS Code is not installed or not added to PATH.")

    elif "exit" in command or "stop" in command:
        talk("Okay bro, see you later 👋")
        sys.exit()

    elif command != "":
        talk("I heard you, but I don’t understand that yet 😅")

# Start Assistant
talk("Hi! i am Neeharika – your personal voice assistant 💡")
while True:
    run_neeha()
    

