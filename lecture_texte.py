import string
from math import *
from functions import * # module utilisateur


MyFile = './exemple_fichier_texte.txt'
# toujours utiliser cette commande avec ces paramètres
fp = open(MyFile, 'r', -1, 'utf-8') # ou "cp1252" pour ansi
try: # même construction qu'en Delphi
    for MyLigne in fp:
        print(MyLigne.strip()) # depuis Python 3.3, print est une fonction
finally:
    fp.close
    

#------------------------

print(Carre(32))
print(CubeCarre(32))
print(Max(32 ,666))
