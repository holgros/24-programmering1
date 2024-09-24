# ENKEL FUNKTION SOM ADDERAR TVÅ TAL
def add(a, b):     # Här
  the_sum = a + b  # skapas
  return the_sum   # funktionen
# Huvudprogram nedan
tal_1 = 10
tal_2 = 20
summa = add(tal_1, tal_2) # Här anropas funktionen
print("Summan av", tal_1, "och", tal_2, "är", summa)
# print(the_sum) # ger felmeddelande eftersom the_sum endast är synlig inuti funktionen

# FUNKTION UTAN RETURVÄRDE
def print_multabell(n):
  # Skriver ut fem rader i multiplikationstabell n
  for i in range(1, 6):
    print(f"{i:2.0f} * {n} = {i*n:3.0f}")
print_multabell(12) # Ange önskad tabell att skriva ut här
print_multabell(5)
print_multabell(17)
print(print_multabell(12)) # None (implicit returvärde)

# EN FUNKTION AVSLUTAS NÄR DEN KOMMER TILL ETT RETURN-STATEMENT
def maximum(a, b):
  '''
  Funktionen returnerar det största av två tal
  Parameter 1: a | ett tal (int eller float)
  Parameter 2: b | ett tal (int eller float)
  Returvärde: Det största av talen. Vid likhet returneras None.
  '''

  if a > b:
    return a
    print("Funktionen kommer inte hit!")
  elif b > a:
    return b
    print("Funktionen kommer inte hit!")
  return None # Onödig rad, utan return-sats returneras None ändå
max = maximum(1, 3)   # Anropar funktionen
print(max)