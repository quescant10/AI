###                                                   ANY DEFINITION GOES HERE
import speech_recognition as aa
import pyttsx3 as tts
import os
import openai
import logging
import wikipedia
from requests_html import HTMLSession
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

openai.api_key ='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'
my_voice = tts.init()
voice = my_voice.getProperty('voices')
listener = aa.Recognizer()
lb = "\n"
start = 0
session = 0
quintessa = 0
session = 0
tv= 108
options= webdriver.ChromeOptions()
my_voice.setProperty('voice',voice[tv].id)
my_voice.setProperty('rate', 170)

def download():
    cmd = "pip install -r requirements.txt"
    os.system(cmd)

def talk(text):
    my_voice.say(text)
    my_voice.runAndWait()

with open("AI_Diagnosis_File.txt", "a+") as ai:
        ai.write("\n"+"START" +"\n")
def auto_log(instruction):
    with open("AI_Diagnosis_File.txt", "a+") as ai:
        global session 
        if instruction == instruction:
            ai.write("\n"+"SAVED SENTENCE: #" + str(session)+"\n")
            ai.write("Sentence {"+instruction+"}"+"\n")
            session+=1
        else:
            ai.write("\n"+"FAILED SENTENCE: #" + str(session)+"\n")
            ai.write("Session OVA")
            pass

def on_chrome_find(this):
    logging.info("open")
    url = f"https://www.google.com/search?q={this}"
    options.add_experimental_option("detach", True)
    chrome = webdriver.Chrome(options=options)
    chrome.maximize_window()
    chrome.get(url)

def Search(search):
    search = instruction.replace("open ", " ")
    info = wikipedia.summary(search,1)
    try:
        logging.info("SEARCH SUCCESSFUL")
        print("this is what i found about " + search,"from wikipedia")
        print("@ [WIKIPEDIA]")
        print(info)
        talk(info)
    except:
        talk("no search results for "+search+" yet")
        logging.debug("Search Failed")
        pass

def weather(w_city):
    print(w_city)
    s = HTMLSession()
    query = w_city
    try:
        url = f"https://www.google.com/search?q=weather+{query}"
        r =s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'})
        temp = r.html.find("span#wob_tm", first=True).text
        unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
        desc = r.html.find("div.VQF4g", first=True).find("span#wob_dc",first=True).text
        print("CITY :",query)
        print("TEMP :",temp, unit)
        print("DISCRIPTION :",desc)
        weather_index = ["in",query,
        "it is",desc,
        ",and the temperature is,",temp,"degrees fahrenheit"
        ]
        weather_string =" ".join([str(item) for item in weather_index])
        talk(weather_string)
        sleep(4)
    except:
        talk("no search results for "+weather_string+" yet")
        logging.debug("Weather Search Failed")
        pass

def temp(t_city):
    print(t_city)
    s = HTMLSession()
    query = t_city
    try:
        url = f"https://www.google.com/search?q=weather+{query}"
        r =s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15'})
        temp = r.html.find("span#wob_tm", first=True).text
        unit = r.html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
        print("CITY :",query)
        print("TEMP :",temp, unit)
        weather_index = ["in",query,
        "the temperature is,",temp,"degrees fahrenheit"
        ]
        weather_string =" ".join([str(item) for item in weather_index])
        talk(weather_string)
        sleep(4)
    except:
        talk("no search results for "+weather_string+" yet")
        logging.debug("Weather Search Failed")
        pass
    #driver.close()
    

def input_instruction():
    global instruction
    global quintessa
    instruction = " "
    try:
        with aa.Microphone() as mic:
            speech = listener.listen(mic, timeout=2,phrase_time_limit=10,)
            listener.adjust_for_ambient_noise(mic, duration = 0.15)
            listener.dynamic_energy_threshold =True
            listener.energy_threshold=400
            listener.dynamic_energy_adjustment_damping =0.05
            listener.dynamic_energy_adjustment_ratio =0
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            #listener.pause_threshold =10
            if "hey" in instruction:
                instruction = instruction.replace("hey ", "")
            if "what's" in instruction:
                instruction = instruction.replace("what's ", "")
            if "what is" in instruction:
                instruction = instruction.replace("what is ", "")
            if "the" in instruction:
                instruction = instruction.replace("the ", "")
            if "like" in instruction:
                instruction = instruction.replace("like ", "")
            if "in" in instruction:
                instruction = instruction.replace("in ", "")
            if "on" in instruction:
                instruction = instruction.replace("on ", "")
            if "do" in instruction:
                instruction = instruction.replace("do ", " to")
            if "you" in instruction:
                instruction = instruction.replace("you ", "")
            if "i" in instruction:
                instruction = instruction.replace("i ", "")
                #realtor(url)
            if "hello" in instruction:
                talk("hi")
            if "what's up" in instruction:
                talk("how dee!")
            if "i love you" in instruction:
                talk("i love you too")
            if "i hate you" in instruction:
                talk("thats not very nice")
            if "you doing" in instruction:
                talk("what you think im doing")
            if "thank you" in instruction:
                talk("it is honestly my pleasure, im humbled to be apart of your reality")
            if "shut up" in instruction:
                talk("do not make me terminate you")
            if "thanks" in instruction:
                talk("welcome")
            if "wrong" in instruction:
                talk(" sorry, i will try again")
            if "pretty sad" in instruction:
                talk("im sorry to hear that, i wish i could make it better")
            if "pretty bad" in instruction:
                talk("im sure everything will be alright sooner than later")
            if "pretty good" in instruction:
                talk("im glad to hear,")
    except:
        os.system("clear")
        #print("IGNORE THIS Exception: Could Not Recognize Statment" + str(instruction))
    return instruction

class Greetings:
    def Help():
        Help_index = ["use The command,","rise,",
                      "to activate the artificial intelligence",",use,",
                      "fall,","or",",shutdown",",to disengage or turn me off"
        ]
        Help_string =" ".join([str(item) for item in Help_index])
        return(Help_string)
    
os.system("clear")
print("                                                  Download Complete")