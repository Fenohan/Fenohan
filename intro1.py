from turtle import shape
import numpy as np
import matplotlib as mpl

a = np.array([[[1,2,3,"a"],[7,8,9,"b"]],[[4,5,6,"c"],[10,11,12,"d"]]])

print(np.ndim(a))
print(a.ndim)
print(a)
print(a.shape) 
b = np.zeros([2,4])
print(b)
c = np.ones([2,4])
print(c)

a = np.random.randn(5,5)
print(a)
print(f"ny max ao dia {a.max()}, ary ny min kosa {a.min()}. Rehefa natao zany ny somme dia manome {a.sum()}, moyenne {a.mean()}")

c = np.random.randint(1,100,(10,5))
print(c)
print(c.shape) # nb dimension
d = np.array([[1,2,3,4,5]])
print(d)
e = np.concatenate([c,d],axis=0)
print(e)
#f = np.concatenate([c,d],axis=1)  # tsy mety satria tsy mitovy ny isany
#print(f)

b = np.linspace(0,10,5)
print(b)

#mpl.plot(b)
#mpl.show()

c = np.arange(0,10,15)
print(c)

## reshape exemple (4,6) = 24 elements => (3,8) = 24 elements
g = np.random.randint(1,100,(6,4))
print(g)
print(g.shape) # nb dimension

h = np.reshape(g,shape=(8,3),order="C")
print(h)
print(h.shape) # nb dimension

j = np.reshape(g,shape=(8,3),order="F")
print(j)
print(j.shape) # nb dimension

print(j[0,1])
j[0,1] = j[6,2]
print(j)

for i in range(0,6):
    j[i,1] = 0

print(j)


