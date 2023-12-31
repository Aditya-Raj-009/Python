import time
import pyttsx3
import datetime
import requests
import pyaudio
import speech_recognition as sr
import wikipedia  # to search on wikipedia.
import webbrowser  # for youtube and other task.
import os  # for song.
import smtplib  # for email sent.
import pywhatkit  # for playing song on youtube.
import pyautogui
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')  # use for voice.

voices = engine.getProperty('voices')  # to get voices
# print(voices)   # print no of voices present in your computer (output for this: 2 voices one male and one female).

engine.setProperty("voice", voices[1].id)  # to set voice.


# print(voices[0].id) # print a source which id name is David ..If we do voices[1].id it print Zira which a female voice.

def speak(audio):
    engine.say(audio)  # to speak
    engine.runAndWait()  # wait to speak.


def wishMe():  # wish according to time.
    hour = int(datetime.datetime.now().hour)  # get time in hour from 0-24.
    if 0 <= hour < 12:  # condition for morning.
        speak("Good Morning!")

    elif 12 <= hour < 16:  # condition for after noon.
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir, Please tell me how may I help you?")


def takeCommand():
    ''''It takes microphone input from the user and returns string as output:'''

    r = sr.Recognizer()  # class.
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete. mtlb jab jum wait kr 1 sec tak bolne keliye tab wo phase complete na kr de.
        r.energy_threshold = 4500  # minimum audio energy to consider for recording. this is a by default value. you can change it.

        audio = r.listen(source)  # to take voice from source.

    try:
        print("Recognising....")
        quer = r.recognize_google(audio, language='en-in')  # for recognising.
        print(f"User said : {quer}\n")

    except Exception as e:
        # print(e)
        print("I unable to hear you")
        speak("I unable to hear you")
        return "None"

    return quer


def sentEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 465)  # 587 is port
    server.ehlo()
    server.login("princesinghrajput@gmail.com", "prince@0806")
    server.sendmail("princesinghrajput08679@gmail.com", to, content)
    server.close()


if __name__ == '__main__':
    speak("Hello! Sir")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query:
        if 'wikipedia' in query or "search" in query:
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)  # return 2 senteces from wikipedia
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("Google.com")

        elif 'open stack overflow' in query:
            speak("opening stackOverFlow...")
            webbrowser.open("stackoverflow.com")

        elif 'play' in query:
            speak("opening youtube...")
            pywhatkit.playonyt(f"https://www.youtube.com//results?search_query={query[5::]}")
        #             if u want to play song from your directory:
        #             songs = os.listdir(music_dir)
        #             print(songs)
        #             os.startfile(os.path.join(music_dir,songs[0]))
        elif 'what the time' in query or "time right now" in query or "current time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The time is {strtime}")

        elif 'open vs code' in query or 'open visual studion code' in query:
            vscodepath = "C:\\Users\\Mithilesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)  # to open vs code.

        elif 'open pycharm' in query or 'open py charm' in query:
            pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.1\\bin\\pycharm64.exe"
            os.startfile(pycharm)

        elif 'open intellij' in query or 'open intelli j' in query:
            intellij = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.3.2\\bin\\idea64.exe"
            os.startfile(intellij)

        elif 'open chrome' in query:
            chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)

        elif 'open bluej' in query or 'open blue j' in query:
            bluej = "C:\\Program Files\\BlueJ\\BlueJ.exe"
            os.startfile(bluej)

        elif 'email to prince' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "princesinghrajput08679@gmail.com"
                sentEmail(to, content)
                speak("sir,Your email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry! Sir your email has not sent, please try again or check your internet connection!")

        elif "thank you" in query or "quit" in query:
            speak("Thank you sir!...closing programme please "
                  "wait!")
            time.sleep(2)
            break

        elif "what is your name" in query or "what's your name" in query:
            speak("Sir, My Name is Jarvis.")

        elif "who made you" in query:
            speak("Prince has mad me, sir")

        elif 'on whatsapp' in query or 'on whats app' in query:
            contact = {
                "sushil": "+917428814857",
                "vivekananda": "+918951513580",
                "priyanka": "+918210467420",
                "happy": "+918252800394",
                "mummy": "+917061624725",
                "daddy": "+918237550856",
                "rajnish": "+919661158554"
            }
            speak("To whom sir....")
            name = takeCommand().lower()
            speak("What is your message sir?")
            msg = takeCommand()
            speak(f"Ok sir pleas wait..opening whatsapp..")
            if "to" in name:
                name = name.replace("to ", "")
            try:
                if name in contact:
                    pywhatkit.sendwhatmsg(contact.get(name), msg, datetime.datetime.now().hour,datetime.datetime.now().minute + 1)
                    speak("Your message has been sent succesfully!")

                else:
                    speak("Contact Id is not present in database...please add or try again")

            except Exception as e:
                speak("Check for Internet connection..")

        elif "volume up" in query or "volume increase" in query:
            pyautogui.press('volumeup')

        elif 'volume dowm' in query or 'volume decrease' in query:
            pyautogui.press('volumedown')

        elif 'mute' in query:
            pyautogui.press('volumemute')

        elif "open camera" in query:
            import cv2
            speak("Ok! Sir Opening camera please wait...")
            cam = cv2.VideoCapture(0)
            while cam.isOpened():
                _, frame1 = cam.read()
                cv2.imshow("Jarvis Came!", frame1)
                q = takeCommand()
                if 'close' in q:
                    break
        elif "temperature" in query:
            # search = "temperature in jamshedpur"
            url = f"https://www.google.com/search?q={query}"
            r = requests.get(url).text
            data = BeautifulSoup(r,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            k = query.find("temperature")
            speak(f"{query[k::]} is {temp}")

        elif "close this window" in query or 'close this application' in query or 'close application' in query or 'close window' in query:
            speak("closing this window sir!")
            pyautogui.hotkey('Alt','F4')

        elif "repeat" in query:
            speak("Ok sir , Now I repeat you!")
            while True:
                repeat = takeCommand().lower()
                speak(repeat)
                if "thank you" in repeat or "thankyou" in repeat or "quit" in repeat:
                    speak("Thank you sir!")
                    break
