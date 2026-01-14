import random
b = (random.randint(1,100))

tentative = 3

a = 0

while  (tentative >= 1):
    a = input("Vinanio ny vidin'io entana io (1 - 100) : ")
    a = int(a)
    tentative -= 1

    if b==a:
        print (" Tena mahay !!!!")
        break
    elif (b < a) :
        print(f"ampidino !!! in-{tentative} mamaly sisa ")
    elif (b > a) :
        print(f"ampiakaro !!! in-{tentative} mamaly sisa ")
if (tentative == 0):
    print("Tsy afaka miteny intsony")
    
    
    

