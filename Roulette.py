"""
Petit jeu de roulette au casino (version 1)
Auteur: Jonathan Meresse
Date : 5 Mai 2020
Petit jeu de devinette d'un nombre entier tiré aléatoirement
par le programme dans un intervalle donné

"""
import random
# importation des modules
regles=(print("Choississez un chiffre entre 0 et 15\n"
              "Si vous parriez entre 0 et 12 et que la bille tombe sur le bon resultat vous gangerez\n"
              "10 fois votre mise. Entre 13 et 14 2 fois votre mise si le chiffre est pair ou impair.\n"
              "Si vous pariez sur 15 et que la bille tombe sur 1,3,5,7,9,12 vous remportez 2 fois votre mise\n"
              "Si vous pariez sur 16 et que la bille tombe sur 2,4,6,8,10,11 vous remportez 2 fois votre mise"))
mise = int(input("Pariez sur un chiffre entre 0 et 15:"))
Roulette = random.randint(0,15)
#Roulette = int(input())
Argent = 10
Roulette15 = [1,3,5,7,9,12]
Roulette16 = [2,4,6,8,10,11]
while (mise <0 or mise >15):
    print ("Veuillez rentrer une valeur correct entre 0 et 15")
    mise = int(input())
if mise >=0 and mise <= 12 and mise == Roulette:
    Argent = Argent * 12
    print ("Votre porte monnaie est de :",Argent)
    print ("La Bille est tombée sur",Roulette)
elif mise == 13 and Roulette % 2 == 0 :
    Argent = Argent * 2
    print ("Votre porte monnaie est de :",Argent)
    print("La Bille est tombée sur", Roulette)
elif mise == 14 and Roulette % 2 != 0 :
    Argent = Argent * 2
    print ("Votre porte monnaie est de :",Argent)
    print("La Bille est tombée sur", Roulette)
elif mise == 15:
    if Roulette in Roulette15:
        Argent = Argent * 2
        print("Votre porte monnaie est de :",Argent)
        print("La Bille est tombée sur", Roulette)
    else:
        Argent = Argent - 10
        print("Votre porte monnaie est de :",Argent)
        print("La Bille est tombée sur", Roulette)
elif mise == 16:
    if Roulette in Roulette16:
        Argent = Argent * 2
        print("Votre porte monnaie est de :",Argent)
        print("La Bille est tombée sur", Roulette)
    else:
        Argent = Argent - 10
        print("Votre porte monnaie est de :",Argent)
        print("La Bille est tombée sur", Roulette)
else:
    Argent = Argent - 10
    print ("Votre porte monnaie est de :",Argent)
    print("La Bille est tombée sur", Roulette)







