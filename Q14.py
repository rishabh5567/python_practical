s = "hello"
reversed_s = ""
i = len(s) - 1
while i >= 0:
    reversed_s = reversed_s + s[i]
    i = i - 1
print("Reversed string:", reversed_s)
