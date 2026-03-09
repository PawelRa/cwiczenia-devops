kontakty = {}
next_id = 1

while True:
    print("\n--- KSIĄŻKA ADRESOWA ---")
    print("1. Dodaj kontakt")
    print("2. Wyświetl wszystkie kontakty")
    print("3. Wyszukaj kontakt")
    print("4. Usuń kontakt")
    print("5. Edytuj kontakt")
    print("6. Zakończ")

    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("Podaj telefon: ")
        email = input("Podaj email: ")

        if telefon.isdigit():
            kontakty[next_id] = {
                "imie": imie,
                "nazwisko": nazwisko,
                "telefon": telefon,
                "email": email
            }
            print("Dodano kontakt o ID:", next_id)
            next_id += 1
        else:
            print("Błąd: numer telefonu musi zawierać tylko cyfry.")

    elif wybor == "2":
        if len(kontakty) == 0:
            print("Brak kontaktów.")
        else:
            for id_kontaktu in kontakty:
                print("\nID:", id_kontaktu)
                print("Imię:", kontakty[id_kontaktu]["imie"])
                print("Nazwisko:", kontakty[id_kontaktu]["nazwisko"])
                print("Telefon:", kontakty[id_kontaktu]["telefon"])
                print("Email:", kontakty[id_kontaktu]["email"])

    elif wybor == "3":
        szukaj = input("Podaj imię lub nazwisko: ").lower()
        znaleziono = False

        for id_kontaktu in kontakty:
            imie = kontakty[id_kontaktu]["imie"].lower()
            nazwisko = kontakty[id_kontaktu]["nazwisko"].lower()

            if szukaj == imie or szukaj == nazwisko:
                print("\nID:", id_kontaktu)
                print("Imię:", kontakty[id_kontaktu]["imie"])
                print("Nazwisko:", kontakty[id_kontaktu]["nazwisko"])
                print("Telefon:", kontakty[id_kontaktu]["telefon"])
                print("Email:", kontakty[id_kontaktu]["email"])
                znaleziono = True

        if znaleziono == False:
            print("Nie znaleziono kontaktu.")

    elif wybor == "4":
        id_usun = input("Podaj ID kontaktu do usunięcia: ")

        if id_usun.isdigit():
            id_usun = int(id_usun)

            if id_usun in kontakty:
                del kontakty[id_usun]
                print("Kontakt usunięty.")
            else:
                print("Nie ma kontaktu o takim ID.")
        else:
            print("ID musi być liczbą.")

    elif wybor == "5":
        id_edytuj = input("Podaj ID kontaktu do edycji: ")

        if id_edytuj.isdigit():
            id_edytuj = int(id_edytuj)

            if id_edytuj in kontakty:
                nowe_imie = input("Nowe imię: ")
                nowe_nazwisko = input("Nowe nazwisko: ")
                nowy_telefon = input("Nowy telefon: ")
                nowy_email = input("Nowy email: ")

                if nowy_telefon.isdigit():
                    kontakty[id_edytuj]["imie"] = nowe_imie
                    kontakty[id_edytuj]["nazwisko"] = nowe_nazwisko
                    kontakty[id_edytuj]["telefon"] = nowy_telefon
                    kontakty[id_edytuj]["email"] = nowy_email
                    print("Kontakt został edytowany.")
                else:
                    print("Błąd: numer telefonu musi zawierać tylko cyfry.")
            else:
                print("Nie ma kontaktu o takim ID.")
        else:
            print("ID musi być liczbą.")

    elif wybor == "6":
        print("Koniec programu.")
        break

    else:
        print("Nieprawidłowy wybór.")
