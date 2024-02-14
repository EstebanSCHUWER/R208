mycar = voiture('Mercedes', 'Classe A', 7, 'rouge')
print(mycar)

class voiture:
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

    def __str__(self):
        return f"Voici les caractéristiques de cette voiture:\n- Marque : {self.get_marque()}\n- Modele : {self.get_modele()}\n- Couleur : {self.get_couleur()}\n- Puissance : {self.get_puissance_fiscale()}"

if __name__ == "__main__":
    mycar = voiture('Mercedes', 'Classe A', 7, 'rouge')

    print(mycar)

