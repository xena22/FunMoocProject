###########################
#LA CONJECTURE DE SYRACUSE#
###########################
'''
la première valeur de la suite est le nombre n lui-même
si n est pair la valeur suivante sera n divisé par 2,
sinon la valeur suivante est 3n + 1 (n multiplié par 3 auquel on rajoute 1).
'''

n = int(input('valeur du nombre n dont on veut tester la conjecture : '))
while n != 1:
   if n % 2 == 0 :  # si un nombre entier modulo 2 vaut 0, il est pair
       n = n // 2
       print (n)
   else:                 # cas où le nombre est impair
       n = 3 * n + 1
       print (n)