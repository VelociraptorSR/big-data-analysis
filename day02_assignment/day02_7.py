"""
Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring. 
Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2
"""


main_string = input("enter any string ")
sub_string = input("enter a substring ")
counter = 0
l = len(sub_string)
lm = len(main_string)
for i in range(0,lm):
    if main_string[i:l+i] == sub_string:
        counter += 1
print(f"{sub_string} = {counter}")