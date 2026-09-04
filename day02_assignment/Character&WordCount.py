"""
    Sentence Analysis (Character & Word Count)
    Write a Python program that prompts the user to enter a sentence. The program must count and display:

    The total number of characters (including spaces and punctuation).
    The total number of words.

    Sample Input: "Learning Python is fun!"
    Sample Output:
    Total Characters: 23
    Total Words: 4
"""


def wholeSentanceCharacterCount(sentance):
    return len(sentance)

def wordCount(sentance):
    words = sentance.split()
    return len(words)
    
def main():
    sentance = input("Enter a sentence: ")
    character_count = wholeSentanceCharacterCount(sentance)
    word_count = wordCount(sentance)
    print("Total Characters:", character_count)
    print("Total Words:", word_count)

if __name__ == "__main__":
    print("*" * 80)
    print(f"{' Sentence Analysis ':^80}")
    print("-" * 80)
    main()