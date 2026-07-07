import os
import sys
from Internals.to_ascii import conv_ascii
import json
from colorim import Color
from time import sleep

with open("Internals/chs.json", 'r', encoding="utf-8") as f:
    chs=json.load(f)
charsets = chs["charsets"][0]
blocks = charsets["blocks"]
ascii = charsets["ascii"]
braille = charsets["braille"]
nf = charsets["nf"][0]

linux = nf["linux"]
oses = nf["oses"]
langs = nf["langs"]

banner = """                                                             
▄▄▄▄▄▄▄                  ▄▄            ▄▄▄▄▄▄▄▄▄          ▄▄ 
███▀▀███▄                ██            ▀▀▀███▀▀▀          ██ 
███▄▄███▀ ▄█▀█▄ ████▄ ▄████ ▄█▀█▄ ████▄   ███ ▄███▄ ▄███▄ ██ 
███▀▀██▄  ██▄█▀ ██ ██ ██ ██ ██▄█▀ ██ ▀▀   ███ ██ ██ ██ ██ ██ 
███  ▀███ ▀█▄▄▄ ██ ██ ▀████ ▀█▄▄▄ ██      ███ ▀███▀ ▀███▀ ██ 
                                                             
                                                             V 2.0"""

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
    print(Color.blue("[4]: Render Image using Nerd Font glyphs."))
    print()
    print(Color.blue("[5]: Render Image with custom charset."))
    print()
    print(Color.blue("[0]: Exit"))
    print()
    choice = int(input(Color.blue("> ")))
    
    def get_choice(mode):
        cls()
        show_banner()
        path = input(Color.blue("Enter in your image's path: "))
        path=path.strip('"')
        cls()
        conv_ascii(path, mode)

    if choice == 0:
        cls()
        sys.exit()
    elif choice == 1:
        get_choice(braille)

    elif choice == 2:
        get_choice(ascii)

    elif choice == 3:
        get_choice(blocks)

    elif choice == 4:
        def get_choice_nf():
            cls()
            show_banner()
            print()
            print(Color.blue("[1]: Linux distros."))
            print()
            print(Color.blue("[2]: Operating systems."))
            print()
            print(Color.blue("[3]: Programming languages."))
            print()
            choice = int(input(Color.blue("> ")))
            cls()
            show_banner()
            path = input(Color.blue("Enter your image's path: "))
            path=path.strip('"')
            if choice == 1:
                cls()
                conv_ascii(path, linux)
            elif choice == 2:
                cls()
                conv_ascii(path, oses)
            elif choice == 3:
                cls()
                conv_ascii(path, langs)
            elif choice == "exit":
                cls()
                show_banner()
                sys.exit()
            else:
                cls()
                print(Color.red("Choice not supported, taking you back to the main menu!"))
                sleep(0.5)
                get_choice_nf()
        get_choice_nf()
    
    elif choice == 5:
        cls()
        show_banner()
        print()
        chs = input(Color.blue("Type your charset > "))
        path = input(Color.blue("Enter your image's path: "))
        cls()
        show_banner()
        print()
        path=path.strip('"')
        conv_ascii(path, chs)
            
    else:
        cls()
        print(Color.red("Choice not supported, taking you back to the main menu!"))
        sleep(0.5)
        cls()
        main_menu()

main_menu()