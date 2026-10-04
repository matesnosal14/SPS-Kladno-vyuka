cislo1 = float(input("Zadej své první číslo: "))
cislo2 = float(input("Zadej své druhé číslo: "))
operace = input("Jakou operaci chceš provést ?")

if operace == "+"  :
    print(f" Výsledek: {cislo1 + cislo2}")
elif operace == "-":
    print(f" Výsledek: {cislo1 - cislo2}")
elif operace == "*":
    print(f" Výsledek: {cislo1 * cislo2}")
elif operace == "/":
    if cislo2 == 0:
        print("Nulou nelze dělit tlamo! ")
    else:
        print(f" Výsledek: {cislo1 / cislo2}")
else:
    print("Neznámá operace")


