def speak (audio):
    engine.say(audio)
    engine.runAndwait() #without this command, speech will not be audible to us.
    pass        #for now, we will write the conditions later.

import pyttsx3

engine = pyttsx3.init('sapi5')
voices= engine.getproperty('voices') #getting details of current voice
engine.setproperty('voice', voice [0].id)

if __name__"__main__" :
speak("code with Harry")

import datetime
def wishme():
    hour = int(datetime.datetime.now().hour)
    importspeechRecognition as sr 

def takecommand():
    #it takes microphone input from the user and retuns string output

    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in') #using google for voice recognition.
    print(f"user said: {query}\n") 