def change_list(lst):
    lst.append(100)

def change_string(ns):
    ns = ns + "!!!"

L = [1, 2, 3]
change_list(L)
print("List after function call:", L)

S = "hello"
change_string(S)
print("String after function call:", S)
