"""
Jeu du célèbre RANDOM
Auteur: Jonathan Meresse
Date : 6 Mai 2020
Trouvez le nombre mystère en 6 coups

"""
import random
i = 0
NB_ESSAIS_MAX = 6 # défini le nombre d'essais
secret = random.randint(0, 100) 
print ("Trouvez le nombre mystère entre 0 et 100.Nombre d'essai : 6")
c= int(input("Choississez un nombre :"))
while c != secret:
    if c<secret:
        i = i + 1
        if i == NB_ESSAIS_MAX :
            print("Perdu ! le secret était ", secret)
            break
        print ("Trop petit. Nombre d'essai(s) restant(s):",6-i)
        c = int(input("Choississez un nombre :"))
    elif c>secret:
        i = i + 1
        if i == NB_ESSAIS_MAX:
            print("Perdu ! Le secret était", secret)
            break
        print ("Trop grand. Nombre d'essai(s) restant(s):",6-i)
        c = int(input("Choississez un nombre :"))
if c == secret :
    print ("Gagné en " ,i + 1," essais !")









