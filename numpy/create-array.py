import numpy as np

arr_1 = np.array([1,2,3,4,5])
print(arr_1)

arr_2 = np.array([6,7,8,9], dtype='float32')
print(arr_2)

arr_3 = np.array([range(i, i + 3) for i in [2,4,6]])
print(arr_3)

print(np.zeros(5, dtype=int))
print(np.full((3,3), 2))

print(np.random.random((3,3)))