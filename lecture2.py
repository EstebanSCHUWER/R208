def lecture2(nom_fichier, mot):
    count = 0
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                count += ligne.count(mot)
        print(f"Le mot '{mot}' est présent {count} fois dans le fichier.")
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
    except PermissionError:
        print("Vous n'avez pas les autorisations nécessaires pour accéder au fichier.")
    except IOError:
        print("Une erreur d'entrée/sortie s'est produite lors de la lecture du fichier.")
    except OSError as e:
        print(f"Erreur système : {e}")

# Test de la fonction lecture2
lecture2("python_info.txt", "Python")
