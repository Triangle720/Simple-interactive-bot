import speech_recognition as sr
import file_manager as fm
from nltk_module import get_actions_with_args
from random import choice


class SimpleBot():
    def __init__(self):
        fm.init_files_if_not_exist()
        self.softwares = fm.read_aliases_and_paths()
        self.welcome()

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
                print(command)
                print(f'bot > {self.try_to_execute(command)}')

    
    def read(self):
        command = input('> ')
        if command:
            print(f'bot > {self.try_to_execute(command)}')

    def try_to_execute(self, command: str):
        actions = get_actions_with_args(command)
        if actions:
            return 'there is at least one action'
        else:
            return 'there is no actions'
