f = open("valaszok.txt")
forras = []
megoldas = f.readline() 
for x in f:
    x = x.strip().split()
    azonosito = x[0]
    valasz = x[1]
    forras.append([azonosito,valasz])
f.close()

print("2.feladat")
print("A vetélkedőn {} versenyző indult".format(len(forras)))

print("3.feladat")
azonbe = input("A versenyző azonosítója: ")
for y in forras:
    if y[0] == azonbe:
        zu = y[1]
        print(zu + "(a verzenyző válasza)")
print("4.feladat")
kiirni = []
for s in range(13):
    if megoldas[s] == zu[s]:
        kiirni.append("+")
    else:
        kiirni.append(" ")
print(megoldas,"".join(kiirni),"(a versenyző helyes megoldásai)")

print("5.feladat")
befeladat = int(input("A feladat sorszáma: "))
hanyhelyes = 0
for c in forras:
    if c[1][befeladat-1] == megoldas[befeladat-1]:
        hanyhelyes += 1
print("A feladatra {} ember adott helyes választ, ez a versenyzők {:02.2f}%-a.".format(hanyhelyes,(hanyhelyes/len(forras)*100)))

print("6.feladat")
pontok = open("pontok.txt","w")
feladatpontok = [3,3,3,3,3,4,4,4,4,4,5,5,5,5,6]
for o in forras:
    pontja = 0
    for p in range(13):
        if o[1][p] == megoldas[p]:
            pontja += feladatpontok[p]
    print(o[0],pontja, file=pontok)
    
pontok.close()

print("7.feladat")
    



