from turtle import shape
import numpy as np
np.random.seed(0)

c = np.random.randint(1,100,(4,6))
print(c)


#print(c[0:2,0:2])

print(c[1:3,1:5])
c[1:3,1:5] = 0
print(c)

c = np.random.randint(1,100,(4,6))
print(c)
c[::2,::2] = 0
print(c)
