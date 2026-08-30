"""
Longest Palindromic Substring
Write a program that prompts the user to enter a text string and finds the longest substring within 
it that reads the same forward and backward. If there are multiple palindromic substrings of 
the same maximum length, print any one of them.

Sample Input: "babad"
Sample Output: "bab" (or "aba")
Sample Input: "cbbd"
Sample Output: "bb"
"""
word = "babad"
curr_max = 0
sub = ""
for i in range(len(word)):
    for j in range(i+2,len(word)):
        sub_string = word[i:j]
        if sub_string[::-1] == sub_string and len(sub)>=curr_max:
            curr_max = len(sub_string)
            sub = sub_string
            
print(f'{sub} lengt is {curr_max}')
            
