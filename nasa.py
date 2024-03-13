from urllib import request
import requests
import os
from PIL import Image
import pyttsx3

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty("voices",voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f":{audio}  ")
    print("  ")
    Assistant.runAndWait()

Api_key = "MqfYzo5T6a7eQ5R4ImUpT9Tr8ksThTT8YQbCDb17"

def NasaNews(Date):
    
    Speak("Extracting data from nasa !")
    
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)
    
    Params = {'date':str(Date)}
    
    r = requests.get(Url, params = Params)
    
    Data = r.json()
    
    Title = Data['title']
    
    Image_Url = Data['url']
    
    Info = Data['Explanation']
    
    Image_r = requests.get(Image_Url)
    
    FileName = str(Date) + '.jpg'
    
    with open(FileName,'wb') as f:
        
        f.write(Image_r.content)
        
    Path_1 = 'D:\\jarvis\\jarvisadvance\\' + str(FileName)
    
    Path_2 = "D:\\jarvis\\nasa database\\" + str(FileName)  
    
    os.rename(Path_1,Path_2)
    
    img = Image.open(Path_2)
    
    img.show()
    
    Speak(f'Title :{Title}')
    Speak(f'According to nasa : {Info}')
                