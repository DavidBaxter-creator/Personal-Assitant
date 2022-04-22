from Speech_recon import takeCommand
import requests
from Voice_engine import speak
from nlkt_run import query
from inital_greeting import greetMe
from username_file import username
from Weather_api import weatherinpit
from search_run import Search_up
from calculator_run import calculator
from NTLK_NER import NTLK_NER
import subprocess
import webbrowser
import json
import pyjokes
import time
# Replace all query with filtered_speech
# inital run Greetme, username, 



uname = username()
greetMe(uname)
print(f"Welcome to David's personal assistant {uname}") 
speak(f"Welcome to David's personal assistant {uname}")
while True:

    filtered_speech = query()
    print(filtered_speech)

# Working
    if 'question' in filtered_speech or 'what' in filtered_speech or 'why' in filtered_speech or 'who' in filtered_speech or 'when' in filtered_speech:  # question, What, why, who
        if 'question' in filtered_speech:
            Search_speech = ' '
            Search_speech = (Search_speech.join(filtered_speech))
            Search_speech = Search_speech.replace('question', ' ')
            print(Search_speech)
            Search_up(Search_speech)
        if 'what' in filtered_speech:
            Search_speech = ' '
            Search_speech = (Search_speech.join(filtered_speech))
            print(Search_speech)
            Search_up(Search_speech)
        if 'why' in filtered_speech:
            Search_speech = ' '
            Search_speech = (Search_speech.join(filtered_speech))
            print(Search_speech)
            Search_up(Search_speech)
        if 'who' in filtered_speech:
            Search_speech = ' '
            Search_speech = (Search_speech.join(filtered_speech))
            print(Search_speech)
            Search_up(Search_speech)
        if 'when' in filtered_speech:
            Search_speech = ' '
            Search_speech = (Search_speech.join(filtered_speech))
            print(Search_speech)
            Search_up(Search_speech)

# Working
    elif 'weather' in filtered_speech: 
        broken_speech = NTLK_NER(filtered_speech)
        weatherinpit(broken_speech) 

# Working
    elif 'search' in filtered_speech or 'play' in filtered_speech: 
        try:
            if 'search' in filtered_speech: 
                search_input = ' '
                search_input = (search_input.join(filtered_speech))
                search_input = search_input.replace('search', ' ')
                if 'for' in search_input:
                    search_input = search_input.replace('for', ' ')
                    print(search_input)
                    webbrowser.open(search_input)
                    pass
                else:
                    print(search_input)
                    webbrowser.open(search_input)
                    pass
            else: 
                search_input = ' '
                search_input = (search_input.join(filtered_speech))
                search_input = search_input.replace('play', ' ')
                print(search_input)
                webbrowser.open(search_input)
                pass
        except Exception:
            print("Error with webbroser cought")
            pass

# Working
    elif 'calculate' in filtered_speech:
        plain_speech = ' '
        plain_speech = (plain_speech.join(filtered_speech))
        print(plain_speech)
        calculator(plain_speech)

# Working
    elif True in[word in filtered_speech for word in ['open','google']]: 
        webbrowser.open("google.com")

# Working
    elif 'joke' in filtered_speech: 
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

# Working
    elif True in [word in filtered_speech for word in ['good', 'morning']]: 
        speak(f"Good Morning to you too {uname}")
        print(f"Good morning to you too {uname}")

    elif True in [word in filtered_speech for word in ['good', 'evening']]:
        speak(f"Good evening to you too {uname}")
        print(f"Good evening to you too {uname}")

    elif True in [word in filtered_speech for word in ['good', 'afternoon']]:
        speak(f"Good afternoon to you too {uname}")
        print(f"Good afternoon to you too {uname}")

    elif True in [word in filtered_speech for word in ['can','i','date', 'you']]:
        print(f"No i am sorry {uname}, i am simply a machine i dont know how that would work")
        speak(f"No i am sorry {uname}, i am simply a machine i dont know how that would work")
    
    elif True in [word in filtered_speech for word in ['do', 'you', 'love', 'me']]:
        print(f"I am not sure {uname}, but i hope so")
        speak(f"I am not sure {uname}, but i hope so")

# Working
    elif True in [word in filtered_speech for word in ['do', 'you', 'have', 'name']]:
        print("I don't have a name currently")
        speak("I don't have a name currently")
        print("Would you like to give me a new name?")
        speak("Would you like to give me a new name?")
        name_response = query()
        if 'yes' in name_response:
            print("What name would you like me to have for the time being?")
            speak("What name would you like me to have for the time being?")
            print("just say my new name by the way")
            speak("just say my new name by the way")
            name = query()
            usable_name = ' '
            usable_name = usable_name.join(name)
            print(f"{usable_name} is this the name you wish to give me?")
            speak(f"{usable_name} is this the name you wish to give me?")
            comfirm_name = query()
            if 'yes' in comfirm_name:
                print(f"Okay my new name is {usable_name}. Thank you very much {uname} for giving me a name")
                speak(f"Okay my new name is {usable_name}. Thank you very much {uname} for giving me a name")
                pass
            if 'no' in comfirm_name:
                print("what would you like to call me then?")
                speak("what would you like to call me then?")
                second_attemp_for_name = query()
                second_attemp_name = ' '
                second_attemp_name = second_attemp_name.join(second_attemp_for_name)
                print(f"is {second_attemp_name} the correct name this time{uname}")
                speak(f"is {second_attemp_name} the correct name this time{uname}")
                secound_confirm_name = query()
                if 'yes' in secound_confirm_name:
                    print(f"Thank you for deciding my name {second_attemp_name}, {uname}")
                    speak(f"Thank you for deciding my name {second_attemp_name}, {uname}")
                    pass
                if 'no' in secound_confirm_name:
                    print(f"I give up {uname} I dont want a name anymore")
                    speak(f"I give up {uname} I dont want a name anymore")
                    pass
        if 'no' in name_response:
            print("Okay then what's your next question?")
            speak("Okay then what's your next question?")
            pass

    elif True in [word in filtered_speech for word in ['what', 'can', 'you', 'do']]:
        speak("I can answer most questions, along with calculations, opening google and looking things in it for you.")
        speak("I can also tell jokes, shutdown your system, restart your system, and put your system into hibernation")

# Working
    elif True in [word in filtered_speech for word in ['stop', 'listening']]:
        try:
            print("How long would you like me to not listen for?")
            speak("How long would you like me to not listen for?")
            sleep_time = ' ' 
            sleep_time = int(sleep_time.join(query()))
            print(f"I will not listen for: {sleep_time} seconds")
            time.sleep(sleep_time)
        except TypeError:
            print("Opps there has been a problem with stop listning")
            pass

# Working
    elif 'thank' in filtered_speech and 'you' in filtered_speech: 
        print(f"No thank you {uname}")
        speak(f"No thank you {uname}")

# dont know
    elif True in [word in filtered_speech for word in ['system', 'restart']]:
        speak("Give me one second and i will restart your system")
        print("Restarting....")
        subprocess.call(["shutdown", "/r"])

# Dont know
    elif True in [word in filtered_speech for word in ['system', 'hibernate']]:
        speak("Give me one second and i will activate hibernation")
        print("hibernating....")
        subprocess.call("shutdown / h")

# Dont know
    elif True in [word in filtered_speech for word in ['system', 'shutdown']]:
        speak("Hold on one secound your system will shut down shortly")
        subprocess.call('shutdown / p /f')

# Working
    elif 'exit' in filtered_speech:  
        print(f"thanks for your time {uname}")
        speak(f"Thanks for your time {uname}")
        exit()

    
    


    


                 
        































