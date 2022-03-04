from deep_translator import GoogleTranslator
import random as r
import os
proxies_example = {
    "http": "5.202.191.226:8080",
    "http": "140.246.224.68:8888",
    'http': "62.201.214.146:8080",
    "http": "88.255.102.98:8080"
}
start = input("What string of ENGLISH text would you like to start with? ")
iter = input("How many iterations do you want? ")
eng_updates = input("Would you like to see the english text as it is being translated? (y/N) ").upper()
langs = [
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'ny',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'en',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'ky',
    'lo',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'no',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu']
def text_refresh(text, lang, j):
    os.system('cls' if os.name == 'nt' else 'clear')
    if eng_updates =='Y':
        eng = GoogleTranslator(source='auto', target='en', proxies=proxies_example).translate(text)
        print("Language: "+lang.upper()+"       Iterations: "+str(j+1)+'/'+iter+"      Text: "+eng)
    else:
        print("Language: "+lang.upper()+"       Iterations: "+str(j+1)+'/'+iter+"      Text: "+text)
initial =  GoogleTranslator(source='auto', target=r.choice(langs), proxies=proxies_example).translate(start)
for i in range(int(iter)):
    randlang = r.choice(langs)
    initial =  GoogleTranslator(source='auto', target=randlang, proxies=proxies_example).translate(initial)
    text_refresh(initial, randlang, i)
final = GoogleTranslator(source='auto', target='en', proxies=proxies_example).translate(initial)
os.system('cls' if os.name == 'nt' else 'clear')
print("Final Text: "+final)