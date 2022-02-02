import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    '''speaks out the input string'''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    '''wish with intro'''
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir!")
    elif 12 <= hour <= 15:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir")

    speak("I am Jarvis, How may I help you?")


def takeCommand():
    '''takes input by listening to microphone and return a string output'''
    r = sr.Recognizer()
    my_mic = sr.Microphone(device_index=1)
    with my_mic as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("I can't hear that!")
        return ''

    return query


def sendMail(to, content):
    '''sends email from your account but first allow your email account to trust less safe applications'''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email', 'email-password')
    server.sendmail('your-email', to, content)
    server.close()


if __name__ == '__main__':
    # wishMe()
    while True:
        query = takeCommand().lower()
        query=query.replace('jarvis','')
        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to wikipedia: {results}")
        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'open google' in query:
            webbrowser.open('https://www.google.com')
        elif 'open stack overflow' in query:
            webbrowser.open('https://www.stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'C:\\Users\\sagar\\OneDrive\\Documents'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            curTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(curTime)
        elif 'open browser' in query:
            filePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(filePath)
        elif 'email to sagar' in query:
            try:
                speak("What do you want to write?")
                content = takeCommand()
                to = 'sagar.0dev@gmail.com'
                sendMail(to, content)
                speak("Mail sent successfully")
            except Exception as e:
                print(e)
                speak("Can't send your message\nPlease try again after sometime.")
        elif 'my' in query and 'name' in query:
            speak("Your name is Sagar Malhotra")
        elif 'exit' in query or 'quit' in query or 'sleep' in query or 'power off' in query:
            speak('Powering off...')
            break
        else:
            if query != '':
                query=query.replace('search google','')
                speak(f"Searching google for {query}")
                query = query.replace(' ', '+')
                webbrowser.open(f'https://www.google.com/search?q={query}')
