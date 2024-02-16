# 1. Fonction divise1
def divise1(a, b):
    c = a / b
    return c

# 2. Main
def main():
    a = float(input("Saisir a : "))
    b = float(input("Saisir b : "))
    c = divise1(a, b)
    print(f"La division de {a} par {b} donne {c}")

# 3. Gestion de l'erreur de division par zéro
def divise2(a, b):
    if b == 0:
        print("Erreur, b est égal à 0 et on ne peut pas diviser par zéro")
        print("La division n’est pas possible dans ce cas")
        return None
    else:
        return a / b

# 7. Gestion de l'erreur avec try/except/else
def divise3(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur, b est égal à 0 et on ne peut pas diviser par zéro")
        print("La division n’est pas possible dans ce cas")
    else:
        return result

# 4. Test de divise2
def test_divise2():
    a = float(input("Saisir a : "))
    b = float(input("Saisir b : "))
    result = divise2(a, b)
    if result is not None:
        print(f"La division de {a} par {b} donne {result}")

# 5. Provoquer une erreur mathématique
def provoke_math_error():
    a = float(input("Saisir a : "))
    b = float(input("Saisir b : "))
    try:
        result = a / b
    except ZeroDivisionError:
        print("Erreur, b est égal à 0 et on ne peut pas diviser par zéro")
        print("La division n’est pas possible dans ce cas")
    except Exception as e:
        print(f"Autre exception : {e}")

# 8. Résoudre le problème de saisie de "aaa" avec try/except/else
def handle_invalid_input():
    try:
        a = float(input("Saisir a : "))
        b = float(input("Saisir b : "))
        result = a / b
    except ValueError:
        print("Erreur de saisie : veuillez entrer des nombres réels.")
    except ZeroDivisionError:
        print("Erreur, b est égal à 0 et on ne peut pas diviser par zéro")
        print("La division n’est pas possible dans ce cas")
    else:
        print(f"La division de {a} par {b} donne {result}")

# 9. Boucle pour saisir les nombres jusqu'à ce qu'ils soient réels
def input_real_numbers():
    while True:
        try:
            a = float(input("Saisir a : "))
            b = float(input("Saisir b : "))
        except ValueError:
            print("Erreur de saisie : veuillez entrer des nombres réels.")
        else:
            break
    return a, b

# Utilisation de la fonction main()
if __name__ == "__main__":
    main()
