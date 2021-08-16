import speech_recognition as sr
#from gtts import gTTS
import os
def open_button(text):
    a=text.split("+")
    if "camera" in a or "Camera" in a:
        os.system("start microsoft.windows.camera:")
    elif "calculator" in a or "Calculator" in a:
        os.system("start calc")
    elif "chrome" in a or "Chrome" in a or "Google" in a or "google" in a:
        os.system("start chrome")
    else:
        os.system("start chrome https://www.google.com/search?q="+text[5::])
def search_button(text):
    os.system("start chrome https://www.google.com/search?q="+text[7::])
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Tell")
    audio=r.listen(source)
try:
    text=r.recognize_google(audio)
    text=text.replace(" ","+")
    if(text.split("+")[0]=="open"):
        open_button(text)
    elif text.split("+")[0]=="search":
        search_button(text)
    else:
        os.system("start chrome https://www.google.com/search?q="+text)
except:
    print("Dint recognize the voice")
