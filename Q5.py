L = [1, 2, 3]
L[0] = 5
print("Changed list:", L)


T = (1, 2, 3)
LT = list(T)
LT[0] = 5
T = tuple(LT)
print("Changed tuple:", LT)
