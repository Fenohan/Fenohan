import numpy as np

age = np.random.randint(-100,100,[1,100])
print(age)
agevalid = age[age>0]
print("===================================SUM=================================")
print(sum(age[age>=18]))
print("==================================SORT==================================")
print(np.sort(age))
print("=================================ARGSORT===================================")
print(age.argsort())
print("==================================SORT= trie le tableau ===================")
print(age.sort())
print("=================================ARGSORT===================================")
print(np.argsort(age))


