class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele
        self.options = []

    def __str__(self):
        return f"Voiture {self.marque} {self.modele} avec options : {', '.join(self.options)}"

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        self._options = value

    def ajouter_option(self, opt):
        self.options.append(opt)

    def supprimer_option(self, opt):
        if opt in self.options:
            self.options.remove(opt)

    def is_option_present(self, opt):
        return opt in self.options


if __name__ == "__main__":
    voiture = Voiture("Toyota", "Corolla")
    print(voiture)  # Voiture Toyota Corolla avec options :
