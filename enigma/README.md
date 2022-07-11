# Enigma Project

## Helpful resources
* [Cipher Machines and Cryptology](https://www.ciphermachinesandcryptology.com/)
* [Enigma article on Matematik Sider](https://www.matematiksider.dk/enigma_eng.html)
* [YouTube video by Jared Owen - "How did the Enigma Machine work?"](https://www.youtube.com/watch?v=ybkkiGtJmkM&ab_channel=JaredOwen)
* [Cryptography StackExchange - "Enigma ring settings - is the relative location of the turnover all that matters?"](https://crypto.stackexchange.com/questions/86371/enigma-ring-settings-is-the-relative-location-of-the-turnover-all-that-matters)
* [Cryptography StackExchange - "Why does the Bombe not consider the Ringstellung when determining stecker pairs?"](https://crypto.stackexchange.com/questions/81319/why-does-the-bombe-not-consider-the-ringstellung-when-determining-stecker-pairs)

## Miscellaneous

### using json files in python
the json file for the rotor settings can be found on this repository. Here's the piece of code you can use to bring that json file into your python code as a python dictionary. (keep the json file in the same directory as the other files)
```python
import json

# load file into variable
with open("wirings.json", "r") as s:
    wirings = json.load(s)

# variable is a dictionary, so use like you would a normal python dictionary
alphabet = wirings['alphabet']

```
