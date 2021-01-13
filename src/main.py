#!/usr/bin/env python3
import sys
from nltk import download
from simple_bot import SimpleBot


# !!! IMPORTANT !!!
# Uncomment function 'download()' if you are running this program for the first time
# download()

FLAGS = {
    '-k' : 0,
    '--keyboard' : 0,
    '-v' : 1,
    '--voice' : 1
}

def run():
    if len(sys.argv) == 2:
        key = sys.argv[1]
        if key in FLAGS:
            main(FLAGS[key])
            return
    main(0)

def main(mode: int):
    bot = SimpleBot()
    if mode:
        while 1:
            bot.listen()
    else:
        while 1:
            bot.read()

run()
