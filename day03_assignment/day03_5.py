'''
The Spy's Word Reverser
Scenario: A secret agent wants to send an encrypted message. The encryption rule is simple: 
reverse every word in the sentence, but keep the order of words unchanged. 
Write a program that prompts the user for a sentence, splits it, uses a list comprehension to reverse the 
letters of each word, and joins them back together.

Sample Input: "Meet me at midnight"
Sample Output: "teeM em ta thgindim"
'''
sent = "Meet me at midnight"
list_1 = sent.split(" ")
list_2 = []
for i in range(len(list_1)):
    list_1[i] = list_1[i][::-1]
    
print(" ".join(list_1))
    