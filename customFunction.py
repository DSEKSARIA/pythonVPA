import speech_recognition as sr

def speechListen(engine):
    r =sr.Recognizer()
    with sr.Microphone() as source:
        #engine.say("Boliye Kya karna hai")
        engine.runAndWait()
        text = r.listen(source)
        try:
            recognised_text = r.recognize_google(text)
            print(recognised_text)
            #engine.say("You Said :-"+recognised_text)
            print("You Said :-"+recognised_text)
           # engine.runAndWait()
            return recognised_text
        except sr.UnknownValueError:
            print("EError Unknow Value")
            #engine.say("Error Unknow Value")
            #engine.runAndWait()
            pass
        except sr.RequestError as e:
            print("request error")
            #engine.say("request error")
            #engine.runAndWait()
            pass
        
    #engine.say("Command Received")
    #engine.runAndWait()


def speak(engine,q):
    engine.say(q)
    engine.runAndWait()