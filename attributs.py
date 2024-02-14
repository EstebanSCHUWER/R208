
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

if __name__ == "__main__":
    mycar1 = Voiture('Renault', 'Clio', 5, 'Bleu')

    print("Attributs de mycar1 à l'intérieur de la classe Voiture:")
    print("Marque:", mycar1.get_marque())
    print("Modèle:", mycar1.get_modele())
    print("Puissance fiscale:", mycar1.get_puissance_fiscale())
    print("Couleur:", mycar1.get_couleur())
