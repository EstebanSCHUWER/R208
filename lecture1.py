def lecture1(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                print(ligne.rstrip('\n'))
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
    except PermissionError:
        print("Vous n'avez pas les autorisations nécessaires pour accéder au fichier.")
    except IOError:
        print("Une erreur d'entrée/sortie s'est produite lors de la lecture du fichier.")
    except OSError as e:
        print(f"Erreur système : {e}")

# Test de la fonction lecture1 avec un fichier inexistant
lecture1("fichier_inexistant.txt")
