# Caesar Cipher Project

We will write a python program that can encode and decode caesar ciphers. According to [Wikipedia](https://en.wikipedia.org/wiki/Caesar_cipher), the Caesar cipher “is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.”

We will have 3 files: `main.py`, `caesar.py`, and `test.py`. 

- `main.py` will be the file that we will run to interact with the caesar cipher program through a text interface. You will implement a text user interface here that lets the user encode, decode, and brute force messages as they please.
- `caesar.py` is the module where you implement the inner workings of the caesar cipher encode, decode, etc. functionality in the `caesar` class.
- `test.py` is where you will be writing and running your unit tests. Make sure to thoroughly test the functionality of your caesar cipher program to ensure that it behaves correctly and reacts to invalid inputs accordingly.

**The starter code is available on our class github repo.**

# Implementation

Here are the things that must be implemented. Feel free to whatever other variables and methods you feel is necessary for your implementation. Think about what is needed before you start writing the code, though! Use only what you need, or your code might become cluttered. Also, make sure to give your variables names that are easy to understand.

### `class caesar` (inside `caesar.py`)

- member variables
    - `_shift`  - the amount of characters we will be shifting
- methods
    - `__init__(self, shift_val=0)`
        - initializes a caesarCipher class instance, is an identity map by default (`_shift = 0`)
        - **input:** `int shift_val` (default =0)
        - **output:** void
    - `encode(self, plaintext)`
        - encodes input ciphertext
        - **input:** `string plaintext`
        - **output:** `string`
    - `decode(self, ciphertext)`
        - decodes input ciphertext
        - **input:** `string ciphertext`
        - **output:** `string`
    - `brute_force(self, ciphertext)`
        - allows for brute forcing by **printing** all 26 possible combinations of the input string.
        - **input:** `string ciphertext`
        - **output:** void
    - `set_shift(self, new_shift_val)`
        - updates the `self._shift` value to new values
        - **input:** `int new_shift_val`
        - **output:** void
    - `get_shift(self)`
        - returns the current _shift value.
        - **input:** void
        - **output:** `int`
    - `__repr__(self)`
        - when `print()` is called on this object, it prints a representative string that shows what this instance is.
        - **input:** void
        - **output:** `string` (in the form **“<caesarCipher object at 0x106caaee0, shift +3>”** where 0x106caaee0 is replaced by the actual memory location of object, and +3 with the actual shift number of this caesarCipher instance.)

### `function main()` (inside `main.py`)

- implement this function in however way you choose, but you must have a menu interface that looks like this (cool ASCII text is optional):

```
user@user-pc caesar % python3 main.py
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
    
1

-- Enter text to encode below --
The French are invading at midnight

-- Enter shift number --
3

-- Result --
Wkh Iuhqfk duh lqydglqj dw plgqljkw
```

- As is the case with our caesar class, you must account for erroneous user inputs in the user interface as well.

```
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
    
7

Input is invalid. Enter option again.

9

Input is invalid. Enter option again.

4
user@user-pc caesar %
```

# Testing

As we covered in class, please be thorough in your testing process. Test for as many cases as you can think of, especially edge cases (first element, last element, etc.) and base cases (empty data structures or single-element data structures, trivial cases, etc.)

Refer to the documentation for help on using the `unittest` module in python.

You are responsible for making sure your program works correctly!!

# Helpful Resources

Reference for data structures that might help with implementation
- [python enumerations](https://docs.python.org/3/library/enum.html?highlight=enum)
- [python dictionaries](https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionaries#dictionaries)

Misc references
- [python unittest module docs](https://docs.python.org/3/library/unittest.html)
