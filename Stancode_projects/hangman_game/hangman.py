"""
File: hangman.py
Name: lilian
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    guess word
    """
    st=random_word()
    N_TURNS = 7
    word = no_word(st)
    anss = word
    print('The word looks like:'+ word)
    while True:
        print('You have '+ str(N_TURNS) +' guesses left.')
        print('Your guess: ')
        a = input("")
        while not a.isalpha():
            print('illegal format.')
            print('Your guess: ')
            a = input("")
        while not len(a) ==1:
            print('illegal format.')
            print('Your guess: ')
            a = input("")
        ans = guess(a)
        anss = check_word(ans,st,anss)
        print('The word looks like:' + anss)
        if ans not in st:
            N_TURNS -=1
        if N_TURNS == 0:
            print('You are completely hung :(')
            print('The word is : '+st)
            break
        if anss == st :
            print('You win!!')
            print('The word was : ' + st)
            break


def guess(a):
    ans = ""
    for i in range(len(a)):
        ch = a[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


def no_word(st):
    word=""
    l=len(st)
    word = l * '_'
    return word


def check_word(ans,st,anss):
    if ans not in st:
        print("There is no "+ans+'\'s'+" in the word.")
    else:
        w = ""
        print("You are correct!")
        for j in range(len(st)):
            ch = st[j]
            if ans == ch:
                w += st[j]
            else:
                w += anss[j]
        anss = w
    return anss










def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
