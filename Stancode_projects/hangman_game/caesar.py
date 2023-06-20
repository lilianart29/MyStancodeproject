"""
File: caesar.py
Name:lilian
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    TODO:
    """
    print("Secret number: ")
    a = int(input(""))
    print("What's the ciphered string? ")
    str = input("")
    biggers = bigger(str)
    print("The deciphered number is :" + new_alphabet(biggers,a))


def bigger(str):
    biggers = ""
    for j in range(len(str)):
        ch = str[j]
        if ch.islower():
            biggers += ch.upper()
        else:
            biggers += ch
    return biggers


def new_alphabet(biggers,a):
    ans = ""
    for char in biggers:
        for i in range(26):
            ch = ALPHABET[i]
            if char == ch:
                k = ALPHABET.find(char)
                if k+a < 26:
                    ans += ALPHABET[k+a]
                else:
                    ans += ALPHABET[k+a-26]
    return ans







#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
