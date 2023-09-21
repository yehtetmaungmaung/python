from copy import deepcopy

a = [1, 2, [1, 2]]
b = deepcopy(a)

b[2][1] = 100

print("list a:", a)
print("list b:", b)
print("address of a:", id(a))
print("addrss of b", id(b))