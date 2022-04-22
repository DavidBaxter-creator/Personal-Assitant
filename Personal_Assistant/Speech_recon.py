import speech_recognition as sr 
from speech_recognition import Recognizer

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("silence please, calibrating background noise")
        r.adjust_for_ambient_noise(source, duration=2)
        print("Calibrating, now speak....")
        audio = r.listen(source)
    try: 
        user_response = format(r.recognize_google(audio))
        print("\033[91m {}\033[00m" .format("YOU SAID : "+user_response))
        return user_response
    except sr.UnknownValueError:
        print("Oops Didn't catch that")
        exit()



