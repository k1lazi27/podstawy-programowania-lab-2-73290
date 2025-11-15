
wynki_studenta = int(input("Podaj zdobyte punkty:"))

if wynki_studenta > 80:
    print("Student zalicza egzamin w terminie 0")
elif wynki_studenta > 50:
    print("Możesz poprawić wynik z egzaminu")
else:
    print("Musisz poprawić egzamin")