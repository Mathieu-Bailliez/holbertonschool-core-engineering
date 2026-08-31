#!/usr/bin/env python3
"""Module : """


# 2. Alphabet Game (Lowercase)

for alphabts in range(97, 123):
    if alphabts != 101 and alphabts != 113:
        print(chr(alphabts), end="")

# Etape 1. On crée une variable vide pour stocker les lettres
result = ""

# Etape 2. On boucle jusqu'à 123 pour inclure le 'z' (122)
for alphabet in range(97, 123):
    if alphabet != 101 and alphabet != 113:
        # Etape 3. On ajoute la lettre à notre variable
        result = result + chr(alphabet)

# Etape 4. On affiche tout d'un coup (le saut de ligne automatique est préservé !)
print(result)


# Ce qui ma bloquer

"""
J'ai tenter de créer une variable qui contient abcd...z et ca marche mais la boucle for n'est pas utiliser
dans ce cas

le dernier saut de ligne était ce qui ma bloquer le plus longtemps en un SEUL print sinon il fallait systématiquement
mettre un deuxiéme print() vide aprés la boucle
"""


# Ce que j'ai appris :

"""
J'ai appris a utiliser une variable pour stocker l'accumulation et le résultat de
la boucle
ce qui permet ensuite avec un seul print d'avoir le comportement normal de saut de ligne
avec le end="" tout en ayant les caractére coller entre eux
Tout ca en UN seul Print
"""
