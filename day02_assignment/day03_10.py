"""
Run-Length String Compression
Write a program that prompts the user to enter a text string and compresses it using run-length encoding 
(listing character counts next to each repeated character). 
If the compressed string is not smaller in size than the original string, print the original string.

Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
Sample Input: "abcd"
Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")
"""
string = "aabcccccaaa"
count = 1
new_str = ""
for i in range(1,len(string)):
    if string[i] == string[i-1]:
        count += 1
    else:
        new_str = new_str + string[i-1] + str(count)
        count = 1

new_str = new_str + string[-1] + str(count)
print(new_str)