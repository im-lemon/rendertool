import argparse
from Internals.to_ascii import conv_ascii
import json
import os

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

with open("Internals/chs.json", 'r', encoding="utf-8") as f:
    chs=json.load(f)
charsets = chs["charsets"][0]
blocks = charsets["blocks"]
ascii = charsets["ascii"]
braille = charsets["braille"]
nf = charsets["nf"][0]

linux = nf["linux"]
oses = nf["oses"]
langs = nf["languages"]



modes = ["blocks", "braille", "ascii", "nf", "custom"]
parser = argparse.ArgumentParser()
parser.add_argument("--mode", "-m", help="The mode to cenvert the image.", required=True)
parser.add_argument("--path", "-p", help="The path to the image.", required=True)
args=parser.parse_args()

if not args.mode in modes:
    print(f"Mode: {args.mode} is not supported, see modes below.")
    print()
    for mode in modes:
        mode = str(mode)
        print(mode)
    print()
elif args.mode == "blocks":
    conv_ascii(args.path, blocks)
elif args.mode == "ascii":
    conv_ascii(args.path, ascii)
elif args.mode == "braille":
    conv_ascii(args.path, braille)
elif args.mode == "custom":
    chs = input("Type your charset here: ")
    cls()
    conv_ascii(args.path, chs)
elif args.mode == "nf":
    subsets = ["linux", "oses", "langs"]
    choice = input("Choose your subset: ")
    
    if not choice in subsets:
        print(f"Subset: {choice} is not supported. See supported subsets below.")
        print()
        for subset in subsets:
            subset = str(subset)
            print(subset)
        print()
    if choice == "linux":
        cls()
        conv_ascii(args.path, linux)
    elif choice == "oses":
        cls()
        conv_ascii(args.path, oses)
    elif choice == "langs":
        cls()
        conv_ascii(args.path, langs)
    