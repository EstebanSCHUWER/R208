def is_domaine(domaine):
    return bool(re.match(r'^[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$', domaine))

# Test de la fonction
print(is_domaine("google.fr"))    # Devrait retourner True
print(is_domaine("openai.com"))   # Devrait retourner True
print(is_domaine("example.org"))  # Devrait retourner True
print(is_domaine("invalid"))      # Devrait retourner False
