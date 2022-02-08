# Data types and comments
Een computer kan achter de motorkap alleen reeksen nullen en enen waarnemen. Datatypes worden in programmeertalen gebruikt om de computer te leren hoe hij reeksen moet interpreteren.
Wanneer een computer bijvoorbeeld de binaire string 01000001 moet lezen, moet hij het gegevenstype kennen om te weten te komen of het 65 of "A" betekent.


## Key-terms
- **Boolean** = A Boolean value is either **true** or **false**.
- **string** = Values that are treated as text.
- **int** = Variables that must take an integer value.
- **float** = a variable that can hold a real number or a number with a decimal point.
- **comments** = Are  lines in the code that are ignored by the compiler during the execution of the program.
## Opdracht

### Oefening 1:
- Maak een nieuw script.
- Kopieer de onderstaande code in je script.

       a = "int
       b = 7
       c = False
       d = "18.5"

- Bepaal de datatypes van alle vier de variabelen (a, b, c, d) met behulp van een ingebouwde functie.
- Maak een nieuwe variabele x en geef deze de waarde b + d. Print de waarde van x. Dit zal een fout opleveren. Maak het zo dat ```print(x)``` een float afdrukt.
- Schrijf een commentaar boven elke regel code die de lezer vertelt wat er in je script gebeurt.

### Oefening 2:
- Maak een nieuw script.
- Gebruik de functie ```input()``` om input van de gebruiker te krijgen. Sla die input op in een variabele.
- Zoek uit welk gegevenstype de uitvoer van ```input()``` is. Kijk of het verschillend is voor verschillende soorten input (getallen, woorden, etc.).

### Gebruikte bronnen

### Ervaren problemen

#### Resultaat

#### Oefening 1: 

```Python
# The variable below has a string named 'int'.
a = 'int'
# With the in build function type() we can determine what type the variable 'a' has.
print(type(a))
# the variable named b has an integer 7 value.
b = 7
# With the in build function type() we can determine what type the variable 'b' has.
print(type(b))
# The variable 'c' is a Boolean.
c = False
# With the in build function type() we can determine what type the variable 'c' has.
print(type(c))
# In variable d we have a float value saved as a string.
d = "18.5"
# With the in build function type() we can determine what type the variable 'd' has.
print(type(d))
# varx sums up variable b with variable d only this will throw an error, so we transformed variable d in a float.
x = b + float(d)
# With the in build function type() we can determine what type the variable 'x' has.
print(type(x))
```

#### Oefening 2:

```Python
user_input = input("Type something:")

try:
    int(user_input)
    print("it's an integer!")
except ValueError:
    try:
        float(user_input)
        print("it's a float!")
    except ValueError:
        try:
            str(user_input)
            print("It's a string!")
        except ValueError:
            print("I do not know what this is.")
   ```