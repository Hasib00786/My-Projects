import subprocess
import pyttsx3
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import shutil
from ecapture import ecapture as ec
from urllib.request import urlopen
from gtts import gTTS

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
        print("Good Morning Sir !")

    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")
        print("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")
        print("Good Evening Sir !")

    assname = "Terminator 1 point o"
    speak("I am your Assistant")
    print("I am your Assistant \n Terminator 1.0")
    speak(assname)


def usrname():
    speak("What should i call you sir")
    print("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("😎😎😎😎😎😎😎😎😎😎".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("😎😎😎😎😎😎😎😎😎😎".center(columns))

    speak("How can i Help you, Sir")
    print("How can i Help you, Sir")

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your email', 'password')
    server.sendmail('your email', to, content)
    server.close()

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]


if __name__ == '__main__':
    clear = lambda: os.system('cls')


    clear()
    wishMe()
    usrname()

    while True:

        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'play music online' in query or "play song online" in query:
            speak("Here you go with music")
            webbrowser.open("https://www.jiosaavn.com/")

        elif 'play local music' in query or 'play song' in query:
            speak("trying to make you feel better with music")
            music_dir = "E:/download"
            songs=os.listdir(music_dir)
            print(songs)
            rand=random.randint(0,232)
            random=os.startfile(os.path.join(music_dir,songs[rand]))

        elif 'the time' in query or 'date' in query:
            strTime = datetime.datetime.now()
            t1=strTime.strftime("%H:%M:%S")
            D1=strTime.strftime("%d/%m/%y")
            print("THE DATE IS:",D1)
            print("TIME IS:",t1)
            speak(f"Sir, the date and time is {strTime}")


        elif 'send an email' in query or 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif 'exit' in query or 'terminate' in query:
            speak("Thanks for giving me your time")
            print("Thanks for giving me your time")
            exit()

        elif 'hello' in query or 'hi' in query:
            speak("hello sir How are you.. Tell me how may I help you")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by a group of students of G I E T University.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query or 'calculation' in query:
            speak("What do you want to calculate")
            my_string=takeCommand()
            print(my_string)

            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            print(eval_binary_expr(*(my_string.split())))


        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to world" in query:
            speak("Thanks to the students. further It's a secret")

        elif 'open presentation' in query:
            speak("opening Power Point presentation")
            os.startfile("E:/Python files/3RD SEM PROJECT.pptx")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by Haseeb")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by the students of G I E T University")

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "Location of wallpaper",0)
            speak("Background changed succesfully")

        elif 'news' in query:

            try:
                jsonObj = urlopen('''https://timesofindia.indiatimes.com/''')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')

                for item in data['articles']:

                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")

        elif "take a photo" in query or "open camera" in query:
            ec.capture(0, "User Camera ", "img.jpg")


        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('new_document.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now()
                t1=strTime.strftime("%H:%M:%S")
                D1=strTime.strftime("%d/%m/%y")
                file.write(D1)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "open note" in query:
            speak("Showing Notes")
            file = open("new_document.txt", "r")
            print(file.read())
            speak(file.read(6))

        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "terminator" in query:

            wishMe()
            speak("terminator 1 point o in your service Mister")
            speak(assname)

        elif "weather" in query or 'how is the weather' in query:
            print("Showing you the weather report for your location")
            speak("Showing you the weather report for your location")
            webbrowser.open('https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57j69i59j69i60l6.1633j0j7&sourceid=chrome&ie=UTF-8')


        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad to meet you")

        elif "i love you" in query:
            mytext="प्यार एक धोखा है, पढ़ लो बेटा अब भी मौका है"
            la='hi'
            obj=gTTS(text=mytext,lang=la,slow=False)
            obj.save("love.mp3")
            os.startfile("love.mp3")



        elif 'who is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif "amazing" in query or "good" in query or "nice" in query:
            speak("Thankyou ..")
            speak("The credit goes to my developer . If you have any queries regarding me you can contact him.")
            speak("Do you need to contact him")
            query=takeCommand().lower()

            if "yes" in query or "ya" in query:
                print("🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️")
                print("MAIL ID - 19cse328.mdhasiburrahman@giet.edu")
                print("CONTACT NUMBER - 9348479792")
                print("🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️🏳️")

            elif "no" in query or "sorry" in query:
                speak("Thanks for giving me your time:")


