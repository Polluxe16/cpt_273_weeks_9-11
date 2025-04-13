import speech_recognition as sr 
import datetime         #imports the necessary modules
import pyjokes
import webbrowser
import pyautogui

def listen_command():   #Enables the program to listen to audio input
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)  #Prints what the program heard
        print(f"You said {command}")
        return command
    except sr.UnknownValueError:           #Exception handling for UnknownValueError and RequestError
        print("Sorry, I didn't quite hear you.")
        return None
    except sr.RequestError:
        print("Sorry, I can't seem to be able to process the request")
        return None
        


def main():         #Main function that performs tasks based on words heard

    while True:

        command = listen_command()  

        #AssistantName = "Bob"          Code for making it respond when it's name is called; just left it out cuz it's kind of unnecessary for testing

        #if command and AssistantName in command:

        if "time" in command:       #Outputs the time if it hears the word "time"
            current_time = datetime.datetime.now().strftime("%H:%M")
            response = f"The current time is {current_time}."
            print(response)
        elif "joke" in command:    #Uses pyjokes to get and output a random joke
            joke = pyjokes.get_joke()
            print(joke)
        elif "cow" in command:   #Just thought I'd throw this in for fun
            print("MOOOOOOOOOOOOOOOOO")
        elif "open browser" in command:   #Opens a web browser to a really cool Youtube video
            print("Opening Browser.")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        elif "move" in command:    #Moves your mouse to the top left corner of your computer screen (0,0)
            pyautogui.moveTo(0,0)
            print("Your mouse has been moved to the top left of the screen")
        elif "find" in command:     #Prints the location of your mouse where it currently is
            print("Your mouse's location is", pyautogui.position())
        #elif "screenshot" in command:       Here's code to print a screenshot, but it kept getting errors when I tried to use it so I commented it
        #    pyautogui.screenshot("screenshot.png")
        #    print("There, I took a screenshot for you")
        elif "exit" in command:    #Closes the program
            print("See you later")
            break
        else:       #Handling for when it doesn't recognize any words for tasks
            print("Sorry, I can't respond to this request")
    
    
if __name__ == "__main__":      #Calls the main function
    main()
    
    