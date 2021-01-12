#!/usr/bin/env python3
import sys
from simple_bot import SimpleBot

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
    bot.welcome()
    if mode:
        while 1:
            bot.listen()
    else:
        while 1:
            bot.read()

run()
