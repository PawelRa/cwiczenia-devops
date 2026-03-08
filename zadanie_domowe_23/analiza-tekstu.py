text = input("Wpisz tekst do analizy: ")
slowa =  text.split()
analizowany_tekst = text.lower()
dlugosc_tekstu = len(text)
dlugosc_tekstu_bez_znakow = len(text.replace(" ",""))
ilosc_slow = len(slowa)
ilosc_zdan = text.count(".") + text.count("!") + text.count("?")
najdluzsze_slowo = max(slowa, key=len)
licznik = {}

if ilosc_zdan == 0:
   ilosc_zdan = 1

for slowo in slowa:
    if slowo in licznik:
        licznik[slowo] += 1
    else:
        licznik[slowo] = 1

max_wystapien = max(licznik.values())
najczestsze_slowa = []

for slowo, ile in licznik.items():
    if ile == max_wystapien:
        najczestsze_slowa.append(slowo)

print(f"Twój tekst {text } ma {dlugosc_tekstu} znaków. Bez spacji {dlugosc_tekstu_bez_znakow} znaków.")
print(f"W tekście znajduje się {ilosc_slow} słów oraz {ilosc_zdan} zdań. Najdłuższe słowo to {najdluzsze_slowo}")
print(f"Najczęściej występujące słowo to {najczestsze_slowa}")
