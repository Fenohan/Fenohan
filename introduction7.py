tableau1=[5,1,6,3,8]
print(min(tableau1))
print(sum(tableau1))
pi = 3.14
print(round(pi,1))

tableau2 = [True,False,True]
print(all(tableau2))
print(any(tableau2))
''''
f = open("text2.txt","w")  # ouvrir fichier en mode ecriture
f.write(" salut les 5 amis ")
f.close

with open("text.txt","r") as file:
    content = file.read()
    print(content)

    '''

import math
print(math.cos(2))

import random
print(random.choice(tableau1))
print(random.shuffle(tableau1))