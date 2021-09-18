import urllib.request
import requests
import math
import os
import time
import sys
import re

def Kalle():
    key="Kalle%20Hallden"
    kalle_channel = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + key)
    video_id = re.findall(r"watch\?v=(\S{11})", kalle_channel.read().decode())
    print("https://www.youtube.com/watch?v=" + video_id[0])
    time.sleep(5)

    menu()

def LTT():
    key="Linus%20Tech%20Tips"
    c = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + key)
    video_id = re.findall(r"watch\?v=(\S{11})", c.read().decode())
    print("https://www.youtube.com/watch?v=" + video_id[0])
    time.sleep(5)

    menu()

def Davie():
    key="Davie504"
    c = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + key)
    video_id = re.findall(r"watch\?v=(\S{11})", c.read().decode())
    print('https://www.youtube.com/watch?v=' + video_id[0])
    time.sleep(5)

    menu()

def menu():
    os.system('clear')
    print('-'*15 + 'Menu' + '-'*15)
    print('1 | Look at Kalle\'s new Video')
    print('2 | Look at LTT\'s new Video  ')
    print('3 | Look at Davie504\'s new Video')
    print('Q | Quit the Program          ')
    print('-'*19 + '-'*15)

    Opt = input('> ')
    if Opt == '1':
        Kalle()
    elif Opt == '2':
        LTT()
    elif Opt == '3':
        Davie()
    elif Opt == 'q':
        print('Exiting..')
        time.sleep(1.75)
        os.system('clear')
        exit()
    elif Opt == 'Q':
        print('Exiting..')
        time.sleep(1.75)
        os.system('clear')
        exit()
    else:
        print('Unknown Command')
        time.sleep(0.75)
        menu()
menu()
