import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.2
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        return "None"
    return query


def speak(audio):
    engine.say(audio) 
    print(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good Morning Abhy! I am Katie, How can I help you?")
    elif hour >12 and hour < 18:
        speak("Good Afternoon Abhy! I am Katie, How can I help you?")
    else:
        speak("Good Evening Abhy! I am Katie, How can I help you?")


def main():
    print('in main')
    wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")

            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open spotify' in query:
            codePath = "C:\\Users\\Star\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(codePath)

        elif 'open code' in query:
            codePath = "C:\\Users\\Star\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'how are you' in query:
            speak("I am fine, Abhy! How are you?")
        elif 'quit' in query:
            speak("GoodBye!")
            exit()
        elif 'stop' in query:
            speak("GoodBye!")
            exit()
if __name__ == '__main__':
    main()