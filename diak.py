# 1. Fájl beolvasása
fajl = open("diak.txt", "r", encoding="utf-8")
diakok = []

for sor in fajl:
    sor = sor.strip()
    nev, mag = sor.split(";")
    diakok.append([nev, int(mag)])

fajl.close()

print("Diákok száma:", len(diakok))

# 2. Legmagasabb diák keresése
legmag = 0
legnev = ""
for diak in diakok:
    if diak[1] > legmag:
        legmag = diak[1]
        legnev = diak[0]

print("Legmagasabb:", legnev, "-", legmag, "cm")

# 3. Rendezés 
diakok.sort(key=lambda x: x[1], reverse=True)

print("Tornasor:")
for diak in diakok:
    print(diak[0], diak[1])

fajl.close()
