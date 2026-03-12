class Ksiazka:
    def __init__(self, tytul, autor, isbn, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.isbn = isbn
        self.rok_wydania = rok_wydania
        self.dostepna = True

    def __str__(self):
        status = "Dostępna" if self.dostepna else "Wypożyczona"
        return f"{self.tytul} | {self.autor} | ISBN: {self.isbn} | {self.rok_wydania} | {status}"


class Czytelnik:
    def __init__(self, imie, nazwisko, numer_czytelnika):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_czytelnika = numer_czytelnika
        self.wypozyczone_ksiazki = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} | Nr czytelnika: {self.numer_czytelnika}"


class Biblioteka:
    def __init__(self, nazwa, adres):
        self.nazwa = nazwa
        self.adres = adres
        self.__kolekcja_ksiazek = []
        self.__lista_czytelnikow = []

    def dodaj_ksiazke(self, ksiazka):
        self.__kolekcja_ksiazek.append(ksiazka)
        print(f"Dodano książkę: {ksiazka.tytul}")

    def zarejestruj_czytelnika(self, czytelnik):
        self.__lista_czytelnikow.append(czytelnik)
        print(f"Zarejestrowano czytelnika: {czytelnik.imie} {czytelnik.nazwisko}")

    def wyszukaj_ksiazke(self, fraza):
        wyniki = []

        for ksiazka in self.__kolekcja_ksiazek:
            if (
                fraza.lower() in ksiazka.tytul.lower()
                or fraza.lower() in ksiazka.autor.lower()
                or fraza == ksiazka.isbn
            ):
                wyniki.append(ksiazka)

        return wyniki

    def znajdz_czytelnika(self, numer_czytelnika):
        for czytelnik in self.__lista_czytelnikow:
            if czytelnik.numer_czytelnika == numer_czytelnika:
                return czytelnik
        return None

    def znajdz_ksiazke_po_isbn(self, isbn):
        for ksiazka in self.__kolekcja_ksiazek:
            if ksiazka.isbn == isbn:
                return ksiazka
        return None

    def wypozycz_ksiazke(self, numer_czytelnika, isbn):
        czytelnik = self.znajdz_czytelnika(numer_czytelnika)
        ksiazka = self.znajdz_ksiazke_po_isbn(isbn)

        if czytelnik is None:
            print("Nie znaleziono czytelnika.")
            return

        if ksiazka is None:
            print("Nie znaleziono książki.")
            return

        if not ksiazka.dostepna:
            print("Ta książka jest już wypożyczona.")
            return

        ksiazka.dostepna = False
        czytelnik.wypozyczone_ksiazki.append(ksiazka)
        print(f"Wypożyczono książkę '{ksiazka.tytul}' czytelnikowi {czytelnik.imie} {czytelnik.nazwisko}.")

    def zwroc_ksiazke(self, numer_czytelnika, isbn):
        czytelnik = self.znajdz_czytelnika(numer_czytelnika)
        ksiazka = self.znajdz_ksiazke_po_isbn(isbn)

        if czytelnik is None:
            print("Nie znaleziono czytelnika.")
            return

        if ksiazka is None:
            print("Nie znaleziono książki.")
            return

        if ksiazka in czytelnik.wypozyczone_ksiazki:
            czytelnik.wypozyczone_ksiazki.remove(ksiazka)
            ksiazka.dostepna = True
            print(f"Zwrócono książkę '{ksiazka.tytul}'.")
        else:
            print("Ten czytelnik nie ma wypożyczonej tej książki.")

    def stan_wypozyczen_czytelnika(self, numer_czytelnika):
        czytelnik = self.znajdz_czytelnika(numer_czytelnika)

        if czytelnik is None:
            print("Nie znaleziono czytelnika.")
            return

        print(f"\nCzytelnik: {czytelnik.imie} {czytelnik.nazwisko}")

        if len(czytelnik.wypozyczone_ksiazki) == 0:
            print("Brak wypożyczonych książek.")
        else:
            print("Wypożyczone książki:")
            for ksiazka in czytelnik.wypozyczone_ksiazki:
                print("-", ksiazka.tytul)

    def wyswietl_ksiazki(self):
        print(f"\nKsiążki w bibliotece {self.nazwa}:")
        for ksiazka in self.__kolekcja_ksiazek:
            print(ksiazka)

    def wyswietl_czytelnikow(self):
        print(f"\nCzytelnicy biblioteki {self.nazwa}:")
        for czytelnik in self.__lista_czytelnikow:
            print(czytelnik)

# Tworzenie biblioteki
biblioteka = Biblioteka("Biblioteka Miejska", "ul. Główna 10")

# Tworzenie książek
ksiazka1 = Ksiazka("Pan Tadeusz", "Adam Mickiewicz", "111", 1834)
ksiazka2 = Ksiazka("Lalka", "Bolesław Prus", "222", 1890)
ksiazka3 = Ksiazka("Wiedźmin", "Andrzej Sapkowski", "333", 1993)

# Dodawanie książek
biblioteka.dodaj_ksiazke(ksiazka1)
biblioteka.dodaj_ksiazke(ksiazka2)
biblioteka.dodaj_ksiazke(ksiazka3)

# Tworzenie czytelników
czytelnik1 = Czytelnik("Jan", "Kowalski", "C001")
czytelnik2 = Czytelnik("Anna", "Nowak", "C002")

# Rejestrowanie czytelników
biblioteka.zarejestruj_czytelnika(czytelnik1)
biblioteka.zarejestruj_czytelnika(czytelnik2)

# Wyświetlenie danych
biblioteka.wyswietl_ksiazki()
biblioteka.wyswietl_czytelnikow()

# Wypożyczenie książki
biblioteka.wypozycz_ksiazke("C001", "111")

# Próba ponownego wypożyczenia tej samej książki
biblioteka.wypozycz_ksiazke("C002", "111")

# Stan wypożyczeń
biblioteka.stan_wypozyczen_czytelnika("C001")

# Wyszukiwanie książki
wyniki = biblioteka.wyszukaj_ksiazke("Lalka")
print("\nWyniki wyszukiwania:")
for ksiazka in wyniki:
    print(ksiazka)

# Zwrot książki
biblioteka.zwroc_ksiazke("C001", "111")

# Stan po zwrocie
biblioteka.stan_wypozyczen_czytelnika("C001")

# Końcowy stan książek
biblioteka.wyswietl_ksiazki()
