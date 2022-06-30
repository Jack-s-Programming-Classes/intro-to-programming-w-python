# main.py -- the wrapper / text ui for the caesarCipher class

import caesar as cc
import os

def ui(selection, runState):
    if selection == '1':
        print("\nEnter text to encode")
        plaintext = input()
        print("\nEnter shift number")
        shift = input()
        print("\nResult:\nWkh Iuhqfk duh lqydglqj dw plgqljkw")
        return True
    elif selection == '2':
        print("do decode")
        return True
    elif selection == '3':
        print("do brute")
        return True
    elif selection == '4':
        return False
    else:
        print("\nInput is invalid. Enter option again.\n")
        selection = input()
        return ui(selection, runState)


def main():
    mainMenu = """
                                               _         __                                    
  _____ ____ _ ___   _____ ____ _ _____ _____ (_)____   / /_   ___   _____        ____   __  __
 / ___// __ `// _ \ / ___// __ `// ___// ___// // __ \ / __ \ / _ \ / ___/       / __ \ / / / /
/ /__ / /_/ //  __/(__  )/ /_/ // /   / /__ / // /_/ // / / //  __// /     _    / /_/ // /_/ / 
\___/ \__,_/ \___//____/ \__,_//_/    \___//_// .___//_/ /_/ \___//_/     (_)  / .___/ \__, /  
                                             /_/                              /_/     /____/   

Welcome to my caesar cipher program! Enter a number to access the following menu items!

    1. encode message
    2. decode message
    3. brute force message
    4. exit
    """
    erroneousSelection = """

    """
    running = True
    while running:
        print(mainMenu)
        selection = input()
        running = ui(selection, running)

if __name__ == '__main__':
    main()