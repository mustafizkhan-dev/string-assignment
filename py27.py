# 27. Check whether a word exists
sentence = input("Enter a sentence: ")
word = input("Enter a word: ")
if word in sentence.split():
    print("Word exists")
else:
    print("Word does not exist")