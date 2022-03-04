from deep_translator import GoogleTranslator
import random as r
import os
import json
proxies = {
    "http": "5.202.191.226:8080" #only http and https are supported rn. 
}
start = input("What string of ENGLISH text would you like to start with? ")
iter = input("How many iterations do you want? ")
eng_updates = input("Would you like to see the english text as it is being translated? (y/N) ").upper()
langs = []
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
    "te",
    "th",
    "tr",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "xh",
    "yi",
    "yo",
    "zh-CN",
    "zh-TW",
    "zu"]
with open("lang_groups.json") as f: #load from text file
    data = f.read()
lang_groups = json.loads(data)
use_lang_groups = input("Would you like to use Language Groups? (y/N) ").upper()
if use_lang_groups == "Y":
    lang_group_number = input("What Language Group? ")
    confirm_lang_group = input("Language Group "+lang_group_number+", Description: "+str(lang_groups[lang_group_number]["desc"])+" (Y/n) ").upper()
    if not confirm_lang_group == "N":
        langs = lang_groups[lang_group_number]["lang_list"] # use the langage group
else:
    langs = base_langs #if not, use the default language group
def text_refresh(text, lang, j): #refresh the text
    if eng_updates =="Y":
        eng = GoogleTranslator(source="auto", target="en", proxies=proxies).translate(text) #take the text to english
        os.system("cls" if os.name == "nt" else "clear") #clear, then print
        print("Language: "+lang.upper()+"       Iterations: "+str(j+1)+"/"+iter+"      Text: "+eng)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Language: "+lang.upper()+"       Iterations: "+str(j+1)+"/"+iter+"      Text: "+text)
initial =  GoogleTranslator(source="auto", target=r.choice(langs), proxies=proxies).translate(start) #initial text --> 1st translation
for i in range(int(iter)):
    randlang = r.choice(langs) #choose lang
    initial =  GoogleTranslator(source="auto", target=randlang, proxies=proxies).translate(initial) #do the translate
    text_refresh(initial, randlang, i) #refresh the text
final = GoogleTranslator(source="auto", target="en", proxies=proxies).translate(initial) #back to english
os.system("cls" if os.name == "nt" else "clear") 
print("Final Text: "+final) #final output