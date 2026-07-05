import argparse
from Internals.to_ascii import conv_ascii
import json

with open("Internals/chs.json", 'r', encoding="utf-8") as f:
    chs=json.load(f)
charsets = chs["charsets"][0]
blocks = charsets["blocks"]
ascii = charsets["ascii"]
braille = charsets["braille"]



modes = ["blocks", "braille", "ascii"]
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