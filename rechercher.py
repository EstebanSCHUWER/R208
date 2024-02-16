import re

with open("utilisateur.txt", "r") as fichier:
    utilisateurs_bash = sum(1 for ligne in fichier if re.search(r'/bin/bash$', ligne))

print("Nombre d'utilisateurs avec bash comme interpréteur:", utilisateurs_bash)
