# Gyorstalpaló Python nyelvből

## Kiiratás

```Python
print("Helló, világ!")
```

## Beolvasás

```Python
nev = input("Hogy hívnak? ")
print("Szia,", nev)
```
### Szám beolvasás

```Python
b = int(input("b?"))
```

## Teszteljük az eddigieket

```Python
import math
 
print("Mennyi a kör sugara?")
sugar = float(input())
 
print("Kerület =", 2 * sugar * math.pi)
print("Terület =", sugar**2 * math.pi)
```


## While 
```Python
   print("Meddig írjam ki?")   
   n = int(input())   

   x = 1   
   while x <= n:   
       print(x, end=" ")   
       x = x+1   

   print(".")
```
