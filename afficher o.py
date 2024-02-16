import re

with open("utilisateur.txt", "r") as fichier:
    utilisateurs_oo = [ligne.split(':')[0] for ligne in fichier if len(re.findall(r'o', ligne)) >= 2]

print("Utilisateurs avec deux lettres 'o' dans leur nom:", utilisateurs_oo)
