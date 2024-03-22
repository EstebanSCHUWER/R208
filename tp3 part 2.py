import json

class Film:
    def __init__(self, titre, date_sortie, note):
        self._titre = titre
        self._date_sortie = date_sortie
        self._note = note
        self._avis = []

    @property
    def titre(self):
        return self._titre

    @property
    def date_sortie(self):
        return self._date_sortie

    @property
    def note(self):
        return self._note

    @property
    def avis(self):
        return self._avis

    @titre.setter
    def titre(self, value):
        self._titre = value

    @date_sortie.setter
    def date_sortie(self, value):
        self._date_sortie = value

    @note.setter
    def note(self, value):
        self._note = value

    @avis.setter
    def avis(self, value):
        self._avis = value

    def ajouter_avis(self, avis):
        self._avis.append(avis)

    def __str__(self):
        avis_str = "\n".join(["- " + avis for avis in self._avis])
        return f"le film {self._titre} est sorti le {self._date_sortie}, il a la note {self._note} et voici les avis du public l'ayant vu :\n{avis_str}"

    def to_json(self):
        return {
            "titre": self._titre,
            "date_sortie": self._date_sortie,
            "note": self._note,
            "avis": self._avis
        }


class Bibliothèque:
    def __init__(self):
        self._films = []

    def ajouter_film(self, film):
        self._films.append(film)

    def afficher_films(self):
        for film in self._films:
            print(film)

    def mostrate(self):
        max_rating_film = max(self._films, key=lambda x: x.note)
        print(f"Le film avec la note la plus élevée est : {max_rating_film.titre}")

    def top3(self):
        top_3_films = sorted(self._films, key=lambda x: x.note, reverse=True)[:3]
        print("Top 3 des films les mieux notés :")
        for film in top_3_films:
            print(film.titre)

    def lastmovie(self):
        regex = re.compile(r"\d{4}-\d{2}-\d{2}")
        sorted_films = sorted(self._films, key=lambda x: regex.findall(x.date_sortie)[-1])
        print(f"Le film le plus récent dans la bibliothèque est : {sorted_films[-1].titre}")

    def avrgnote(self):
        total_notes = sum(film.note for film in self._films)
        avg_note = total_notes / len(self._films)
        print(f"La note moyenne de l'ensemble des films de la bibliothèque est : {avg_note:.2f}")

    def to_json_file(self, filename):
        with open(filename, "w") as file:
            json.dump([film.to_json() for film in self._films], file, indent=4)

    def from_json(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for film_data in data:
                film = Film(film_data["titre"], film_data["date_sortie"], film_data["note"])
                film.avis = film_data["avis"]
                self.ajouter_film(film)

if __name__ == "__main__":
    biblio = Bibliothèque()
    film1 = Film("Gladiator", "2000-05-05", 4.5)
    film1.ajouter_avis("Epic historical drama!")
    film1.ajouter_avis("Russell Crowe delivers a powerhouse performance!")
    biblio.ajouter_film(film1)

    film2 = Film("Inception", "2010-07-16", 4.8)
    film2.ajouter_avis("Mind-bending masterpiece!")
    film2.ajouter_avis("Leonardo DiCaprio shines!")
    biblio.ajouter_film(film2)

    biblio.to_json_file("films.json")

    print("Avant la lecture depuis le fichier JSON :")
    biblio.afficher_films()

    biblio.from_json("films.json")

    print("\nAprès la lecture depuis le fichier JSON :")
    biblio.afficher_films()
