'''
    Custom Title Case Formatter
    Write a program that accepts a string input from the user and outputs it in Title Case
    (capitalizing the first letter of each word and lowercasing the remaining letters).
    Do not use Python's built-in .title() method.

    Sample Input: "WELCOME TO BANGALORE CITY"
    Sample Output: "Welcome To Bangalore City"
'''

import os


def customTitle(string):
    words = string.split()
    result = []

    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        result.append(new_word)

    return " ".join(result)


def main():
    string = input("Enter a string: ")

    result = customTitle(string)

    print("Title Case:", result)


if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Custom Title Case Formatter ':^80}")
    print("-" * 80)
    main()