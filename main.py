heslo = input("Zadej své heslo: Nesmí obsahovat #! ")
zakazany_znak = "#"

if len(heslo) <= 8 or zakazany_znak in heslo:
    print("Nebezpečné heslo")
else:
    print("Heslo je bezpečné")

