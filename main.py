import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
joy = pyttsx3.init()
#voices = joy.getProperty('voices')  #if need female voice
#joy.setProperty('voice', voices[1].id)


def talk(text):
    joy.say(text)
    joy.runAndWait()



def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'joy' in command:
                command = command.replace('joy', '')
    except:
        pass
    return command

def run_joy():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is')
        talk(time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk('I am in another relationship')
    elif 'made you' in command:
        talk('I made by developer Dhanonjoy Howlader')
    elif 'how are you' in command:
        talk('I am Fine! How can I help you')
    else:
        talk("I am going to search for you")
        pywhatkit.search(command)

while True:
    run_joy()