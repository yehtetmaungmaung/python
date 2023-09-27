"""
Using the data from the following lists, write a python code to create the following bar chart shown in figure. 
	For “BMW”, width=5, color=’red’, Days=[0.25, 1.25, 2.25, 3.25,4.25], 
	Distance= [50,40,70,80,20]
	For “Audi”, width=5, color=’blue’, Days=[0.75, 1.75, 2.75, 3.75,4.75], 
	Distance= [80,20,20,50,60]
"""

from matplotlib import pyplot as plt

plt.bar([0.25, 1.25, 2.25, 3.25, 4.25], [50, 40, 70, 80, 20], label="BMW", width=0.5, color="red")
plt.bar([0.75, 1.75, 2.75, 3.75, 4.75], [80, 20, 20, 50, 60], label="Audi", width=0.5, color="blue")


plt.title("information")
plt.xlabel("Days")
plt.ylabel("Distance(kms)")
plt.legend()
plt.show()