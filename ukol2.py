print ("napiš desetiné číslo")
cislo1 = int(input())
print ("napiš znaménko")
znamenko = input()
print ("napiš druhé desetiné číslo")
cislo2 = int(input())

soucet = (cislo1 + cislo2)
rozdil = (cislo1 - cislo2)
soucin = (cislo1 * cislo2)
podil = (cislo1 / cislo2)

vysledek = soucet or rozdil or soucin or podil
print (vysledek)
