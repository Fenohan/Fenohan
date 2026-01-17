import numpy as np

c = np.random.randint(1,10,(3,10))
#print(c)

c[0:1,0:10] = 0
#print(c)
c[1:2,0:10] = 1
#print(c)
c[2:3,0:10] = 5
print(c)

tab2= c[0:1,0:10]
print(tab2)
tab1= c[1:2,0:10]
print(tab1)
tab3= c[2:3,0:10]
print(tab3)
tab4= c[0:1]
print(tab4)

tab0 = np.zeros(10)  
print(tab0)
tab5 = np.full(10,5)  # 5 = valeur ao anatiny 10 = nombre
print(tab5)




