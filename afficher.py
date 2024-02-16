import re

with open("utilisateur.txt", "r") as fichier:
    utilisateurs_bash = [ligne.split(':')[0] for ligne in fichier if re.search(r'/bin/bash$', ligne)]

print("Utilisateurs avec l'interpréteur bash:", utilisateurs_bash)
