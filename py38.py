# 38. Find shortest word
sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    print(min(words, key=len))
else:
    print("No words entered")
