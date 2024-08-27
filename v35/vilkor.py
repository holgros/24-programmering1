# ett enkelt villkor med else-tillägg
a = -1
if a > 0:
   print("a är större än noll")
else:
   print("a är mindre än noll")

# ett annat exempel
e_gräns = 15
poäng = int(input('Ange din provpoäng -> '))
if poäng >= e_gräns:
   print("Godkänd!")            # Skriv endast ut om godkänd
print("Programmet avslutas")    # Skriv ut oavsett om godkänd eller ej

# jämförelseoperatorer
print(1 < 2)    # True (mindre än)
print(1 > 2)    # False (större än)
print(1 <= 2)   # True (mindre än eller lika med)
print(1 >= 2)   # False (större än eller lika med)
print(1 == 2)   # False (lika med - OBS: dubbelt likhetstecken)
print(1 != 2)   # True (skilt från)
a = 1
b = 2
if a < b:
   print("a är mindre än b")

# booleska variabler
my_boolean = True
if my_boolean:
   print("Den booleska variabeln är sann")
my_other_boolean = False
if not my_other_boolean:
   print("Den andra booleska variabeln är inte sann")

# booleska operatorer (and, or och not)
a = True
b = False
print(a and b)      # False (det är inte fallet att både a och b är sanna)
print(a or b)       # True (a eller b är sann, eftersom a är sann)
print(a or (a and not b))   # True (kontrollera själv varför!)

# Ett lite mer komplext program (se presentation)
tal = int(input('Ange valfritt heltal ->'))
if tal >= 0:            # om talet är större eller lika med noll
   if tal == 0:         # om talet dessutom är lika med noll
      print("Noll!")
   else:               # annars, dvs. om talet är större än noll
      print("Positivt!")
else:                  # annars, dvs. om talet är mindre än noll
   print("Negativt!")
print("Programmet avslutas")