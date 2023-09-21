# Zip: if one tuple contains more items, these items are ignored.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = zip(a, b)
y = list(x)

print(type(y))
print(y)