# Tesztverseny
Egy közismereti versenyen a versenyzőknek 13+1, azaz összesen 14 tesztfeladatot tűznek ki. A versenyzőknek minden feladat esetén négy megadott lehetőség (A, B, C, D) közül kell a helyes választ megjelölniük. A versenybizottság garantálja, hogy tesztlapon minden kérdéshez pontosan egy helyes válasz tartozik. A kitöltött tesztlapokat elektronikusan rögzítik, a visszaélések elkerülése végett a versenyzőket betűkből és számokból álló kóddal azonosítják.

A helyes megoldást és a versenyzők válaszait a valaszok.txt szöveges állomány tartalmazza. A fájlban legfeljebb 500 versenyző adatai szerepelnek. A fájl első sorában a helyes válaszok szerepelnek. A fájl többi sora a versenyzők kódjával kezdődik, ezt egy szóköz, majd
az adott versenyző által adott válaszok sorozata követi. A versenyzők kódja legfeljebb 5 karakterből áll. A válaszok a feladatokkal egyező sorrendben, elválasztójel nélkül, nagybetűvel szerepelnek. Ha a versenyző egy kérdésre nem válaszolt, akkor annak helyén X
betű szerepel. Például:

```
BCCCDBBBBCDAAA
AB123 BXCDBBACACADBC
AH97 BCACDBDDBCBBCA
...
```
A 2. kérdésre a helyes válasz a C volt, de erre a kérdésre az AB123 kódú versenyző nem válaszolt.

Készítsen programot tesztverseny néven az alábbi feladatok megoldására! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 2. feladat:)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! A képernyőn megjelenő üzenetek az adott környezet
nyelvi sajátosságainak megfelelően a mintától eltérhetnek (pl. ékezetmentes betűk, tizedespont használata).

## Feladatok

<details>
<summary>
1. Olvassa be és tárolja el a valaszok.txt szöveges állomány adatait! <p>
</summary>


`1. feladat`
```python
válaszok = []
 
forrásfájl = open('valaszok.txt')
for sor in forrásfájl:
    válaszok.append(sor.strip().split())
forrásfájl.close()
```

<hr/>
</details>


<details>
<summary>
2. Jelenítse meg a képernyőn a mintának megfelelően, hogy hány versenyző vett részt a tesztversenyen! <p>
</summary>

`2. feladat`
```python
print('2. feladat: A vetélkedőn', len(válaszok), 'versenyző indult.')
```

<hr/>
</details>

<details>
<summary>
3. Kérje be egy versenyző azonosítóját, és jelenítse meg a mintának megfelelően a hozzá eltárolt válaszokat! Feltételezheti, hogy a fájlban létező azonosítót adnak meg. <p>
</summary>

`3. feladat`
```python
versenyzőazonosító = input('3. feladat: A versenyző azonosítója = ')
for bejegyzés in válaszok:
    if bejegyzés[0] == versenyzőazonosító:
        versenyző_válaszai = bejegyzés[1]
        print(versenyző_válaszai, ' (a versenyző válasza)')
        break
```

<hr/>
</details>

<details>
<summary>
4. Írassa ki a képernyőre a helyes megoldást! A helyes megoldás alatti sorba „+” jelet tegyen, ha az adott feladatot az előző feladatban kiválasztott versenyző eltalálta, egyébként egy szóközt! A kiírást a mintának megfelelő módon alakítsa ki! <p>
</summary>

`4. feladat`
```python
print('4. feladat')
print(helyes_válaszok, ' (a helyes megoldás)')
for index in range(len(versenyző_válaszai)):
    if versenyző_válaszai[index] == helyes_válaszok[index]:
        print('+', end='')
    else:
        print(' ', end='')
print(' (a versenyző helyes válaszai)')
```

<hr/>
</details>

<details>
<summary>
5. Kérje be egy feladat sorszámát, majd határozza meg, hogy hány versenyző adott a feladatra helyes megoldást, és ez a versenyzők hány százaléka! A százalékos eredményt a mintának megfelelően, két tizedesjeggyel írassa ki! <p>
</summary>

`5. feladat`
```python
feladat_sorszáma = int(input('5. feladat: A feladat sorszáma = '))
feladat_indexe = feladat_sorszáma - 1
 
számláló = 0
for bejegyzés in válaszok:
    if bejegyzés[1][feladat_indexe] == helyes_válaszok[feladat_indexe]:
        számláló += 1
print('A feladatra', számláló, 'fő, a versenyzők', round(számláló/len(válaszok)*100, 2), '%-a adott helyes választ.')
```

<hr/>
</details>


<details>
<summary>
6. A verseny feladatai nem egyenlő nehézségűek: az 1-5. feladat 3 pontot, a 6-10. feladat 4 pontot, a 11-13. feladat 5 pontot, míg a 14. feladat 6 pontot ér. Határozza meg az egyes versenyzők pontszámát, és a listát írassa ki a pontok.txt nevű állományba! Az állomány minden sora egy versenyző kódját, majd szóközzel elválasztva az általa elért pontszámot tartalmazza! <p>
</summary>

`6. feladat`
```python
pontok = []
for bejegyzés in válaszok:
    pontok.append([bejegyzés[0], feladatsort_pontoz(helyes_válaszok, bejegyzés[1])])
célfájl = open('pontok.txt', 'w')
for sor in pontok:
    print(sor[0], sor[1], file=célfájl)
célfájl.close()
```
`6. feladat feladatsort_pontoz`
```python
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
```

<hr/>
</details>

<details>
<summary>
7. A versenyen a három legmagasabb pontszámot elérő összes versenyzőt díjazzák. Például 5 indulónál előfordulhat, hogy 3 első és 2 második díjat adnak ki. Így megtörténhet az is, hogy nem kerül sor mindegyik díj kiadására. Írassa ki a mintának megfelelően a képernyőre a díjazottak kódját és pontszámát pontszám szerint csökkenő sorrendben! <p>
</summary>

`7. feladat`
```python
print('7. feladat: A verseny legjobbjai:')
ponthalmaz = set()
for bejegyzés in pontok:
    ponthalmaz.add(bejegyzés[1])
pontlista = sorted(list(ponthalmaz), reverse = True)[0:3]
 
for pontszám in pontlista:
    for bejegyzés in pontok:
        if bejegyzés[1] == pontszám:
             print(pontlista.index(pontszám)+1, '. (', pontszám, ' pont): ', bejegyzés[0], sep='')
```

<hr/>
</details>

## Minta a szöveges kimenetek kialakításához:
(A képernyőre írt üzeneteknek tartalmilag meg kell felelniük az alábbi mintának. Képernyőre írást nem igénylő feladatok esetén nem szükséges a feladat számát sem kiíratnia.)

```
1. feladat: Az adatok beolvasása

2. feladat: A vetélkedőn 303 versenyző indult.

3. feladat: A versenyző azonosítója = AB123
BXCDBBACACADBC (a versenyző válasza)

4. feladat:
BCCCDBBBBCDAAA (a helyes megoldás)
+ + + + (a versenyző helyes válaszai)

5. feladat: A feladat sorszáma = 10
A feladatra 111 fő, a versenyzők 36,63%-a adott helyes
választ.

6. feladat: A versenyzők pontszámának meghatározása
7. feladat: A verseny legjobbjai:
1. díj (56 pont): JO001
2. díj (52 pont): DG490
2. díj (52 pont): UA889
3. díj (49 pont): FX387
```
