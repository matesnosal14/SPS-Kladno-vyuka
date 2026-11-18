a = int(input("cislo1"))
b = int(input())

while not(a == 0 or b == 0):
    if a > b:
        c = b // a
        b = b - (a*c)
    else:
        c = a // b
        a = a - (b*c)
    if b == 0:
        print("Největší dělitel je A")
    else:
        print("Největší dělitel je B")

      