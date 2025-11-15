#zadanie 2

x = int(input("Podaj wartość x : "))
y = int(input("Podaj wartość y : "))
z = int(input("Podaj wartość z : "))
if x > y:
    x, y = y, x
if x > z:
    x, z = z, x
if y > z:
    y, z = z, y
print(f"1: {x}, 2: {y}, 3: {z}")