import os
import speech_recognition as sr



def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recogninzing.....")
            query = command.recognize_google(audio,language='en-in')
            print(f'you said : {query}')

        except:
            return "None"

        return query.lower()

while True:

    wake_Up = takecommand()
    if 'wake up jarvis' in wake_Up:
        os.startfile('"D:\\jarvis\\jarvisadvance\\jarvis.py"')        

    else:
        print("nothing......")    
