fajl=open("diak.txt","r",encoding="utf-8")

diakok=[]

for sor in fajl:
    sor=sor.strip()
    adat=sor.split()
    nev=adat[0]
    magassag=int(adat[1])
    diakok.append([nev,magassag])

fajl.close()

