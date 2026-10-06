kosik = ["BOTY" , "TRIČKO" , "PONOŽKY"]

print(f"Toto máte v seznamu {kosik}")

odebrani = input("Co chcete z košíku odstranit? ").upper()

if (odebrani) in kosik:
    kosik.remove(odebrani)
    print(f"Položka odebrána. Tvůj nový košík: {kosik}") 
else:
    print("Toto není vůbec v košíku")