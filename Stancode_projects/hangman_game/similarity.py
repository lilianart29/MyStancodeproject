"""
File: similarity.py
Name:Lilian
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    find the similarity DNA strand
    """
    print("Please give me a DNA strand to search: ")
    a = input("")
    ans = code(a)
    print("What DNA sequence would you like to match: ")
    b = input("")
    match = match_number(b)
    print("The best match is " + c(match,ans))


def code(a):
    ans = ""
    for i in range(len(a)):
        ch = a[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


def match_number(b):
    match = ""
    for j in range(len(b)):
        ch = b[j]
        if ch.islower():
            match += ch.upper()
        else:
            match += ch
    return match


def c(match,ans):
    best = ""
    big = 0
    if match in ans:
        best = match
    else:
        for i in range(len(match)):
            k = 0
            ans_ = ans[i:i+len(match)]
            for j in range(len(match)):
                if match[j] == ans_[j]:
                    k = k+1
            if k > big:
                big = k
                best = ans_
    return best

#

###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
