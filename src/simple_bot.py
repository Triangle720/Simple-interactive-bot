import speech_recognition as sr
from nltk_module import get_actions_with_args
from random import choice
from executor import Executor

class SimpleBot():
    def __init__(self):
        self.executor = Executor()
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
                print(f'bot > {self.execute(command)}')

    
    def read(self):
        command = input('> ')
        if command:
            print(f'bot > {self.execute(command.lower())}')

    def execute(self, command: str):
        actions = get_actions_with_args(command.lower())
        if actions:
            return self.executor.asign_functions_and_run(actions)
        else:
            return 'There is no actions.'
