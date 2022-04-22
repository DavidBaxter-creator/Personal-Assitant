import datetime
from Voice_engine import speak
from username_file import username
from Speech_recon import takeCommand
def greetMe(uname):
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        print(f"Good Morning {uname}!")
        speak(f"Good Morning {uname}!")
        

    elif hour>=12 and hour<18:
        print(f"Good Afternoon {uname}!")
        speak(f"Good Afternoon {uname}!")
        

    else:
        print(f"Good Evening {uname}!")
        speak(f"Good Evening {uname}!")
        




