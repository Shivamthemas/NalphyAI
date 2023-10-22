
import speech_recognition as sr
import win32com.client

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
            print(f"User said: {query}")
            return (query)
        except Exception as e:
            return "some error, sorry master."




if __name__ == '__main__':
    print('Pycharm')
    say("what is your name")
    while True:
        print("listening...")
        text = takecommand()
        say(text)
