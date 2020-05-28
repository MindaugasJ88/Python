from collections import Counter

vowels = "aeiou"
def count_vowels(text):
    mylist = []
    for letter in text:
        if letter.lower() in vowels:
            mylist.append(letter.lower())
    return Counter(mylist)
