N = 15
a, b = 0, 1
i = 0
while i < N:
    print(a, end=" ")
    a, b = b, a + b
    i += 1