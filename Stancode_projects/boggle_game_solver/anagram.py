"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        word = input('Find anagram for: ')
        start = time.time()
        if word == EXIT:
            break
        else:
            num_word = len(word)
            word_s = []
            word_s.append(word)
            word_s.append(num_word)
            read_dictionary(word_s)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(word_s):
    with open(FILE, 'r') as f:
        s = []
        for line in f:
            line = line.strip()
            num = len(line)
            if num == word_s[1]:
                s.append(line)
        find_anagrams(s, word_s)


def find_anagrams(s, word_s):
    """
    :param s:
    :return:
    """
    ans = []
    sub_s = '' # print 條件
    a = ''
    word_b = word_s[0]
    print('Searching...')
    for i in range(len(s)):
        check = s[i]
        check_lst = []
        for o in range(len(check)):
            check_lst.append(check[o])
        for n in range(len(check_lst)):
            if check_lst[n] in word_b:
                sub_s += check_lst[n]
                x = word_b.find(check_lst[n])
                a += word_b[:x]
                a += word_b[x + 1:]
                word_b = a
                a = ''
                if len(sub_s) == word_s[1]:
                    print('Found:' + str(check))
                    print('Searching...')
                    ans.append(check)
                    sub_s = ''
                    a = ''
                    word_b = word_s[0]
            else:
                sub_s = ''
                a = ''
                word_b = word_s[0]
                break
    print(str(len(ans)), 'anagrams: ', end="")
    print(ans)


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    pass


if __name__ == '__main__':
    main()
