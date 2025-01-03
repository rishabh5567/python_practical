import keyword
word = "if"
if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
