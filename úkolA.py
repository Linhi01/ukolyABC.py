print("zadej tři jídla, která jsi během dne snědl")
jidlo1 = input()
jidlo2 = input()
jidlo3 = input()

print("zadej odhad počtu kalorií v každém jídle")
kalorie1 = int(input())
kalorie2 = int(input())
kalorie3 = int(input())
celkove_kalorie = (kalorie1 + kalorie2 + kalorie3)

print (f"celkem je to {celkove_kalorie} kalorií")
