import re

def lecture3(nom_fichier):
    regex = re.compile(r"^([(+-)?(\d)+\.?(\d)*)$")
    try:
        with open(nom_fichier, 'r') as fichier:
            for ligne in fichier:
                mots = ligne.split()
                for mot in mots:
                    if regex.match(mot):
                        print(f"'{mot}' est un nombre.")
                    else:
                        print(f"'{mot}' n'est pas un nombre.")
    except FileNotFoundError:
        print("Le fichier spécifié est introuvable.")
    except PermissionError:
        print("Vous n'avez pas les autorisations nécessaires pour accéder au fichier.")
    except IOError:
        print("Une erreur d'entrée/sortie s'est produite lors de la lecture du fichier.")
    except OSError as e:
        print(f"Erreur système : {e}")

# Test de la fonction lecture3
lecture3("python_info.txt")
