import os


docDir = 'Documents'
softFile = 'Softwares.txt'
 
def init_files_if_not_exist():
    create_soft_file()
    create_docs_directory()

def read_aliases_and_paths():
    result = []
    if file_exist(softFile):
        with open(softFile, 'r', encoding='UTF-8') as f:
            for line in f:
                if line[0] != '#' and '|' in line:
                    temp = line.rstrip('\n').split('|')
                    if len(temp) == 2:
                        result.append(temp)
    return result

def find_file_path(fileName: str):
    if directory_exist(docDir):
        for file in os.listdir(docDir):
            if fileName == file[:file.index('.')].lower():
                return os.path.join(docDir, file)
    return None

def create_soft_file():
    if not file_exist(softFile):
        with open('Softwares.txt', 'w', encoding='UTF-8') as f:
            f.write('# Add your aliases and paths to your programs here so I know what you want to run.\n')
            f.write('# ----------\n')
            f.write('# Example:\n')
            f.write('# 1) my_fav_program|' + os.path.abspath('main.py') + '\n')
            f.write('# 2) If you want to open defined software just tell me something like:\n')
            f.write('#  - Hey! It\'s time to open my_fav_program!\n')
            f.write('# ----------\n')
            f.write('# Remember to separate alias and path with \'|\' character!\n')
            f.write('# Alias can not contain whitespaces and don\'t use \'#\' at start of the line\n')
            f.write('# You can delete tutorial above :)\n')
            f.write('# alias | path\n')

def create_docs_directory():
    if not directory_exist(docDir):
        os.makedirs(docDir)
    filePath = os.path.join(docDir, 'README.txt')   
    if not file_exist(filePath):
        with open(filePath, 'w', encoding='UTF-8') as f:
            f.write('# Store your documents, photos, etc. in this directory\n')
            f.write('# If you tell me the appropriate command and name of file, I will open it :)\n')

def file_exist(filePath: str):
    return os.path.isfile(filePath)
    
def directory_exist(directoryPath: str):
    return os.path.isdir(directoryPath)
