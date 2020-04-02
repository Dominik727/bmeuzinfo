
#!/usr/bin/env python3
 
def feladatsort_pontoz(helyesek, mostaniak):
    pontszám = 0
    for index in range(len(helyesek)):
        if helyesek[index] == mostaniak[index]:
            if 0 <= index <= 4:
                pontszám += 3
            elif 5 <= index <= 9:
                pontszám += 4
            elif 10 <= index <= 12:
                pontszám += 5
            elif index == 13:
                pontszám += 6
    return pontszám
 
#1. feladat
válaszok = []
 
forrásfájl = open('valaszok.txt')
for sor in forrásfájl:
    válaszok.append(sor.strip().split())
forrásfájl.close()
 
helyes_válaszok = válaszok[0][0]
válaszok = válaszok[1:]
 
print('2. feladat: A vetélkedőn', len(válaszok), 'versenyző indult.')
 
versenyzőazonosító = input('3. feladat: A versenyző azonosítója = ')
for bejegyzés in válaszok:
    if bejegyzés[0] == versenyzőazonosító:
        versenyző_válaszai = bejegyzés[1]
        print(versenyző_válaszai, ' (a versenyző válasza)')
        break
 
print('4. feladat')
print(helyes_válaszok, ' (a helyes megoldás)')
for index in range(len(versenyző_válaszai)):
    if versenyző_válaszai[index] == helyes_válaszok[index]:
        print('+', end='')
    else:
        print(' ', end='')
print(' (a versenyző helyes válaszai)')
 
feladat_sorszáma = int(input('5. feladat: A feladat sorszáma = '))
feladat_indexe = feladat_sorszáma - 1
 
számláló = 0
for bejegyzés in válaszok:
    if bejegyzés[1][feladat_indexe] == helyes_válaszok[feladat_indexe]:
        számláló += 1
print('A feladatra', számláló, 'fő, a versenyzők', round(számláló/len(válaszok)*100, 2), '%-a adott helyes választ.')
 
#6. feladat
pontok = []
for bejegyzés in válaszok:
    pontok.append([bejegyzés[0], feladatsort_pontoz(helyes_válaszok, bejegyzés[1])])
célfájl = open('pontok.txt', 'w')
for sor in pontok:
    print(sor[0], sor[1], file=célfájl)
célfájl.close()
 
print('7. feladat: A verseny legjobbjai:')
ponthalmaz = set()
for bejegyzés in pontok:
    ponthalmaz.add(bejegyzés[1])
pontlista = sorted(list(ponthalmaz), reverse = True)[0:3]
 
for pontszám in pontlista:
    for bejegyzés in pontok:
        if bejegyzés[1] == pontszám:
             print(pontlista.index(pontszám)+1, '. (', pontszám, ' pont): ', bejegyzés[0], sep='')