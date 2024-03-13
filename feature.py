import pywhatkit
import wikipedia
from pywikihow import WikiHow , search_wikihow
import os
import webbrowser as web
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voices",voices[0].id)
engine.setProperty('rate',170)

def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f":{audio}  ")
    print("  ")
    engine.runAndWait()
  
def DateConverter(query):
    
    Date = query.replace("and", "-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")
    return str(Date)
       