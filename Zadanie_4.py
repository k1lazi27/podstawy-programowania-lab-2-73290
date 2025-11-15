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