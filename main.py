from math import trunc
from customFunction import *
from speechrecog import *
import pyttsx3 as tts

engine =tts.init()
while True:
    command=speechListen(engine)
    try:
        if "ramu" in command.lower():
            TakeCommand()
        elif 'bye' in command.lower():
            speak(engine,"Love you Baby")
            break
    except:
        pass
