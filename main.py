import os

import speech_recognition as sr
import win32com.client
import webbrowser
import datetime
import openai
from config import apikey
import random

def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.speak(text)


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"You Asked: {query}")
            return (query)
        except Exception as e:
            return "some error, sorry master."

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Harry: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/prompt- {random.radint(1,23433343434343)}", "w") as f:
        f.write(text)

if __name__ == '__main__':
    print(" HOW TO WAHT ISN THIS".lower())
    print("I am ready to serve")
    say("Hello Master")
    while True:
        print("listening...")
        query = takecommand()
        sites = [["youtube", "https://www.youtube.com"], ["Google", "https://www.google.com"],
                 ["wikipedia", "https://www.wikipedia.com"]]
        for site in sites:

            if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
            if "the time" in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir the time is {strfTime} ")
            if "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

