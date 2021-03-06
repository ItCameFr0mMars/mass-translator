from deep_translator import GoogleTranslator
import random as r
import os
import json
import time
from termcolor import colored, cprint
import requests
import pyperclip

def clear(): #clear screen funtion
    os.system("cls" if os.name == "nt" else "clear")
proxies = {
    "http": "5.202.191.226:8080" #only http and https
}
base_langs = [
    "af",
    "sq",
    "am",
    "ar",
    "hy",
    "az",
    "eu",
    "be",
    "bn",
    "bs",
    "bg",
    "ca",
    "ceb",
    "ny",
    "zh-CN",
    "zh-TW",
    "co",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "eo",
    "et",
    "tl",
    "fi",
    "fr",
    "fy",
    "gl",
    "ka",
    "de",
    "el",
    "gu",
    "ht",
    "ha",
    "haw",
    "iw",
    "hi",
    "hmn",
    "hu",
    "is",
    "ig",
    "id",
    "ga",
    "it",
    "ja",
    "jw",
    "kn",
    "kk",
    "km",
    "rw",
    "ko",
    "ku",
    "ky",
    "lo",
    "la",
    "lv",
    "lt",
    "lb",
    "mk",
    "mg",
    "ms",
    "ml",
    "mt",
    "mi",
    "mr",
    "mn",
    "my",
    "ne",
    "no",
    "or",
    "ps",
    "fa",
    "pl",
    "pt",
    "pa",
    "ro",
    "ru",
    "sm",
    "gd",
    "sr",
    "st",
    "sn",
    "sd",
    "si",
    "sk",
    "sl",
    "so",
    "es",
    "su",
    "sw",
    "sv",
    "tg",
    "ta",
    "tt",
    "te",
    "th",
    "tr",
    "tk",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "xh",
    "yi",
    "yo",
    "zu"]
color = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan'] #show colors on startup
r.shuffle(color)
for i in range(len(color)):
    clear()
    cprint(
"""
\r
\r
 /$$      /$$                                       /$$$$$$$$                                         /$$             /$$                        
| $$$    /$$$                                      |__  $$__/                                        | $$            | $$                        
| $$$$  /$$$$  /$$$$$$   /$$$$$$$  /$$$$$$$           | $$     /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$ $$/$$ $$ |____  $$ /$$_____/ /$$_____/           | $$    /$$__  $$ |____  $$| $$__  $$ /$$_____/| $$ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  $$$| $$  /$$$$$$$|  $$$$$$ |  $$$$$$            | $$   | $$  \__/  /$$$$$$$| $$  \ $$|  $$$$$$ | $$  /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$\  $ | $$ /$$__  $$ \____  $$ \____  $$           | $$   | $$       /$$__  $$| $$  | $$ \____  $$| $$ /$$__  $$  | $$ /$$| $$  | $$| $$      
| $$ \/  | $$|  $$$$$$$ /$$$$$$$/ /$$$$$$$/           | $$   | $$      |  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
|__/     |__/ \_______/|_______/ |_______/  /$$$$$$   |__/   |__/       \_______/|__/  |__/|_______/ |__/ \_______/   \___/   \______/ |__/      
                                        |______/                                                                                              
\r
\r
Made By ItCameFr0mMars
""", ""+color[i]+"")
    time.sleep(0.5)
    fincolor = color[i] #save the last used color for the theme
cprint("Type \"H\" for help, enter your command, or Press Enter to Continue", fincolor) 
menu = input("").upper()
if menu == "I":
    clear()
    cprint("""
This project was made by ItCameFr0mMars. If you have any questions, email me (mars@mars.tk), or DM me on discord (ItCameFr0mMars#6559). 
I would appreciate it if you star the repo, and any suggestions can be made on a github issue, or pull request.
""", fincolor)
    input("")
elif menu == "H":
    clear()
    cprint("""
H: Shows this.
I: Info screen
C: Create your own Language group
F: Load text from a file
""", fincolor)
    input("")
