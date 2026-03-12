class Produkt:
    def __init__(self, nazwa, cena, kod_produktu):
        self.nazwa = nazwa
        self.cena = cena
        self.kod_produktu = kod_produktu

    def oblicz_cene_koncowa(self):
        return self.cena

    def __str__(self):
        return f"{self.nazwa} | kod: {self.kod_produktu} | cena: {self.oblicz_cene_koncowa()} zł"


class Elektronika(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, gwarancja_miesiace):
        super().__init__(nazwa, cena, kod_produktu)
        self.gwarancja_miesiace = gwarancja_miesiace

    def oblicz_cene_koncowa(self):
        return round(self.cena * 1.23, 2)


class Ubranie(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, rozmiar, material):
        super().__init__(nazwa, cena, kod_produktu)
        self.rozmiar = rozmiar
        self.material = material

    def oblicz_cene_koncowa(self):
        return round(self.cena * 1.08, 2)


class Ksiazka(Produkt):
    def __init__(self, nazwa, cena, kod_produktu, autor, liczba_stron):
        super().__init__(nazwa, cena, kod_produktu)
        self.autor = autor
        self.liczba_stron = liczba_stron

    def oblicz_cene_koncowa(self):
        return round(self.cena * 1.05, 2)


class KoszykZakupowy:
    def __init__(self):
        self.__produkty = []

    def dodaj_produkt(self, produkt):
        self.__produkty.append(produkt)
        print(f"Dodano do koszyka: {produkt.nazwa}")

    def usun_produkt(self, kod_produktu):
        for produkt in self.__produkty:
            if produkt.kod_produktu == kod_produktu:
                self.__produkty.remove(produkt)
                print(f"Usunięto z koszyka: {produkt.nazwa}")
                return
        print("Nie znaleziono produktu w koszyku.")

    def oblicz_sume(self):
        suma = 0
        for produkt in self.__produkty:
            suma += produkt.oblicz_cene_koncowa()
        return round(suma, 2)

    def pokaz_produkty(self):
        if len(self.__produkty) == 0:
            print("Koszyk jest pusty.")
        else:
            print("\nProdukty w koszyku:")
            for produkt in self.__produkty:
                print("-", produkt)

    def pobierz_produkty(self):
        return self.__produkty.copy()


class Uzytkownik:
    def __init__(self, imie, nazwisko, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.__email = email

    def pobierz_email(self):
        return self.__email

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"


class Klient(Uzytkownik):
    def __init__(self, imie, nazwisko, email, adres, metoda_platnosci):
        super().__init__(imie, nazwisko, email)
        self.adres = adres
        self.__metoda_platnosci = metoda_platnosci
        self.historia_zamowien = []

    def pobierz_metode_platnosci(self):
        return self.__metoda_platnosci

    def dodaj_zamowienie(self, zamowienie):
        self.historia_zamowien.append(zamowienie)

    def pokaz_historie_zamowien(self):
        if len(self.historia_zamowien) == 0:
            print("Brak zamówień.")
        else:
            print("\nHistoria zamówień:")
            for zamowienie in self.historia_zamowien:
                print(zamowienie)


class Administrator(Uzytkownik):
    def __init__(self, imie, nazwisko, email, uprawnienia):
        super().__init__(imie, nazwisko, email)
        self.uprawnienia = uprawnienia

    def dodaj_produkt_do_sklepu(self, lista_produktow, produkt):
        lista_produktow.append(produkt)
        print(f"Administrator dodał produkt: {produkt.nazwa}")

    def usun_produkt_ze_sklepu(self, lista_produktow, kod_produktu):
        for produkt in lista_produktow:
            if produkt.kod_produktu == kod_produktu:
                lista_produktow.remove(produkt)
                print(f"Administrator usunął produkt: {produkt.nazwa}")
                return
        print("Nie znaleziono produktu do usunięcia.")


class Zamowienie:
    def __init__(self, koszyk, klient, status_zamowienia, metoda_platnosci):
        self.koszyk = koszyk
        self.klient = klient
        self.status_zamowienia = status_zamowienia
        self.metoda_platnosci = metoda_platnosci

    def zmien_status(self, nowy_status):
        self.status_zamowienia = nowy_status

    def __str__(self):
        return f"Zamówienie klienta {self.klient.imie} {self.klient.nazwisko} | status: {self.status_zamowienia} | suma: {self.koszyk.oblicz_sume()} zł | płatność: {self.metoda_platnosci}"


# Produkty
telefon = Elektronika("Smartfon", 2000, "E001", 24)
laptop = Elektronika("Laptop", 3500, "E002", 36)
koszulka = Ubranie("Koszulka", 100, "U001", "L", "Bawełna")
spodnie = Ubranie("Spodnie", 150, "U002", "M", "Jeans")
powiesc = Ksiazka("Władca Pierścieni", 50, "K001", "J.R.R. Tolkien", 600)

# Lista produktów w sklepie
produkty_w_sklepie = []

# Administrator
admin = Administrator("Adam", "Nowak", "admin@sklep.pl", "pełne")

admin.dodaj_produkt_do_sklepu(produkty_w_sklepie, telefon)
admin.dodaj_produkt_do_sklepu(produkty_w_sklepie, laptop)
admin.dodaj_produkt_do_sklepu(produkty_w_sklepie, koszulka)
admin.dodaj_produkt_do_sklepu(produkty_w_sklepie, spodnie)
admin.dodaj_produkt_do_sklepu(produkty_w_sklepie, powiesc)

# Klient
klient = Klient("Jan", "Kowalski", "jan@wp.pl", "ul. Leśna 5", "karta")

# Koszyk
koszyk = KoszykZakupowy()
koszyk.dodaj_produkt(telefon)
koszyk.dodaj_produkt(koszulka)
koszyk.dodaj_produkt(powiesc)

koszyk.pokaz_produkty()
print("Suma koszyka:", koszyk.oblicz_sume(), "zł")

# Usunięcie produktu
koszyk.usun_produkt("U001")
koszyk.pokaz_produkty()
print("Suma po usunięciu:", koszyk.oblicz_sume(), "zł")

# Zamówienie
zamowienie1 = Zamowienie(koszyk, klient, "Nowe", klient.pobierz_metode_platnosci())
klient.dodaj_zamowienie(zamowienie1)

print("\nDane zamówienia:")
print(zamowienie1)

# Zmiana statusu
zamowienie1.zmien_status("Opłacone")
print("Po zmianie statusu:")
print(zamowienie1)

# Historia zamówień klienta
klient.pokaz_historie_zamowien()

# Administrator usuwa produkt ze sklepu
admin.usun_produkt_ze_sklepu(produkty_w_sklepie, "E002")

print("\nProdukty dostępne w sklepie:")
for produkt in produkty_w_sklepie:
    print(produkt)
