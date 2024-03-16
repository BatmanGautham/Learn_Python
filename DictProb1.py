"""
D = {'a':10,'b':20} be a dictionary. Write commands to 
a) Add new key value pair ('c':30)
b) Update value of b to 45
c) Delete
"""

D = {'a':10,'b':20}

D['c'] = 30
print("a. ",D)

D['b'] = 45
print("b. ",D)

del D['a']
D.pop('b')
print("c. ",D)