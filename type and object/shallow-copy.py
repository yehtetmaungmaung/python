a = [1, 2, [3, 4]]

# shallow copy
b = list(a)
print(b is a)
b.append(100)
print(b)
print(a)

b[2][0] = 50
print(a)
print(b)