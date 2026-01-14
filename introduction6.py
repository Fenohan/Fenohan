'''from asyncio.tools import exit_with_permission_help_text


a =[1,2,3,4,5,6,7,8]

print(a[:6])    # slicing [debut : fin : step]
for w in a:
    print(w)
a.append(10)    #ajout à la fin de la liste
a.insert(3,10)  # insert 10 à la position 3

print (a)
a.extend(a)
print (a)
a.sort() # reverse= true par défaut false 
print(a)
a.pop(19) # supprime l'index 19
print(a)
a.remove(10) # supprime le 10 trouvé en premier
print(a)
a.count(10) # combien de fois 10 apparait dans la liste
print(a)
print(len(a)) # retourne le nombre d'elements
for w,z in enumerate(a):    # retourn l'index et l'element
    print(w,z)
'''

'''
nb_prem = []
nb_autre = []

for i in range(2,120):
    j = i+1
    while j <= i:
        if (i%j) == 0:
            break
        else:
            print(i)
        j += 1
'''

a={"prime":[],"nonprime":[]}

'''for n in range(2,50):
    isPrime = True
    for i in range(2,n+1):
        if n % i == 0:
            isPrime = False
            break

    if isPrime:
        print(n)

'''

isprem=True
x = 0
y = 0

for i in range(2,420):
    for j in range (2,i):
    
        if (i % j) == 0:
            x = i
            isprem=False
            break
        else:
            y = i
            isprem=True
            break
            
    if isprem:
        a["nonprime"].append(x)
        
    else:
        a["prime"].append(y)
        
print(f"prem isika e {a["prime"]}")
print(f"tsy prem za a {a["nonprime"]}")

#print(a["nonprime"]["prime"])
#print(a["prime"])    

'''
ville=["paris","marseille","tana","ntsirabe"]
hab=[100,200,300]

for w,z in zip(ville,hab):   # vao tapitra ny len plus court dia mijanona ny boucle
    print(w,z)

mon_dict = {"key":"valeur"}

#exemple 
mon_dict ={"Paris":1000,
              "Tana":101,
              "Diego":201}

print(mon_dict["Tana"])
mon_dict["Londres"] = 900
print(mon_dict)
mon_dict["NY"] = [1900,1901,1902,1903]
print(mon_dict["NY"][2])  ## affiche 1902

a = [12,34,{"victorien":12,"pascal":34,"julien":"erere"},[1,2,3,{"email":"mail@gmail.com"}]]

print(a[3][3]["email"])
print(f"ny adresse mail an'i {a[2]["julien"]} dia {a[3][3]["email"]}")

'''