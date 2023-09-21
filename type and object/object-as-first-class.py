import math

items = {
    'number': 42,
    'text': "Hello World"
}

print(type(items))

items["func"] = abs

items["mod"] = math

items["error"] = ValueError

nums = [1, 2, 3, 4]
items["append"] = nums.append

print(items["func"](-45))

print(items["mod"].sqrt(4))

items["append"](100)
print(nums)

try:
    x = int("a lot")
except items["error"] as e:
    print("Couldn't convert!!! ",e)