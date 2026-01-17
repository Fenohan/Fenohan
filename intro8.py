import numpy as np


age = np.random.randint(-100,100,[1,100])
print(age)
agevalid = age[age>0]
print(f"tsy valid ireto {age[age<0]}")
age[age<0] = round(agevalid.mean())
print("====================================================================")
print(f"Valide indray ireto {agevalid}")
print(np.size(agevalid))
print("====================================================================")
Majeur = age[age>=18]
print(f"Majeur indray ireto {Majeur}")
print("====================================================================")
Mineur = age[age<18]
print(f"Mineur indray ireto {Mineur}")