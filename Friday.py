import pyttsx3
import pywhatkit
import speech_recognition as sr
import datetime
import os
import wikipedia
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("Please wait for a moment...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You just said:{query}\n")
    except Exception as e:
        print(e)
        speak("Please say it again...")
        query = "none"
    return query


query = commands().lower()


def wishings():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        print("Good Morning boss, I am Friday")
        speak("Good Morning Boss, I am Friday")
    elif hour >= 12 and hour < 16:
        print("Good afternoon boss, I am Friday")
        speak("Good Afternoon boss, I am Friday")
    elif hour >= 16 and hour < 20:
        print("Good Evening boss, I am Friday")
        speak("Good Evening boss, I am Friday")
    else:
        print("Good night boss, I am Friday")
        speak("Good Night Boss, I am Friday")


if __name__ == "__main__":
    wishings()
    query = commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strTime)
        speak(f"Sir, the time is {strTime}")

    elif 'chrome' in query:
        speak("Opening chrome boss..")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    elif 'wikipedia' in query:
        speak("Searching in Wikipedia..")
        try:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia..")
            print(results)
            speak(results)
        except:
            speak("No results found")
            print("No results found")

    elif 'play' in query:
        query = query.replace('play', '')
        speak("playing" + query)
        pywhatkit.playonyt(query)

    elif 'type' in query:
        query = query.replace('type', '')
        speak("What should I type boss?")
        pyautogui.write(query)

    elif 'exit program' in query:
        speak("Exiting boss..")
        quit()
