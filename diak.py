fajl=open("diak.txt","r",encoding="utf-8")

diakok=[]

for sor in fajl:
    sor=sor.strip()
    adat=sor.split(";")
    nev=adat[0]
    mag=int(adat[1])
    diakok.append([nev,mag])

fajl.close()



print("Diákok száma:", len(diakok))


# legmagasabb diák
legnev=diakok[0][0]
legmag=diakok[0][1]

for diak in diakok:
    if diak[1] > legmag:
        legmag = diak[1]
        legnev = diak[0]

print("Legmagasabb:", legnev, "-", legmag, "cm")


