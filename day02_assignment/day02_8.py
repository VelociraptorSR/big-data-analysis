"""
Name Anonymizer
Write a program that prompts the user to enter a full name (first name, middle name, last name) and anonymizes it. 
The output should print the initials of the first and middle names followed by the full last name. 
If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"
"""


name = input("enter any name ")
name_list = name.title().split(" ")
print(name_list)
new_list = []
for i in range(0,len(name_list)-1):
    short_name = name_list[i][0]+"."
    new_list.append(short_name)
new_list.append(name_list[-1])
print(" ".join(new_list))