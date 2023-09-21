from copy import copy

a = [1, 2, 3]
b = copy(a)

b[2] = 12

print("list a:", a)
print("list b:", b)
print("address of a:", id(a))
print("addrss of b", id(b))