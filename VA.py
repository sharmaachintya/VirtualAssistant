import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)
newVoiceRate=150
engine.setProperty('rate',newVoiceRate)

def speak(audio):                                    
    engine.say(audio)
    engine.runAndWait()

def time():
    time=datetime.datetime.now().strftime("%I:%M:%S") 
    speak("Time right now is")
    speak(time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("Today is")
    speak(date)
    speak(month)
    speak(year)

def greet():
    speak("Welcome Back Bhaiji!")
    '''
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good Morning")
    elif hour >= 12 and hour <=18:
        speak("Good Evening")
    elif hour >= 18 and hour <= 24:
        speak("Good Night")
    else:
        speak("Soja")
    '''
    speak("How can I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
    
        return "None"
    
    return query

def sendmail(to, content):
    server=smtplib.SMTP('smtp.gmail.con',587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","your password")
    server.sendmail("youremail@gmail.com",to, content)
    server.close()

def ss():
    img=pyautogui.screenshot()
    img.save("D:\Virtual Assistant\ss.png")

def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery=psutil.sensors_battery()
    speak("Battery percentage right now is" + battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    greet()

    while True:
        query=takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "quit" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="recieversemail@gmail.com"
                sendmail(to,content)
                speak("Email sent succesfully")
            except Exception as e:
                speak(e)
                speak("Mail not sent")
        elif "search in chrome" in query:
            speak("What should I search")
            chromepath="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1") 
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "play songs" in query:
            songs_dir="D:\Virtual Assistant\Music"  
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))     
        elif "remember that" in query:
            speak("what should I remember?")
            data=takeCommand()
            speak("you said me to remember" + data)
            rem=open("data.txt","w")
            rem.write(data)
            rem.close()
        elif "do you know anything" in query:
            rem=open("data.txt","r")
            speak("you said me to remember that" + rem.read())
        elif "screenshot" in query:
            ss()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif ("joke" or "jokes") in query:
            jokes()


