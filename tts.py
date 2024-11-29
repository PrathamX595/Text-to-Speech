from gtts import gTTS
import os

mytext = open("speak.txt").read()
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False, tld='co.in')
myobj.save("talking.mp3")
os.system("start talking.mp3")