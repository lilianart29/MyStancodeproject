"""
File: my_power_function.py
Name:
-------------------------------
This program shows students how to
make their own functions by defining
def my_power(a, b)
"""


def main():
    print('give')
    s = input('')
    a = secrets(s)
    print("sum" + str(a) )


def secrets(s):
    ans = ''
    sum = 0
    for i in range(len(s)):
        for char in s:
            if char.isdigit():
                ans += char
            else:
                sum += int(ans)
                ans = ''
    return sum


    #####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()