'''
    Reversed Uppercased String
    Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

    Sample Input: "Bangalore"
    Sample Output: "EROLAGNAB"
'''
import os

def reverseString(word):
    return word[::-1]

def main():
    sentance = input("Enter a sentence: ")
    reversed = reverseString(sentance).upper()
    print(f"Result :  {reversed}" )

if __name__ == "__main__":
    os.system('cls')
    print("*" * 80)
    print(f"{' Reversed Uppercased String ':^80}")
    print("-" * 80)
    main()