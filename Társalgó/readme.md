# Társalgó

Egy színház társalgójában még a délelőtti próbák alatt is nagy a forgalom. A színészek hosszabb-rövidebb beszélgetésekre térnek be ide, vagy éppen csak keresnek valakit. A feladatban a társalgó ajtajánál 9 és 15 óra között felvett adatokat kell feldolgoznia.

Az ajto.txt fájlban időrendben rögzítették, hogy ki és mikor lépett be vagy ki a társalgó egyetlen ajtaján. A fájl soraiban négy, szóközzel elválasztott érték található. Az első két szám az áthaladás időpontja (óra, perc), a harmadik a személy azonosítója, az utolsó az áthaladás iránya (be/ki). A sorok száma legfeljebb 1000, a személyek azonosítója egy 1 és 100 közötti egész szám. Biztosan tudjuk, hogy a megfigyelés kezdetén (9 órakor) a társalgó üres volt, de a megfigyelés végén (15 órakor) még lehettek benn a társalgóban. A társalgóba be- és kilépéseket azok sorrendjében tartalmazza az állomány, még akkor is, ha a perc pontossággal rögzített adatok alapján egyezőség áll fenn. 


|  Fájl	|  	|  	| adatai 	| Bentlévők száma 	|
|:-:	|:--:	|:--:	|:--:	|---	|
| 9 	| 1 	| 2 	| be 	| 1 	|
| 9 	| 1 	| 9 	| be 	| 2 	|
| 9 	| 3 	| 15 	| be 	| 3 	|
| 9 	| 5 	| 9 	| ki 	| 2 	|
| 9 	| 8 	| 15 	| ki 	| 1 	|
| 9 	| 8 	| 20 	| be 	| 2 	|
| 9 	| 8 	| 26 	| be 	| 3 	|
| 9 	| 13 	| 4 	| be 	| 4 	|
| 9 	| 13 	| 26 	| ki 	| 3 	|
...

A fenti példában a szürke mintázatú részen a bemeneti fájl első néhány sora látható. A második sora azt mutatja, hogy a 9-es azonosítójú személy 9 óra 1 perckor lépett be a társalgóba. A negyedik sorban olvasható, hogy 9 óra 5 perckor már ki is ment, tehát ekkor összesen 4 percet töltött bent. A szürke rész sorai mellett olvasható számok azt mutatják, hogy a be- vagy kilépést követően hányan vannak bent a társalgóban. Ez a szám egy percen belül akár többször is változhat. 

Készítsen programot, amely az ajto.txt állomány adatait felhasználva az alábbi kérdésekre válaszol! A program forráskódját mentse tarsalgo néven! (A program megírásakor a felhasználó által megadott adatok helyességét, érvényességét nem kell ellenőriznie, feltételezheti, hogy a rendelkezésre álló adatok a leírtaknak megfelelnek.) 

A képernyőre írást igénylő részfeladatok eredményének megjelenítése előtt írja a képernyőre a feladat sorszámát (például: 4. feladat:)! Ha a felhasználótól kér be adatot, jelenítse meg a képernyőn, hogy milyen értéket vár! Az ékezetmentes kiírás is elfogadott. 

## Jó tanács

Célszerű egy feladatszám kiíró függvényt csinálni.

<details> 
<summary>
Megoldás 
</summary>

```python
def feledatszam(i): ## célszerű f-nek hívni az időtakarékosság jegyében
    print('{0}. feladat:',i)
```
<hr/>
</details>

## Feladatok

1. Olvassa be és tárolja el az ajto.txt fájl tartalmát!

<details> 
<summary>
Megoldás 
</summary>

`Egyszerűbb megoldás`
```python
inp = open('ajto.txt')
ajto = []
for line in inp.readlines():
    line = line.replace('\n', '')
    sor = line.split(' ')
    ajto.append([int(sor[0]), int(sor[1]), int(sor[2]), sor[3]])
print('%d sor beolvasva.' % len(ajto))
```

`Nehezebb, trükösebb megoldás`
```python
ajto = [line.replace('\n', '').split(' ') for line in open('ajto.txt').readlines()]
print('%d sor beolvasva.' % len(ajto))
```
<hr/>
</details>

2. Írja a képernyőre annak a személynek az azonosítóját, aki a vizsgált időszakon belül először lépett be az ajtón, és azét, aki utoljára távozott a megfigyelési időszakban!

<details> 
<summary>
Megoldás 
</summary>

```python
f(2)
print('Az első belépő: %d' % ajto[0][2])
i = len(ajto) - 1
while i >= 0 and ajto[i][3] != 'ki':
    i -= 1
if i >= 0:
    print('Az utolsó kilépő: %d' % ajto[i][2])
```

<hr/>
</details>

3. Határozza meg a fájlban szereplő személyek közül, ki hányszor haladt át a társalgó ajtaján! A meghatározott értékeket azonosító szerint növekvő sorrendben írja az athaladas.txt fájlba! Soronként egy személy azonosítója, és tőle egy szóközzel elválasztva az áthaladások száma szerepeljen! 

<details> 
<summary>
Megoldás 
</summary>


```python
azonositok = set()
for adat in ajto:
    azonositok.add(adat[2])
lista = sorted(list(azonositok))
athaladasok = [a[2] for a in ajto]
with open('athaladas.txt', 'w') as ath:
    for tag in lista:
        ath.write('%d %d\n' % (tag, athaladasok.count(tag)))
```

<hr/>
</details>

4. Írja a képernyőre azon személyek azonosítóját, akik a vizsgált időszak végén a társalgóban tartózkodtak! 

<summary>
Megoldás 
</summary>


```python
f(4)
bent = []
for tag in lista:
    athaladasok = [a[3] for a in ajto if a[2] == tag]
    if athaladasok[-1] == 'be':
        bent.append(str(tag))
print('A végén a társalgóban voltak: ' + ' '.join(bent))
```

<hr/>
</details>

5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot (óra:perc), amikor a legtöbben voltak bent! 

<summary>
Megoldás 
</summary>


```python
f(5)
max = 0
ido = ''
akt = 0
for adat in ajto:
    akt += (1 if adat[3] == 'be' else -1)
    if akt > max:
        max = akt
        ido = '%d:%d' %(adat[0], adat[1])
print('Például %s-kor voltak a legtöbben a társalgóban.' % ido)
```

<hr/>
</details>

5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot (óra:perc), amikor a legtöbben voltak bent! 

<summary>
Megoldás 
</summary>


```python
f(6)
ember = int(input('Adja meg a személy azonosítóját! '))
```
(elég idétlen feladat)

<hr/>
</details>

5. Hányan voltak legtöbben egyszerre a társalgóban? Írjon a képernyőre egy olyan időpontot (óra:perc), amikor a legtöbben voltak bent! 

<summary>
Megoldás 
</summary>


```python
f(5)
max = 0
ido = ''
akt = 0
for adat in ajto:
    akt += (1 if adat[3] == 'be' else -1)
    if akt > max:
        max = akt
        ido = '%d:%d' %(adat[0], adat[1])
print('Például %s-kor voltak a legtöbben a társalgóban.' % ido)
```

<hr/>
</details>