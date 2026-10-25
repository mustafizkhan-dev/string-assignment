# 24. Extract digits
text = input("Enter a string: ")
result = ""
for ch in text:
    if ch.isdigit():
        result += ch
print(result)
