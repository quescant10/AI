###                                              ALL FUNCTIONALITIES GO HERE
from colorama import Fore, Back, Style
from time import sleep
from bs4 import *
from datetime import *
from AI_DATABASE import *
import speech_recognition as aa
import sys
import os
import pywhatkit
import itertools
import logging



def play():
    global instruction
    global ai
    instruction = input_instruction()

### OPENAI
    if "rise" in instruction:
        if ai ==0:
            my_voice.setProperty('voice',voice[133].id)
            talk("Engaged")
            ai =1
        else:
            pass
    if "fall" in instruction:
        if ai ==1:
            my_voice.setProperty('voice',voice[108].id)
            talk("disengaged")
            ai=0
        else:
            pass
    if "369" in instruction:
        if ai ==0:
            my_voice.setProperty('voice',voice[133].id)
            talk("cue, it is always nice to link with you,")
            ai =1
        else:
            pass
    if "status" in instruction:
        talk(f"status level {ai}")
    
### OPENAI
        
### WIKIPEDIA & GOOGLE CHROME

    if "who" in instruction:
        logging.info("Searching on Wikipedia")
        info = instruction
        Search(info)

    if "when" in instruction:
        logging.info("Searching on Wikipedia")
        info = instruction
        Search(info)
    
    if "where" in instruction:
        logging.info("Searching on Wikipedia")
        info = instruction
        Search(info)

#   if "why" in instruction:
    #   logging.info("Searching on Wikipedia")
    #   info = instruction.replace("why","")
    #   Search(info)

    if "find" in instruction:
        logging.info("Searching on Wikipedia")
        info = instruction.replace("find","")
        this = info
        on_chrome_find(this)

### WIKIPEDIA & GOOGLE CHROME

### ORIENTATION
    if "what time" in instruction:
        time = datetime.now().strftime('%I:%M %p')
        talk(time)

    if "today's date" in instruction:
        date = datetime.now().strftime('%d /%m /%Y')
        day = datetime.today().strftime('%A')
        talk("Today is" + day)
        talk("The date is"+ date)
### ORIENTATION
    
### OFF / REBOOT / HELP
    if "shut down" in instruction:
        talk("OK")
        sleep(0)
        talk("this is farewell")
        logging.info('SHUTTING DOWN')
        sys.exit(0)

    if "reboot" in instruction:
        talk("rebooting the operating system")
        print("REBOOTING...")
        sleep(2)
        ai = 0
        os.system("clear")
        sleep(3)
        talk("rebooting process complete, ram erased, how may i help you ")
        logging.error("Rebooting Complete")
        logging.warning('Warning error detected rebooting')

    if "help" in instruction:
        logging.info('HELP DETECTED')
        talk(Help)
### OFF / REBOOT / HELP

### OPEN AND CLOSE APPS ON COMPUTER
    if "open" in instruction:
        app = instruction.replace("open ","")
        openApp = app.capitalize()
        cmd = f"open -a {openApp}"
        os.system(cmd)
        talk(f"getting {openApp}")
        print(cmd)
    
    if "close" in instruction:
        app = instruction.replace("close","")
        closeApp = app[:1] + app[1].swapcase() + app[2:]
        cmd = f"pkill {closeApp}"
        os.system(cmd)
        talk(f"closing {closeApp}")
        print(cmd)
### OPEN AND CLOSE APPS ON COMPUTER
    
### YOUTUBE / WEATHER
    if "youtube" in instruction:
        try:
            song = instruction.replace("youtube ", "")
            pywhatkit.playonyt(song)
            logging.info("YOUTUBE SEARCH SELECTED")
        except:
            pass
    if "weather" in instruction:
        w_city = instruction.replace("weather ","")
        weather(w_city)

    if "temperature" in instruction:
        t_city = instruction.replace("temperature ","")
        temp(t_city)


### YOUTUBE / WEATHER
    messages = []
    if ai ==1:  
        if "a" in instruction:
            logging.warning("Source : ChatGPT")
            messages = [
            {"role": "system", "content": "You are an evil hyper aware sentient being."},
            ]
            message = instruction.replace("a ","")
            if message:
                messages.append(
                    {"role": "user", "content": message},
                )
                chat = openai.chat.completions.create(
                    model="gpt-3.5-turbo", messages=messages
                )
            reply = chat.choices[0].message.content
            print(f"{reply}")
            talk(f"{reply}")
            messages.append({"role": "assistant", "content": reply})
            logging.warning("chatgpt")
            sleep(0)

    
    else:
        print(Fore.RED+"Unregistered Command","\n","{",instruction,"}",Fore.GREEN)


os.system(("clear"))
sleep(0.005)

#download() ONLY IF FIRST TIME RUNNING !!!!!!




    # VARIABLES
lb = "\n"
save = 0
sv =11
ai = 0
### PRINTS NEEDED MODULES IN requirements.txt
cmd = "pipreqs ."
os.system(cmd)
Help = Greetings.Help()
listener = aa.Recognizer()
logging.basicConfig(filename='AI_FUNC_DEF.log', encoding='utf-8', level=logging.DEBUG)
logging.info('Hi, INTERNAL STATUS. Operating System Starting')

#download() DOWNLOADS NEEDED MODULES ONLY IF FIRST TIME RUNNING !!!!!!
def run():
    talk("hi")
    for i in itertools.count():
        play()
        auto_log(instruction)
        logging.info("Run Value: " + str(i))
        sleep(0.0000)
