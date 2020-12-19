import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, Miss")
    elif hour>=12 and hour<18:
        speak("Good Afternoon, Miss")
    else:
        speak("Good Evening Miss")

    speak("How can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
       # r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception :
        speak("Sorry Miss, didn't catch that.")
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    speak("Hello, I'm Jarvis")
    wishMe()
    
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'play music' in query:
            music_dir = 'C:\\Users\\KIIT\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[2]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Miss, the time is {strTime}")

        elif 'sign out' in query:
         speak("okay miss, signing off")
         break

        elif 'spotify' in query:
            webbrowser.open("https://open.spotify.com/")

            
        

        


