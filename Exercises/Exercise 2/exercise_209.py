from copy import copy

a = [1, 2, [10, 20]]

b = copy(a)
b[2][1] = 0

print("list a:", a)
print("list b:", b)
print("address of a:", id(a))
print("addrss of b", id(b))