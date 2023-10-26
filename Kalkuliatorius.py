while True:
    print("1. Suėtis\n" 
          "2. Atimtis\n"
          "3. Daugyba \n"
          "4. Dalyba\n"
          "Išeiti - q\n")

    pasirinkimas = input(">>>")

    if pasirinkimas == "q":
        print("Išėjote iš programos :)")
        break
    if pasirinkimas not in ("1", "2", "3", "4"):

        print("tokio pasirinkimo nera")
        continue

    skaicius1 = int(input("įveskite skaičių"))
    skaicius2 = int(input("įveskite kitą skaičių"))
    if pasirinkimas == "1":
        print(f"Jūsų pasirinktų skaičių suma yra {skaicius1 + skaicius2}")
    if pasirinkimas == "2":
        print(f"Jūsų pasirinktų skaičių skirtumas yra {skaicius1 - skaicius2}")
    if pasirinkimas == "4":
        print(f"Jūsų pasirinktų skaičių dalmuo yra {skaicius1 / skaicius2}")