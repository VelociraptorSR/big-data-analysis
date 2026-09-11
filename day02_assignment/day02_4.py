'''
    Vowel & Consonant Frequency
    Write a program that prompts the user to enter a string and counts:

    The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
    The total count of all consonants.
    
    Sample Input: "Vinod Kumar Kayartaya"
    Sample Output:
    Vowel Frequencies:
    a: 4
    e: 0
    i: 1
    o: 1
    u: 1
    Total Consonants: 12
'''

import os


def checkVowel(string):
    return string.lower() in "aeiou"


def countVowel(string):
    vowel_count = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0
    }

    consonant_count = 0

    for char in string.lower():

        if char.isalpha():

            if checkVowel(char):
                vowel_count[char] += 1
            else:
                consonant_count += 1

    print("Vowel Frequencies:")

    for vowel, count in vowel_count.items():
        print(f"{vowel}: {count}")

    print("Total Consonants:", consonant_count)


def main():
    string = input("Enter a string: ")
    countVowel(string)


if __name__ == "__main__":
    os.system('cls')
    print("*" * 80)
    print(f"{' Vowel & Consonant Frequency ':^80}")
    print("-" * 80)
    main()