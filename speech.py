import speech_recognition as sr
import os
def func():
    try:
        r = sr.Recognizer()
        sample = sr.AudioFile('file.wav')
        
        with sample as source:
            r.adjust_for_ambient_noise(source)
            audio = r.record(source)
    

        a=r.recognize_google(audio)
        
        os.remove("file.wav")
        f=open('static/speech.doc','w+')
        f.write(a)
        f.close()
        print(a)
        return a
    except:
        return ("e")

