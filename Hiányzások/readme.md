# Hiányzások

Egy osztály második félévi hiányzásai állnak rendelkezésére a naplo.txt fájlban. A hiányzások naponként csoportosítva szerepelnek, minden napot a # karakter kezd, majd egyegy szóközzel elválasztva a hónap és a nap sorszáma következik. Az aznapi hiányzások tanulónként külön sorokban vannak, a tanuló napi hiányzásait egy hét karakterből álló karaktersorozat írja le. A karaktersorozat minden karaktere egy-egy órát ad meg. Értéke az O betű, ha a tanuló jelen volt az adott órán, az X utal az igazolt, az I az igazolatlan távollétre, végül N betű jelzi, ha a tanulónak akkor nem volt órája. Például: 

```
# 01 15
Galagonya Alfonz OXXXXXN
# 01 16
Alma Hedvig OOOOOIO
Galagonya Alfonz XXXXXXX
```

A fenti példa a január 15-16-i hiányzásokat tartalmazza. Galagonya Alfonznak január 15-én hat órája lett volna, de csak az első órán volt jelen, utána igazoltan hiányzott. Alma Hedvignek január 16-án hét órája lett volna, de a 6. óráról igazolatlanul távol maradt. 

Az állomány legfeljebb 600 sort tartalmaz, az osztályba pedig legfeljebb 50 tanuló jár. Feltételezheti, hogy az osztályban nincs két azonos nevű tanuló, továbbá hogy minden tanulónak egy vezeték és egy utóneve van. Felhasználhatja, hogy a jelenlétre vonatkozó bejegyzés mindig 7 karakterből áll. 

Készítsen programot, amely az állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját hianyzasok néven mentse! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, és feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.)

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 3. feladat:)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az eredmények kiírásánál utaljon a kiírt adat jelentésére! A mintától eltérő, valamint az ékezetmentes kiírás is elfogadott.

<details>
<summary>
1. Olvassa be és tárolja el a naplo.txt fájl tartalmát! <p>
</summary>


`1. feladat`
```python
napló = []
 
forrásfájl = open('naplo.txt')
for sor in forrásfájl:
    sor = sor.strip().split()
    if sor[0] == '#': #dátumot találtunk
        hónap = int(sor[1])
        nap = int(sor[2])
    else: #hiányzás-bejegyzést találtunk
        vezetéknév = sor[0]
        keresztnév = sor[1]
        hiányzás = sor[2]
        napló.append([hónap, nap, vezetéknév + ' ' + keresztnév, hiányzás])
forrásfájl.close()
```

<hr/>
</details>

<details>
<summary>
2. Határozza meg és írassa ki, hogy hány sor van a fájlban, ami hiányzást rögzít! (A fenti példában 3 ilyen bejegyzés van.)  <p>
</summary>


`2. feladat`
```python
print('2. feladat')
print('A naplóban', len(napló), 'bejegyzés van.')
```

<hr/>
</details>

<details>
<summary>
3. Számolja meg és írassa ki, hogy összesen hány óra igazolt és hány óra igazolatlan hiányzásvolt a félév során!  <p>
</summary>


`3. feladat`
```python
print('3. feladat')
igazolt = 0
igazolatlan = 0
for bejegyzés in napló:
    igazolt += bejegyzés[3].count('X')
    igazolatlan += bejegyzés[3].count('I')
print('Az igazolt hiányzások száma', igazolt, 'az igazolatlanoké', igazolatlan, 'óra.')
 
```

<hr/>
</details>

Néhány tanár azt feltételezi, hogy a tanulók bizonyos órákról gyakrabban hiányoznak. A következő három feladatban ennek vizsgálatát kell előkészítenie

<details>
<summary>
4. Készítsen függvényt hetnapja néven, amely a paraméterként megadott dátumhoz (hónap, nap) megadja, hogy az a hét melyik napjára esik (hétfő, kedd…). Tudjuk, hogy az adott év nem volt szökőév, továbbá azt is, hogy január elseje hétfőre esett. Használhatja az alábbi algoritmust is, ahol a tömbök indexelése 0-val kezdődik, de ettől eltérő megoldású függvényt is készíthet!  <p>
</summary>




`4. feladat`
```python
def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", 'pentek', "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap-1]+nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja
```

<hr/>
</details>

```
Függvény hetnapja(honap:egesz, nap:egesz): szöveg
 napnev[]:= ("vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat")
 napszam[]:= (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335)
 napsorszam:= (napszam[honap-1]+nap) MOD 7
 hetnapja:= napnev[napsorszam]
Függvény vége
```

<details>
<summary>
5. Kérjen be egy dátumot (hónap, nap), és a hetnapja függvény felhasználásával írassa ki, hogy az a hét melyik napjára esett!  <p>
</summary>


`5. feladat`
```python
hónap = int(input('5. feladat\nA hónap sorszáma='))
nap = int(input('A nap sorszáma='))
print('Azon a napon', hetnapja(hónap, nap), 'volt.')
```

<hr/>
</details>

<details>
<summary>
6. Kérje be a hét egy tanítási napjának nevét és egy aznapi tanítási óra óraszámát (például: kedd 3)! Írassa ki a képernyőre, hogy a félév során az adott tanítási órára összesen hány hiányzás jutott!  <p>
</summary>


`6. feladat`
```python
napneve = input('6. feladat\nA nap neve=')
órasorszáma = int(input('Az óra sorszáma='))
hiányzások = 0
for bejegyzés in napló:
    if hetnapja(bejegyzés[0], bejegyzés[1]) == napneve:
        if bejegyzés[3][órasorszáma-1] in ['X', 'I']:
        hiányzások += 1
print('Ekkor összesen', hiányzások, 'óra hiányzás történt.')
```

<hr/>
</details>

<details>
<summary>
7. Írassa ki a képernyőre a legtöbb órát hiányzó tanuló nevét! Ha több ilyen tanuló is van, akkor valamennyi neve jelenjen meg szóközzel elválasztva! <p>
</summary>


`7. feladat`
```python
print('7. feladat:')
 
névhalmaz = set()
for bejegyzés in napló:
    névhalmaz.add(bejegyzés[2])
 
hiányzáslista = []
for név in névhalmaz:
    hiányzások = 0
    for bejegyzés in napló:
        if bejegyzés[2] == név:
            hiányzások = hiányzások + bejegyzés[3].count('X') + bejegyzés[3].count('I')
    hiányzáslista.append([név, hiányzások])
 
legnagyobb_hiányzás = 0
for bejegyzés in hiányzáslista:
    if bejegyzés[1] > legnagyobb_hiányzás:
    legnagyobb_hiányzás = bejegyzés[1]
 
legtöbbet_hiányzók = []
for bejegyzés in hiányzáslista:
    if bejegyzés[1] == legnagyobb_hiányzás:
        legtöbbet_hiányzók.append(bejegyzés[0])
 
print('A legtöbbet hiányzók:', ' '.join(legtöbbet_hiányzók))
```

<hr/>
</details>

## Minta a szöveges kimenetek kialakításához: 

```
2. feladat
A naplóban 139 bejegyzés van.
3. feladat
Az igazolt hiányzások száma 788, az igazolatlanoké 18 óra.
5. feladat
A hónap sorszáma=2
A nap sorszáma=3
Azon a napon szombat volt.
6. feladat
A nap neve=szerda
Az óra sorszáma=3
Ekkor összesen 49 óra hiányzás történt.
7. feladat
A legtöbbet hiányzó tanulók: Kivi Adrienn Jujuba Ibolya
```
