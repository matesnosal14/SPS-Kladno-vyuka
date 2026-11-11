from datetime import date

with open("osoby.txt", "w") as soubor:
    soubor.write("Petr 1990-08-28\n")
    soubor.write("Jana 1985-05-20\n")
    soubor.write("Pavel 2001-12-10\n")
    soubor.write("Lucie 1978-03-08\n")
    soubor.write("Martin 1995-07-25\n")
    soubor.write("Matyáš 2009-07-14\n")
    soubor.write("Matěj 2009-11-11\n")

    dnes = date.today() 
    vek = date.today()
with open('osoby.txt', 'r') as s:
  for radek in s: 
    data = radek.strip().split()
    jmeno = data[0] 
    datum_narozeni = data[1] 
    rok, mesic, den = map(int, datum_narozeni.split('-')) 
    if date(dnes.year, mesic, den) == dnes: 
      print(f"Blahopřeji k narozeninám, {jmeno}!")
    else:
       print(jmeno, vek)
