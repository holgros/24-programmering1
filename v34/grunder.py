# En kommentar börjar med hashtag, ignoreras av programmet

# Aritmetik
print(2+3)      # addition
print(3-2)      # subtraktion
print(3*2)      # multiplikation
print(3/2)      # division
print(37//6)    # heltalsdivision
print(37%6)     # restdivision

# Variabler
x = 10
print(x)        # 10
x = 10+1
print(x)        # 11
x = x+1
print(x)        # 12
my_decimal_number = 1.5
my_string = "Detta är en textsträng"
my_boolean = True
# variabler kan vara av olika typer, t.ex. heltal, decimaltal, text (strängar) eller logiska värden (boolean)

# Python är "dynamiskt typat", dvs. en och samma variabel kan byta typ under programmets gång
# Man kan ta reda på vilken typ en variabel är med hjälp av funktionen type
x = 2           # ett heltal
print(type(x))  # <class 'int'>
x = "text"      # en textsträng
print(type(x))  # <class 'str'>

# Konvertering av datatyper
x = "1"         # x är en textsträng
y = "2"         # y är en textsträng
print(x+y)      # "12", alltså "1" + "2"
x = int(x)      # konvertera x till ett heltal
y = int(y)      # dito y
print(x+y)      # 3, alltså 1 + 2

# Skriv ut flera textsträngar på samma gång
name = "Holger"
print("Hej, jag heter " + name)

# Läs in från tangentbordet och skriv ut ett svar
namn = input("Vad heter du?")
print("Hej " + namn + ", trevligt att råkas!")
