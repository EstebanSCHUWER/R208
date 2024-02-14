class Voiture:
    def __init__(self, marque='Marque par défaut', modele='Modèle par défaut', puissance_fiscale=0, couleur='Couleur par défaut'):
        self.__marque = marque
        self.__modele = modele
        self.__puissance_fiscale = puissance_fiscale
        self.__couleur = couleur

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_puissance_fiscale(self):
        return self.__puissance_fiscale

    def get_couleur(self):
        return self.__couleur

    def set_marque(self, marque):
        self.__marque = marque

    def set_modele(self, modele):
        self.__modele = modele

    def set_puissance_fiscale(self, puissance_fiscale):
        self.__puissance_fiscale = puissance_fiscale

    def set_couleur(self, couleur):
        self.__couleur = couleur

if __name__ == "__main__":
    mycar1 = Voiture('Renault', 'Clio', 5, 'Bleu')

    print("Attributs de mycar1 (lecture):")
    print("Marque:", mycar1.get_marque())
    print("Modèle:", mycar1.get_modele())
    print("Puissance fiscale:", mycar1.get_puissance_fiscale())
    print("Couleur:", mycar1.get_couleur())

    mycar1.set_marque('Peugeot')
    mycar1.set_modele('208')
    mycar1.set_puissance_fiscale(4)
    mycar1.set_couleur('Rouge')

    print("\nAttributs de mycar1 après modification (lecture):")
    print("Marque:", mycar1.get_marque())
    print("Modèle:", mycar1.get_modele())
    print("Puissance fiscale:", mycar1.get_puissance_fiscale())
    print("Couleur:", mycar1.get_couleur())

    mycar2 = Voiture()

    mycar2.set_marque('Ford')
    mycar2.set_modele('Fiesta')
    mycar2.set_puissance_fiscale(4)
    mycar2.set_couleur('Noir')

    print("\nAttributs de mycar2 (lecture):")
    print("Marque:", mycar2.get_marque())
    print("Modèle:", mycar2.get_modele())
    print("Puissance fiscale:", mycar2.get_puissance_fiscale())
    print("Couleur:", mycar2.get_couleur())
