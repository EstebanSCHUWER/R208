import re

def prenom_composer(prenom):
    return bool(re.match(r'^[a-zA-Z]+-[a-zA-Z]+$', prenom))

# Test de la fonction
print(prenom_composer("Jean-Claude"))  # Devrait retourner True
print(prenom_composer("JeanClaude"))   # Devrait retourner False
