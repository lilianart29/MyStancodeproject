"""
File: complement.py
Name:lilian
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
   find the complement
    """
    print("Please give me a DNA strand and I'll find the complement: ")
    str = input("")
    ans = build_complement(str)
    print("The complement of "+ build_complement(str) + " is " + reverse_complement(ans))


def build_complement(str):
    ans = ""
    for i in range(len(str)):
        ch = str[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


def reverse_complement(ans):
    code = ""
    for i in range(len(ans)):
        ch = ans[i]
        if ch == 'A':
            code += 'T'
        else:
            if ch == 'T':
                code += 'A'
            else:
                if ch == 'C':
                    code += 'G'
                else:
                    code += 'C'
    return code



###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
