import speech_recognition as sr
import file_manager as fm
from random import choice


class SimpleBot():
    def __init__(self):
        self.softwares = fm.read_aliases_and_paths()

    def welcome(self):
        print('bot > Hi! I am here to make your life easier :)')
        print('bot > I am waiting for your commands')

    def listen(self):
        command = None
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('> ', end='')
            audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('\nbot > waiting...')
        except sr.RequestError:
            print('\nbot > Oh, my ears do not works.. Check your internet connection.')
        finally:
            if command:
                # execute
                print(command)

    
    def read(self):
        command = input('> ')
        if command:
            # execute
            print(command)
