import os
import sys
from Internals.to_ascii import conv_ascii
import json
from colorim import Color

with open("Internals/chs.json", 'r', encoding="utf-8") as f:
    chs=json.load(f)
charsets = chs["charsets"][0]
blocks = charsets["blocks"]
ascii = charsets["ascii"]
braille = charsets["braille"]

banner = """                                                             
▄▄▄▄▄▄▄                  ▄▄            ▄▄▄▄▄▄▄▄▄          ▄▄ 
███▀▀███▄                ██            ▀▀▀███▀▀▀          ██ 
███▄▄███▀ ▄█▀█▄ ████▄ ▄████ ▄█▀█▄ ████▄   ███ ▄███▄ ▄███▄ ██ 
███▀▀██▄  ██▄█▀ ██ ██ ██ ██ ██▄█▀ ██ ▀▀   ███ ██ ██ ██ ██ ██ 
███  ▀███ ▀█▄▄▄ ██ ██ ▀████ ▀█▄▄▄ ██      ███ ▀███▀ ▀███▀ ██ 
                                                             
                                                             V 1.0"""

def show_banner():
    print(Color.blue(banner))

def cls():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def main_menu():
    cls()
    show_banner()
    print()
    print(Color.blue("[1]: Render Image in braille."))
    print()
    print(Color.blue("[2]: Render Image in ASCII."))
    print()
    print(Color.blue("[3]: Render Image in blocks."))
    print()
    print(Color.blue("[0]: Exit"))
    print()
    choice = int(input(Color.blue("> ")))
    if choice == 0:
        cls()
        sys.exit()
    elif choice == 1:
        cls()
        show_banner()
        print()
        path = input(Color.blue("Enter in your image's path: "))
        path.strip('"')
        cls()
        show_banner()
        print()
        conv_ascii(path, braille)
    
    elif choice == 2:
        cls()        
        show_banner()
        print()
        path = input(Color.blue("Enter in your image's path: "))
        path.strip('"')
        cls()
        show_banner()
        print()
        conv_ascii(path, ascii)

    elif choice == 3:
        cls()
        show_banner()
        print()
        path = input(Color.blue("Enter in your image's path: "))
        path.strip('"')
        cls()
        show_banner()
        print()
        conv_ascii(path, blocks)

main_menu()