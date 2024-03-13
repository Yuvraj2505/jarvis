from cgitb import text
from distutils.cmd import Command
from re import search
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import keyboard
import pyjokes
import requests
import datetime
import pyaudio
from bs4 import BeautifulSoup
from playsound import playsound
from speedtest import *
from googletrans import Translator
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from nasa import NasaNews
from neuralnetwork import *
from brain import *

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty("voices",voices[1].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f":{audio}  ")
    print("  ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source,0,2)

        try:
            print("Recogninzing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f'you said : {query}')

        except:
            return "None"

        return query.lower()

query = takecommand()

#if 'hello' in query:
     #Speak('hello sir , i am jarvis how may i help you sir    !!')

#else:
   # Speak("no command found")   



    
def TaskExe():

    def Music():
        Speak("please remind me the name of song sir!!!!!")
        musicName = takecommand()

        if "amplifier" in musicName:
            os.startfile('E:\\download\\amplifier.mp3')
            
        else:
            pywhatkit.playonyt(musicName)
            Speak("your song sir!!!!!")            

    def OpenApps():
        Speak('ok sir,  wait a second')

        if 'code' in query:
            os.startfile("C:\\Users\\hp\\Desktop\\Visual Studio Code.lnk")
        
        elif "whatsapp" in query:
            os.startfile("C:\\Users\\hp\\Desktop\\WhatsApp Web.lnk")

        elif "chrome" in query:
            os.startfile("C:\\Program Files (x86)\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'instagram' in query:
            webbrowser.open("https://www.instagram.com/")

        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com/')    
         
        elif 'solid work' in query:
            os.startfile("C:\\Users\\Public\\Desktop\\SOLIDWORKS 2020.lnk")    

    def CloseApps():
        Speak('ok sir , wait a second')

        if 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")

        elif 'whatsapp' in query:
            os.system('TASKKILL /F /im WhatsApp.exe')

        elif 'code' in query:
            os.system('TASKKILL /F  /im Code.exe')

        elif "youtube" in query:
            os.system('TASKKILL /F  /im https://www.youtube.com/') 
            
        elif 'solid work' in query:
            os.system("TASKKILL /F  /im SOLIDWORKS 2020.lnk")                              

    def ChromeAuto():
        Speak('chrome automation started sir')

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'download' in command:
            keyboard.press_and_release('ctrl + j')        

    def screenshot():
        Speak('ok boss , what should i name that file  ?')
        path = takecommand()
        path1name = path + ".png"
        path1 = "D:\\jarvis\\screenshots by jarvis\\" + path1name
        kk = pyautogui.screenshot()
        kk.save(path1)
        os.startfile('D:\\jarvis\\screenshots by jarvis')
        Speak('here is your screenshot')

    def Temp():
        search = "Temperature in bhilai"
        url = f'https://www.google.com/search?q={search}'
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div", class_ = "BNeawe").text 
        Speak(f"the temperature of outside is {temperature} ")
      

    while True:

        query = takecommand()

        if 'hello' in query :
            Speak("hello sir i am jarvis how may i help youS ")

        elif 'how are you' in query:
            Speak("i am fine sir.")
            Speak("what about you ?")    

        elif 'you need a break jarvis'in query:
            Speak("ok sir , you can call me any time") 
            Speak("just say wake up jarvis")
            break
            
        elif 'kya hal hai' in query:
            Speak(" main badiya hoon sir ")

        elif 'youtube search' in query:
            Speak('ok sir, this what i found for you search!!')
            query = query.replace("jarvis",'')
            query = query.replace('youtube search','')
            web = 'https://www.youtube.com/results?search_query='  + query
            webbrowser.open(web)
            Speak('done sir')

        elif 'google search'  in query:
            Speak("this is what i found for your search sir!")
            query = query.replace('jarvis','')
            query = query.replace('google search','')
            pywhatkit.search(query)

        elif 'website' in query:
            Speak('ok sir  , Launching.....')
            query = query.replace("jarvis"," ")
            query = query.replace('website',"")
            query = query.replace('','')
            web1 = query.replace("open",'')
            web2 = "https://www." + web1 + ".com"
            webbrowser.open(web2)
            Speak("Launched sir!!!!" )

        elif 'launch' in query:
            Speak(" please tell me the name of the website! sir")
            name = takecommand()
            web = 'https://www.' + name +'.com'
            webbrowser.open(web)
            Speak("done sir!")

        elif 'music' in query:
            Music()    

        elif 'wikipedia' in query:
            Speak('searching wikipedia')
            query.replace("jarvis","")
            query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"according to wikipedia : {wiki}")

        elif 'screenshot' in query:
           screenshot()

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'open whatsapp' in query:
            OpenApps()

        elif 'open code' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'open youtube' in query:
            OpenApps()               
            
        elif 'open autocad' in query:
            OpenApps()  
            
        elif 'open solidworks' in query:
            OpenApps()          

        elif 'close chrome' in query:
            CloseApps()

        elif 'close code' in query:
            CloseApps()

        elif 'close whatsapp' in query:
            CloseApps()  

        elif 'close youtube' in query:
            CloseApps()
            
        elif 'close autocad' in query:
            CloseApps()
            
        elif 'close solidworks' in query:
            CloseApps()        
      
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')            

        elif "chrome automation" in query:
            ChromeAuto()

        elif 'repeat my words' in query:
            Speak('speak sir !')
            jj = takecommand()
            Speak(f' {jj}') 

        elif "alarm" in query:
            Speak("enter the time !")
            time = input("enter the time :")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    Speak("time to wakeup sir!!")
                    playsound('iron.mp3')
                    Speak("Alarm Closed!")

                elif now>time:
                    break

        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace('jarvis',"")
            query = query.replace('google search',"")
            query = query.replace('google',"")
            Speak("this is what i found for you sir!!")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                Speak(result)

            except:
                Speak('no speakable data available sir')    

        elif 'temperature' in query:
            Temp()
                   
        elif "space news" in query:
            
            Speak("tell me the date for the news extracting process")
            
            Date = takecommand()
            
            from feature import DateConverter
            
            Value = DateConverter(Date)
            
            from nasa import NasaNews
            
            NasaNews(Value)   
             
                          
TaskExe()                    

