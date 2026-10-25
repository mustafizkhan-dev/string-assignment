# 25. Extract alphabets
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.isalpha():
        result += ch
print(result)