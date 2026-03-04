waga = int(input("Podaj swoją wagę: "))
wzrost = int(input("Podaj swój wzrost: "))

BMI = waga / ((wzrost/100)*(wzrost/100))

if BMI >= 30:
   print("Otyłość")
elif BMI >= 25:
   print("Nadwaga")
elif BMI >= 18.5:
   print("Waga prawidłowa")
else:
   print("Niedowaga")
