# Given a positive integer 5, The task is to write a Python program to check if the number is Prime or not in Python.

x = 67

def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        print(i)
        if x % i == 0:
            return False
    return True

if is_prime(x):
    print(x, "is a prime number.")
else:
    print(x, "is not a prime number.")
