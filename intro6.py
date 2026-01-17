import numpy as np

c = np.arange(30,61,1)

print(c)



def test1(initial, max_plus, incrementation):
    return np.arange(initial,max_plus + 1,incrementation)

print(test1(30,60,1))