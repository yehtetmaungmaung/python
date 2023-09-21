# Using the information from studentInfo.csv file,
# create tuples name with “studentInfo”.

import csv

studentInfo = []

with open("studentInfo.csv", mode="r") as f:
    reader = csv.reader(f)

    next(reader, None)

    for row in reader:
        name, age, grade = row
        info = (name, int(age), float(grade))
        studentInfo.append(info)


for v in studentInfo:
    print(v)