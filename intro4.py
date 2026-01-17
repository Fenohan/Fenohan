import numpy as np

tab1 = np.array([1,2,3])
tab2 = np.array([0,4,5,6])



def test1(tab):

    return all(tab != 0)
    return any(tab != 0)
    
def test2(tab):

    return any(tab != 0)
    


print(test1(tab1))
print(test2(tab2))