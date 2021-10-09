import pyttsx3 as tts
import pywhatkit as kit
import datetime as dt
import wikipedia as wiki

from customFunction import *


def TakeCommand():
    engine =tts.init()
    voice = engine.getProperty("voices")
    engine.setProperty("voice",voice[1].id)
    speak(engine,"Namaste Sahab, Ram Ram")
    speak(engine,"Kya Karna hai Mujhe")

    flag=True

    while flag:
        command=speechListen(engine)
        try:
            if "bye"  in command:
                flag=False
            elif "search" in command:
                searchkey = command.replace('search',"")
                speak(engine,"Searching "+searchkey)
                kit.search(searchkey)
                flag=False
            elif "play" in command:
                song = command.replace('play',"")
                speak(engine,"Playing song "+song)
                kit.playonyt(song)
                flag=False
            elif "time" in command:
                time = dt.datetime.now().strftime('%I:%M:%S %p')
                speak(engine,"Abhi ka Waqt hai "+time)
                flag=False
            elif "who is" in command.lower():
                print("inside wiki")
                person=command.replace('who is', '')
                info=wiki.summary(person,5)
                print(info)
                speak(engine,info)
                flag=False
            else :
                speak(engine,"Dont Understand your command")
        except:
            speak(engine,"Microphone Not Working Properly")
            pass
        
     
    speak(engine,"Ja raha hun meine Sahab, Jai Ram Ji Ki")

