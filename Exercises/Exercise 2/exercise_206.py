a = [1, 2, 3]

def func(list):
    list[2] = 11
    return list

b = func(a)

print("List a", a)
print("List b", b)