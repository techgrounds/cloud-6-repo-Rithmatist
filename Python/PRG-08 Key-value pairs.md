# Key-value pairs
U zult ongetwijfeld het concept van key-value pairs tegenkomen. NoSQL databases en AWS resource tags zijn twee voorbeelden van waar je ze kunt vinden. In Python gebruiken dictionaries (dict) key-value pairs om gegevens op te slaan.

Haakjes worden gebruikt om dicts in Python te schrijven. Door de sleutel van de dict aan te roepen, kun je er waarden uit halen.

## Key-terms

## Opdracht

## Oefening 1:
- Maak een nieuw script.
- Maak een woordenboek met de volgende sleutels en waarden:

| **key**    	| **value**      	|
|------------	|----------------	|
| First name 	| Coen           	|
| Last name  	| Meulenkamp     	|
| Job title  	| Learning Coach 	|
| Company    	| Techgrounds    	|

- Loop over het woordenboek en druk elk sleutel-waarde paar af in de terminal.


## Oefening 2:
- Maak een nieuw script.
- Gebruik gebruikersinvoer om naar hun informatie te vragen (voornaam, achternaam, functietitel, bedrijf). Sla de informatie op in een dictionary.
- Schrijf de informatie naar een csv-bestand (door komma's gescheiden waarden). De gegevens mogen niet worden overschreven als je het script meerdere keren uitvoert.
### Gebruikte bronnen

### Ervaren problemen

### Resultaat

#### Oefening 1:

```python
Dict = {"First name": "Coen", "Last name": "Meulenkamp", "Job title": "Learning Coach", "Company": "TechGrounds"}

for i in Dict.items():
    print(i)
```

#### Oefening 2:

```python
import pandas as pd
import os.path

info = {}
df = pd.DataFrame()


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif type(dictionary[key]) == list:
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


while True:
    q1 = input("First name?")
    set_key(info, "First name", q1)
    q2 = input("Last name?")
    set_key(info, "Last name", q2)
    q3 = input("Job title?")
    set_key(info, "Job title", q3)
    q4 = input("Company?")
    set_key(info, "Company", q4)
    break

info = pd.DataFrame.from_dict(info, orient='index').transpose()
df = pd.concat([df, info])

if not os.path.isfile('oefening.csv'):
    df.to_csv('oefening.csv', index=False)
else:
    df.to_csv('oefening.csv', mode='a', header=None, index=False)

```