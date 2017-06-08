#!/usr/bin/env python3

import argparse
import random

current_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(current_dir)

seperators=['1','2','3','4','5','6','7','8','9','0','/','%','_','-','@','$','&','?','!','42','*','+','#', '=']

def parser():
    parser = argparse.ArgumentParser(description="Generate password")
    parser.add_argument("-c", "--count", dest="count", action="store", required=False, type=int, default=5, help="The amount of words")
    parser.add_argument("-s", "--seperator", dest="seperator", action="store_false", required=False, help="Turn off special seperator")
    parser.add_argument("-ca", "--capitalize", dest="capitalize", action="store_false", required=False, help="Turn off random capitalizing of words")
    return parser.parse_args()

def main():
    args = parser()
    passwd = ''
    for i in range(1, args.count + 1):

        if args.seperator:
            seperator = random.choice(seperators)
        else:
            seperator = ' '
        
        lines = open('word_list').read().splitlines()
        myline = random.choice(lines)

        if args.capitalize and random.choice([True, False]):
            myline = myline.capitalize()
        
        passwd += myline + seperator

    print(passwd.strip())


if __name__ == "__main__":
    main()