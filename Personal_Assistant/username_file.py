from Voice_engine import speak
from Speech_recon import takeCommand

def username():
    print("What Should i call you?")
    speak("What Should i call you?")
    print("please wait till calibration is finished for response")
    speak("please wait till calibration is finished for response")
    uname = takeCommand()
    print("Welcome", uname)
    speak("Welcome")
    speak(uname)
    return uname







