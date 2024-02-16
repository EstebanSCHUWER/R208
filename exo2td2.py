# 1. Lecture du contenu du fichier ligne par ligne
with open('exemple.txt', 'r') as fichier:
    for ligne in fichier:
        print(ligne.rstrip("\n"))  # rstrip pour supprimer les sauts de ligne

# 2. Écriture de chaque ligne non vide dans un nouveau fichier
with open('exemple.txt', 'r') as fichier_entree:
    with open('nouveau_fichier.txt', 'w') as fichier_sortie:
        for ligne in fichier_entree:
            if ligne.strip():  # Vérifie si la ligne n'est pas vide
                fichier_sortie.write(ligne)

# 3. Utilisation de la méthode with pour la lecture et l'écriture des fichiers
with open('exemple.txt', 'r') as infile:
    with open('nouveau_fichier.txt', 'w') as outfile:
        for ligne in infile:
            if ligne.strip():
                outfile.write(ligne)
