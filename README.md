# Simple interactive bot
Bot that executes your commands.
Project created for *"Natural Language Processing"* classes.


# Requirements

- SDK
-- Python 3.8.7
- Packages
-- nltk 3.5
-- SpeechRecognition 3.8.1

# How to run
1) Open cmd
2) cd "project_directory_full_path"
3) python `main.py` [FLAG]

- Flags:
  - **-k** or **-\-keyboard** (default) -> bot reads user input
  - **-v** or **-\-voice** -> bot listens user commands

Voice mode is slower because it sends requests to *Google Speech Recognition API*.
Additionally, commands must be pronounced loud and clear (but it's more useful and funnier).

# At first start

**Uncomment line #9 in main file** go to "All Packages" card and **download**:
- words
- punkt
- averaged_perceptron_tagger

After that, You can delete or comment line #9.

# How to use

After first run, bot will create file 'Softwares.txt' and directory 'Documents' with 'README.txt' file.
You will find some instructions there, but I'll give some examples here:

1) **Softwares.txt** should looks like this:
chrome|C:\Program Files\Google\Chrome\Application\chrome.exe
steam|C:\Program Files (x86)\Steam\Steam.exe
..
code|C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe
settings|%windir%\System32\Control.exe`

	etc. (**pattern:** one-part alias + '|' character +  full path to the executable)

2) **./Documents/** directory should contains:
one-part named files with any supported extension

If everything is done, bot is ready to work!

- Avaible commands:
  - **open, execute, run** -> run `software`
  - **open, show, read** -> open `document`
  - **open, show, go** -> open `url`
  - **update** -> read 'Software.txt' and update bot data
  -  more commands in near future :)
- Example commands:
  - Normal:
	 1) **open** `chrome`
	 2) **update**
	 3) **show** `myfile`
  - More '*realistic*':
	1) Could you **open** my favourite  `chrome` app?
	2) What's about **executing** `code` editor?
	3) You should **open** `settings` and **go** to website named: `stackoverflow.com`.

Have fun and feel free to modify!
