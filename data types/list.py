import sys

sys.argv = ['./test.txt']
f = open(sys.argv[0])
lines = f.readlines()
f.close()

fvalues = [float(line) for line in lines]
print("The maximum value is ", max(fvalues))
print("The minumum value is ", min(fvalues))