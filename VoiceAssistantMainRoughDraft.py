#I included this basically to serve as a way to document my thought process and functions I tried. I had initially designed it to have different functions for each task, but
#I decided I didn't like that approach too much and each command wouldn't needed to be called multiple times anyways. I had also tried to implement tts here, but
#my computer kept receiving errors when I tried to use it, so it may end up working for you. Rather than let it go to waste, I stored it here.

import speech_recognition as sr 
import datetime
from gtts import gTTS
import winsound
import pyttsx3
from pydub import AudioSegment
import pyjokes
from threading import Timer

def listen_command():
    global command
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't quite hear you.")
        return None
    except sr.RequestError:
        print("Sorry, I can't seem to be able to process the request")
        return None
        
def speak(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)


def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    response = f"The current time is {current_time}."
    speak(response)


def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def set_timer(seconds):
    def timer_expired():
        speak("Time is up")
    Timer(seconds, timer_expired).start()

def cow():
    speak("MOOOOOOOOOOOOOOOOO")


def unknown_command():
    speak("Sorry, I can't respond to this request")

def main():

    while True:

        command = listen_command()

        AssistantName = "Bob"

        if command and AssistantName in command:
            if "time" in command:
                return tell_time()
            elif "joke" in command:
                return tell_joke()
            elif "timer" in command:
                return set_timer()
            elif "cow" in command:
                return cow()
            elif "Thanks for the help" in command:
                speak("You're welcome, see you later")
                break
            else:
                return unknown_command()
    
    
if __name__ == "__main__":
    main()
    
    
