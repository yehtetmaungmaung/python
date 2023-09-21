# Write the python code for creating sets of union, intersection,
# difference and symmetric difference of the two string sets “Artificial” and “Intelligence”.

art = set("Artificial")
intel = set("Intelligence") 

u = art.union(intel)
i = art.intersection(intel)
d = art.difference(intel)
s = art.symmetric_difference(intel)

print(u)
print(i)
print(d)
print(s)