elif menu == "C":
    cprint("Warning, you must know the letter codes for each language, they can be found in the supported_languages.json file.", fincolor)
    print("\r")
    clear()
    with open("lang_groups.json") as fil: #open file and put the json into a python dict
        data = fil.read()
    check = json.loads(data)
    addedlangs = []
    while True:
        cprint("What language would you like to add? Type \"done\" when you are finished", fincolor)
        langcheck = input("")
        clear()
        proceed = True
        if langcheck == "done": #break the loop if user is done
            break
        if langcheck not in base_langs: #if the inputted lang is not in the supported list
            cprint("its not in the list bro.", fincolor) 
            time.sleep(1)
            clear()
            proceed = False
        if proceed == True and langcheck in addedlangs: #no dupelacates, MAYBE THIS COULD BE A FEATURE IN THE FUTURE
            cprint("Your language is already in the list", fincolor)
            time.sleep(1)
            clear()
            proceed = False
        addedlangs.append(langcheck) #append the added languages
    cprint("What description would you like to set for this Language Group?", fincolor) #set description          
    desc = input("")
    out_dict = {"lang_list": addedlangs, "desc": desc} #assemble the dict
    check["groups"].append(out_dict) #append to the dict
    fil = open("lang_groups.json", "w")
    json.dump(check, fil) #Convert the dict back into json and save to the file
    fil.close()
    clear()
    cprint("Successfully added your language group!", fincolor)
    exit()
elif menu == "F":
    cprint("What is the name of your text file?", fincolor)
    filename = input("")
    try: inputfile = open(filename, "r")
    except: cprint("Your filename is incorrect. Please make sure it is in the same directory as this main.py file.", fincolor), exit()
    start = inputfile.read()
    inputfile.close()


clear()
if menu == "F":
    cprint("Using text loaded from "+filename, fincolor)
    time.sleep(1)
else:    
    cprint("What string of ENGLISH text would you like to start with?", fincolor)
    start = input("")
    if start == "godsays": #get the text from funny website
        t = requests.get("https://godsays.xyz")
        start = t.text
clear()
cprint("How many iterations do you want?", fincolor)
iter = input("")
clear()
cprint("Would you like to see the english text as it is being translated? Warning: Slower. (y/N)", fincolor) #preview option
eng_updates = input("").upper()
clear()
langs = []
with open("lang_groups.json") as f: #load from text file
    data = f.read()
lang_groups = json.loads(data)
cprint("Would you like to use Language Groups? (y/N) ", fincolor) #language groups option
use_lang_groups = input("").upper()
clear()
if use_lang_groups == "Y":
    cprint("What Language Group? ", fincolor) 
    lang_group_number = input("")
    clear()
    cprint("Language Group "+lang_group_number+", Description: "+lang_groups["groups"][(int(lang_group_number)-1)]["desc"]+" (Y/n) ", fincolor) #confirm the group
    confirm_lang_group = input("").upper()
    clear()
    if not confirm_lang_group == "N":
        langs = lang_groups["groups"][int(lang_group_number)-1]["lang_list"] # use the langage group
else:
    langs = base_langs #if not, use the default language group
def text_refresh(text, lang, j): #refresh the text
    if eng_updates =="Y":
        eng = GoogleTranslator(source="auto", target="en", proxies=proxies).translate(text) #take the text to english
        clear() #clear, then print
        cprint("Language: "+lang.upper()+"       Iterations: "+str(j+1)+"/"+iter+"      Text: "+eng, fincolor)
    else:
        clear()
        cprint("Language: "+lang.upper()+"       Iterations: "+str(j+1)+"/"+iter+"      Text: "+text, fincolor)
initial =  GoogleTranslator(source="auto", target=r.choice(langs), proxies=proxies).translate(start) #initial text --> 1st translation
for i in range(int(iter)):
    randlang = r.choice(langs) #choose lang
    initial =  GoogleTranslator(source="auto", target=randlang, proxies=proxies).translate(initial) #do the translate
    text_refresh(initial, randlang, i) #refresh the text
final = GoogleTranslator(source="auto", target="en", proxies=proxies).translate(initial) #back to english
clear() 
cprint("Final Text: "+final, fincolor) #final output
try: pyperclip.copy(final)
except: pass