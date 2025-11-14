
# wynki_studenta = int(input("Podaj zdobyte punkty:"))
#
# if wynki_studenta > 80:
#     print("Student zalicza egzamin w terminie 0")
# elif wynki_studenta > 50:
#     print("Możesz poprawić wynik z egzaminu")
# else:
#     print("Musisz poprawić egzamin")
#


#zadanie 2

# x = 10
# y = 3
# z = 5
# if x > y:
#     x, y = y, x
# if x > z:
#     x, z = z, x
# if y > z:
#     y, z = z, y
# print(f"1: {x}, 2: {y}, 3: {z}")

#zadanie 3
# Nazwa_pliku = "Raport_maj.xlsx"
#
# if Nazwa_pliku.endswith(".xlsx"):
#     print("Tak")
# else:
#     print("Nie")

# Zadanie 4

liczba_strzelonych_bramek = int(input("Podaj liczbe strzelonych bramek drużyny:"))

gol = liczba_strzelonych_bramek
points = liczba_strzelonych_bramek * 10

if gol > 5:
    points += 5
elif gol <= 5:
    points += 10
elif gol >= 10:
    points += 15
print(f"Liczba strzelonych bramek: {gol}, a liczba zdobytych punktów: {points}")