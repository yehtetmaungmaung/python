# Write down the python code that accept name and mark of five students.
# And then output the highest mark holder and lowest mark holder of these five students.

names = []
marks = []

for i in range(5):
    name = input(f"Enter the name of student {i+1} ")
    mark = float(input(f"Enter the mark of student {i+1} "))
    names.append(name)
    marks.append(mark)

x = marks.index(max(marks))
y = marks.index(min(marks))

print(f"Highest mark holder: {names[x]} with {marks[x]} marks.")
print(f"Lowest mark holder: {names[y]} with {marks[y]} marks.")