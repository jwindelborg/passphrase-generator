#!/usr/bin/env python3


def main():
    while True:
        word = input("Word to add\n")
        word = word.lower().strip()
        
        if word == "q":
            break

        if word in open('word_list').read():
            print("Word already there")
        else:
            with open('word_list', 'a') as file:
                file.write('\n' + word)


if __name__ == "__main__":
    main()
