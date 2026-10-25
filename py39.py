# 39. Check valid identifier
import keyword
text = input("Enter a string: ")
if text.isidentifier() and not keyword.iskeyword(text):
    print("Valid identifier")
else:
    print("Invalid identifier")