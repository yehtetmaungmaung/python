# Given a dictionary in Python, write a Python program to find the sum of all items in the dictionary.

x = {"a": 100, "b": 200, "c": 300}
y = {"x": 25, "y": 18, "z": 45}

def sum(x):
    s = 0
    for v in x.values():
        s += v
    return s

print(sum(x))
print(sum(y))