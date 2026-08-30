"""
Group Anagrams
Write a program that starts with a list of strings defined at the top of your script 
(e.g., words = ["eat", "tea", "tan", "ate", "nat", "bat"]) and groups the anagrams 
(words formed by rearranging letters) together. Print the final grouped list of lists.

Hardcoded Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
"""

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict = {}
for word in words:
    key = "".join(sorted(word))
    if key not in dict:
        dict[key] = []
    dict[key].append(word)
    
print(list(dict.values()))
     
    