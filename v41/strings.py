# Sträng jämfört med listor
my_string = "Hello, world"
print(f"Strängkonstanten är: {my_string}")
print(f"Strängkonstantens första tecken är: {my_string[0]}")
print(f"Tecknet \"o\" finns första gången på index: {my_string.index('o')}")

# Delsträngar
my_str = "Detta är en sträng som består av 42 tecken"
print(my_str[:8])
print(my_str[19:29])
print(my_str[33:])

# Loopa genom strängar
vowels = "aeiouyåäö"
chars = "Hello, world"
for char in chars:
    if char.lower() in vowels:
        print(char, end="")
    else:
        print("*", end="")

# Skapa en ny sträng utifrån ett original
vowels = "aeiouyåäö"
source = "Hello, world"
destination = ""
for char in source:
    if char.lower() in vowels:
        destination += char
    else:
        destination += "*"
print(destination)

# Fejka förändring
my_str = "Detta är en sträng som består av 42 tecken"
my_upper_str = my_str.upper()
print(my_str)
print(my_upper_str)
