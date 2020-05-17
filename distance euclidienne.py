"""
On peut imaginer les variables indépendantes (dans une équation de régression) comme définissant
un espace multidimensionnel dans lequel chaque observation peut être tracée. La distance Euclidienne
est une distance géométrique dans cet espace multidimensionnel. Il est calculé comme :

distance(x,y) = {Si (xi - yi )2}1/2

"""

def distance_points(entre_1, entre_2):
    dist = ((entre_1[0] - entre_2[0])**2 + (entre_1[1] - entre_2[1])**2)**0.5
    return dist

print(distance_points((-1.0, 0.5), (2.0, 1.0)))

