fajl = open("diak.txt", "r", encoding="utf-8")
diakok = []

for sor in fajl:
    sor = sor.strip()
    nev, mag = sor.split(";")
    diakok.append([nev, int(mag)])

fajl.close()

print("Diákok száma:", len(diakok))

# 2. Legmagasabb diák 

legmag = 0
legnev = ""
for diak in diakok:
    if diak[1] > legmag:
        legmag = diak[1]
        legnev = diak[0]

print("Legmagasabb:", legnev, "-", legmag, "cm")

# 3. Rendezés csökkenő sorrendben 

diakok.sort(key=lambda x: x[1], reverse=True)

print("Tornasor:")
for diak in diakok:
    print(diak[0], diak[1])


fajl = open("rendezve.txt", "w", encoding="utf-8")
for diak in diakok:
    fajl.write(diak[0] + " " + str(diak[1]) + "\n")
fajl.close()
