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
        print(f"User said: {query}")
    except Exception as e:
        speak("Sorry, I can't hear that!")
        print("Sorry, I can't hear that!")
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
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == 'jarvis':
            speak('Yes? Is there any thing you want?')
        query = query.replace('jarvis', '')

        if 'say' in query:
            query = query.replace('say', '')
            speak(query)
        elif 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to wikipedia: {results}")
        elif 'open browser' in query:
            speak("Opening Your default browser..")
            filePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(filePath)
        elif 'open android studio' in query:
            speak("Opening Android Studio..")
            filePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
            os.startfile(filePath)
        elif 'open ' in query:
            query = query.split('open ')
            query = query[1]
            query = query.split(' ')
            query = query[0]
            speak(f"Opening {query}")
            url = f"www.{query}.com"
            webbrowser.open(url)
        elif 'play music' in query:
            speak("Playing Music..")
            music_dir = 'C:\\Users\\sagar\\OneDrive\\Documents'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            curTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(curTime)
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
            speak("Sir, Your name is Sagar Malhotra")
        elif 'intro' in query or 'introduction' in query:
            speak("Hi. I'm Jarvis, The Artificial Intelligent Software Program. Speed 1 terahertz, memory 1 zetabyte. "
                  "Hmm, Don't panic, that's just a flex "
                  "Introduction. I am still a basic Python Program created by Sagar. But, who knows When we "
                  "can rule this world, haha.")
        elif 'exit' in query or 'quit' in query or 'sleep' in query or 'power off' in query or 'so jao' in query:
            speak('So, Is that everything you want? You know what? I am going now. Bye .')
            break
        elif 'joke' in query:
            speak("Currently I can't do that, Isn't that any lesser than a joke?")
            # use joke api
        else:
            if query != '':
                query = query.replace('what is', '')
                query = query.replace('google for', '')
                query = query.replace('on google', '')
                query = query.replace('google', '')
                query = query.replace('search', '')
                speak(f"Searching google for {query}")
                query = query.replace(' ', '+')
                webbrowser.open(f'https://www.google.com/search?q={query}')
