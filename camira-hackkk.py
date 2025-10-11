#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Compatible with Python2 and Python3 (menu & input)

import os
import sys

# Colors
b = "\033[0;34m"
g = "\033[1;32m"
w = "\033[1;37m"
r = "\033[1;31m"
y = "\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"

# For Python2/3 input compatibility
try:
    input_func = raw_input
except NameError:
    input_func = input

def show_menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Use .format() instead of f-strings
    print("{0}        ____ ".format(r))
    print("   _[]_/____\\__n_ ")
    print("  |_____.--.__()_|")
    print("  |I   //# \\\\    |")
    print("{0}  |P   \\\\__//    |".format(w))
    print("  |CS   '--'     | ")
    print("{0}  '--------------'----------{1}------------------.  ".format(r, w))
    print("{0}  | {1}Author  : {0}HVmbl3 {1}     | {0}INDO{2}{3}{1}N{1}ESIA         | ".format(r, w, ir, reset))
    print("{0}  | {1}Youtube : {1}Shodiq 2701 {1}| {2}+62-813-6487-3762 {1}|".format(r, w, lgray))
    print("{0}  '------------------------------------{1}-------'  ".format(r, w))
    print("  {0}[ 1 ] {1}Italy".format(r, w))
    print("  {0}[ 2 ] {1}Indonesia".format(r, w))
    print("  {0}[ 3 ] {1}Japan".format(r, w))
    print("  {0}[ 4 ] {1}United States".format(r, w))
    print("  {0}[ 5 ] {1}France".format(r, w))
    print("  {0}[ 6 ] {1}Korea".format(r, w))
    print("  {0}[ 7 ] {1}German".format(r, w))
    print("  {0}[ 8 ] {1}Turkey".format(r, w))
    print("  {0}[ 9 ] {1}Exit".format(r, w))
    print("")

def filtering(pilih):
    # dummy placeholders — replace with your actual functions or imports
    if pilih == 1:
        print("You chose Italy")
    elif pilih == 2:
        print("You chose Indonesia")
    elif pilih == 3:
        print("You chose Japan")
    elif pilih == 4:
        print("You chose United States")
    elif pilih == 5:
        print("You chose France")
    elif pilih == 6:
        print("You chose Korea")
    elif pilih == 7:
        print("You chose German")
    elif pilih == 8:
        print("You chose Turkey")
    elif pilih == 9:
        print(r + "Exiting ..." + w)
        sys.exit(0)
    else:
        print(r + "Invalid choice, exiting..." + w)
        sys.exit(1)

def main():
    while True:
        show_menu()
        user_input = input_func("[ Select@Number ]> ").strip()

        if user_input.startswith('+') or '-' in user_input:
            print("Note: Your input contains '+' or '-' — that looks like a phone number.")
            input_func("Press Enter to return to the menu...")
            continue

        try:
            choice = int(user_input)
        except Exception:
            print("Please enter a valid number (example: 2).")
            input_func("Press Enter to return to the menu...")
            continue

        filtering(choice)
        input_func("Action finished. Press Enter to return to the menu...")

if __name__ == '__main__':
    main()