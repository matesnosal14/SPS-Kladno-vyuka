vek = int(input("Kolik ti je let? "))
obcanstvi = input("Jsi občan ČR? ")

if vek >= 18 and obcanstvi == "ano":
    print("Můžeš volit")
else:
    print("VOlit nemůžeš!")

