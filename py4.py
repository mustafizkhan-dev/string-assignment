# 4. Count vowels
text = input("Enter a string: ")
count = 0
for ch in text.lower():
    if ch in "aeiou":
        count += 1
print(count)