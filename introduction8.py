import math
def second_degre(a,b,c):


#a=(input("Entrez la valeur de A "))
#b=(input("Entrez la valeur de B "))
#c=(input("Entrez la valeur de C "))
a= int(a)
b= int(b)
c= int(c)

delta = (b * b) - (4 * a * c)

if a > 0:
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2 * a)
        x2 = (-b + math.sqrt(delta))/(2 * a)
        return (x1,x2)
        print(f"on a deux solutions {x1} et {x2}")
    elif delta == 0:
        x1 = (-b - math.sqrt(delta))/(2 * a)
        return (x1)
        print(f"on n'a qu'une solution {x1} ")
    elif delta < 0:
        print("Désolé !!! Aucune solution ")
elif a ==0:
    print("division par zero")