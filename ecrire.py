import re


def verifier_mot_de_passe(mot_de_passe):
    majuscules = len(re.findall(r'[A-Z]', mot_de_passe))
    chiffres = len(re.findall(r'\d', mot_de_passe))
    caracteres_speciaux = len(re.findall(r'[+-?.*]', mot_de_passe))

    return majuscules >= 2 and chiffres >= 3 and caracteres_speciaux >= 1


# Test de la fonction
print(verifier_mot_de_passe("P@ssw0rd"))  # Devrait retourner True
print(verifier_mot_de_passe("1234Abc"))  # Devrait retourner False (pas de caractères spéciaux)
print(verifier_mot_de_passe("AZ1234*"))  # Devrait retourner True
