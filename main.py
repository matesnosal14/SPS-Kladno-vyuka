nakup = ["Opice" , "Jablko" , "Pes"]
nakup.remove("Opice")
srovnanilistu = sorted(nakup)
print(srovnanilistu)

for i in range(len(nakup)):
    print(f"{i}. {nakup[i]}")




