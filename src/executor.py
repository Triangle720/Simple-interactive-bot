import file_manager as fm
from re import compile, match
from os import system
from enum import Enum

class Function(Enum):
    RUN_SOFTWARE = 1
    OPEN_DOCUMENT = 2
    OPEN_WEB_PAGE = 3
    UPDATE_SOFT_DATA = 4

FUNCTION_GROUPS = {
    ('open', 'execut', 'run') : Function.RUN_SOFTWARE,
    ('open', 'show', 'read') : Function.OPEN_DOCUMENT,
    ('open', 'show', 'go') : Function.OPEN_WEB_PAGE,
    ('update') : Function.UPDATE_SOFT_DATA
}

class Executor():
    def __init__(self):
        fm.init_files_if_not_exist()
        self.softwares = fm.read_aliases_and_paths()
        self.url_pattern = compile(r'[a-z0-9]+\.[a-z]{1,3}')

    def asign_functions_and_run(self, actions: list):
        argsAndFunctions = []
        temp = []
        for act in actions:
            for key in FUNCTION_GROUPS:
                if act[0] in key:
                    temp.append(FUNCTION_GROUPS[key])
            argsAndFunctions.append((act[1:], temp))    
            temp = []
        return self.try_if_runable(argsAndFunctions)

    def try_if_runable(self, argsAndFunctions: list):
        switch = {
            Function.RUN_SOFTWARE : self.execute_program,
            Function.OPEN_DOCUMENT : self.open_document,
            Function.OPEN_WEB_PAGE : self.open_web_page,
            Function.UPDATE_SOFT_DATA : self.update_bot_data
        }
        results = ''
        commandNum = 1
        isDone = False
        for item in argsAndFunctions:
            for function in item[1]:
                f = switch.get(function, False)
                if f(item[0]):
                    isDone = True
                    break
            if isDone:
                isDone = False
                results += f'Command {commandNum} executed, '
            else:
                results += f'Command {commandNum} failed, '
            commandNum += 1
        return f'{results[:-2]}.'

    def execute_program(self, args: list):
        print(f'bot > Trying to {Function.RUN_SOFTWARE.name} w/ arg: {args}: ', end='')
        for software in self.softwares:
            for arg in args:
                if arg == software[0]:
                    if fm.file_exist(software[1]): 
                        return self.cmd_start(software[1])
                    else:
                        print('FAILED - INCORRECT PATH')
                        return True
        return self.wrong_args()

    def open_document(self, args: list):
        print(f'bot > Trying to {Function.OPEN_DOCUMENT.name} w/ arg: {args}: ', end='')
        for arg in args:
            path = fm.find_file_path(arg)
            if path:
                return self.cmd_start(path)
        return self.wrong_args()


    def open_web_page(self, args: list):
        print(f'bot > Trying to {Function.OPEN_WEB_PAGE.name} w/ arg: {args}: ', end='')
        for arg in args:
            if self.is_url(arg):
                return self.cmd_start(f'https://{arg}')
        return self.wrong_args()

    def update_bot_data(self, args: list):
        print(f'bot > Trying to {Function.UPDATE_SOFT_DATA.name}: ', end='')
        newData = fm.read_aliases_and_paths()
        if newData:
            self.softwares = newData
            print('SUCCESS')
        else:
            print('FAILED - NO DATA TO READ')
        return True

    def is_url(self, arg: str):
        return match(self.url_pattern, arg)

    def cmd_start(self, path: str):
        system(f'start "" "{path}"')
        print('SUCCESS')
        return True

    def wrong_args(self):
        print('FAILED')
        return False
