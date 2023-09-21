# Join 2 tuples together

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
lst = list(x)

print(type(lst))
print(lst)