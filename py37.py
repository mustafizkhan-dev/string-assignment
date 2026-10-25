# 37. Find longest word
sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    print(max(words, key=len))
else:
    print("No words entered")
