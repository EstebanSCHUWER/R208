from voiture import *;

if __name__ == "__main__":
    mycar1 = Voiture('Renault', 'Clio', 5, 'Bleu')
    print("mycar1:")
    print("Marque:", mycar1.marque)
    print("Modèle:", mycar1.modele)
    print("Puissance fiscale:", mycar1.puissance_fiscale)
    print("Couleur:", mycar1.couleur)

    mycar2 = Voiture()
    print("\nmycar2:")
    print("Marque:", mycar2.marque)
    print("Modèle:", mycar2.modele)
    print("Puissance fiscale:", mycar2.puissance_fiscale)
    print("Couleur:", mycar2.couleur)

    mycar3 = Voiture('Peugeot', '208', 4)
    print("\nmycar3:")
    print("Marque:", mycar3.marque)
    print("Modèle:", mycar3.modele)
    print("Puissance fiscale:", mycar3.puissance_fiscale)
    print("Couleur:", mycar3.couleur)

    mycar4 = Voiture(couleur='Rouge')
    print("\nmycar4:")
    print("Marque:", mycar4.marque)
    print("Modèle:", mycar4.modele)
    print("Puissance fiscale:", mycar4.puissance_fiscale)
    print("Couleur:", mycar4.couleur)