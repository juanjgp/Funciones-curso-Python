import re
import pyttsx3
import speech_recognition as sr
from speak_and_listen import speak, hear_me


def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            pass
    return name

def main():
    speak("Hola, Cómo te llamas")

    text = hear_me
    name = identify_name(text)
    if name:
        speak("Encantado de conocerte, {}".format(name))
    else:
        speak(("Pues mire, la verdad es que no te entiendo, puedes quitarte la patata de la boca?"))

if __name__ == "__main__":
    main()
