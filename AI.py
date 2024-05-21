import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki
import pyautogui

import json
import requests
import openai
import pywhatkit as kit
import smtplib as smt
import sample
import os


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYzVjZjdhY2MtMTQxMC00Mzk1LWEzMzgtMmE0N2FjZmY3NTAyIiwidHlwZSI6ImFwaV90b2tlbiJ9.309e55AhB4br8Fck4dlVbvqSfoax8bd6QZxG27gix0k"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hi! What do you want...",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Deepak"
}
x=pyttsx3.init()

def youtube(elem):
    kit.playonyt(elem)
def browse(ques):
    kit.search(ques)
def whatsapp(t,msg):
    kit.sendwhatmsg_instantly(t,msg)
def sendemail(to,msg):
    server=smt.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("deepujagana2002@gmail.com","danz ofvj xohn dxvl",)
    server.sendmail("deepujagana2002@gmail.com",to,msg)
    server.close()

def talk_To_Ai(query):
    payload["text"]=query
    #print(payload)
    response=requests.post(url,json=payload,headers=headers)
    #print(response.text)
    result=json.loads(response.text)
    speak(result['openai']['generated_text'])

def speak(audio):
    
    x.say(audio)
    x.runAndWait()
#speak("Good Evening")
def time():
    t=datetime.datetime.now().strftime("%H:%M:%S")
    #print(t)
    speak(t)
#time()
def date():
    y=datetime.datetime.now().year
    m=datetime.datetime.now().month
    d=datetime.datetime.now().day
    speak(d)
    speak(m)
    speak(y)
   # print(y,m,d)
#date()
def wish():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<=6:
        speak("Good afternoon sir")
    else:
        speak("Good night sir")
    speak("How can I help you sir")
#wish()
def inp():
    a = sr.Recognizer()
    with sr.Microphone() as source:
        print("Yes,I am Listening...")
        a.pause_threshold = 1
        a.adjust_for_ambient_noise(source)

        audio=a.listen(source)
        try:
            print("Recognizing...")
            query = a.recognize_google(audio,language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can You repeat it again...")
            inp()
            return "None"
        return query
#inp()

def screenshot():
    im1 = pyautogui.screenshot()
    im1.save("C:/Users/admin/Desktop/New folder/image.png")
if __name__ =="__main__":
    wish()
    while True:
        query = inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("I'm searching the topic...")
            query=query.replace("wikipedia","")
            result=wiki.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "screenshot" in query:
            speak("I am taking the screenshot...")
            screenshot()
        elif "exit" in query:
            speak("Exiting")
            print("Good Bye")
            exit()
        elif "open youtube" in query:
            speak("what you want to browse ?")
            elem=inp()
            speak("Opening youtube")
            youtube(elem)
        elif "open chrome" in query:
            speak("what do you want to search")
            ques=inp()
            speak("Browsing")
            browse(ques)
        elif "send in whatsapp" in query:
            try:
                speak("input receptent as text")
                t=input()
                speak("say what i want to send")
                msg=inp()
                whatsapp(t,msg)
            except Exception as e:
                print(e)
                speak("failed to send")
        elif "remember" in query:
            speak("what to be remembered")
            data=inp()
            speak("your input is"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()
        elif "speak out data" in query:
            remember=open('data.txt','r')
            speak("the  data i stored is"+remember.read())
        elif "send email" in query:
            try:
                speak("what you want to send")
                msg=inp()
                speak("enter receptient email")
                to=inp()
                sendemail(to,msg)
                speak("it is succcess")
            except Exception as e:
                print(e)
                speak("error")
        elif "play a song" in query:
            song_path=input("Enter the song path:")
            sample.play_song(song_path)
        elif "pause the song" in query:
            sample.control('pause')
        elif "unpause" in query:
            sample.control("unpause")
        elif "play" in query:
            try:
                sample.play_song(song_path)
            except:
                print("Please , say Play a song....")
        elif "stop" in query:
            sample.control("stop")
        elif "shutdown my pc" in query:
            os.system("shutdown /s /t 1")
        elif "restart my pc" in query:
            os.system("restart /r /t 1")
        else:
            talk_To_Ai(query)

