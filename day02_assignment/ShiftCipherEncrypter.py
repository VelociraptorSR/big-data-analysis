'''
    Shift Cipher Encrypter

    Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher.
    It should shift each alphabetical character in the string by the specified shift number down the alphabet.
    Maintain uppercase and lowercase characters, and leave spaces or punctuation marks unchanged.

    Sample Input:
    String = "Vinod"
    Shift = 3
    Sample Output:
    "Ylqrg"
'''

import os
def shiftCipherEncrypter(string, shift):
    result = ""
    for char in string:
        if char.isupper():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        elif char.islower():
            new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        else:
            result += char
    return result
def main():
    string = input("Enter a string: ")
    shift = int(input("Enter shift: "))
    result = shiftCipherEncrypter(string, shift)
    print("Encrypted Text:", result)
if __name__ == "__main__":
    os.system("cls")
    print("*" * 80)
    print(f"{' Shift Cipher Encrypter':^80}")
    print("-" * 80)
    main()