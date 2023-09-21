# List: Shallow copy

a = [1, 2, 3]
b = a

print("list a", a)
print("list b", b)

b[2] = 5

print("list a", a)
print("list b", b)