# Werken met tekst (CLI)
Elke opdracht in Linux heeft een standaard invoer en uitvoer.
De standaard invoer (stdin) is het toetsenbord. Als ik 'mkdir myfolder' uitvoer, weet het mkdir-commando welke map moet worden gemaakt, omdat ik 'myfolder' heb getypt.
De standaarduitgang (stdout) is de terminal. Het commando 'echo hallo' zal 'hallo' in de terminal schrijven.

Zowel de invoer als de uitvoer kunnen worden omgeleid naar een bestand in plaats van de standaard. Dit wordt invoeromleiding en uitvoeromleiding genoemd.
Een pipe kan worden gebruikt om de uitvoer van een commando de invoer van een ander commando te laten zijn.
## Key-terms
- “>” = operator voor het overschrijven van een reeds bestaand bestand of een nieuw bestand
- ">>" = operator voegt een reeds aanwezig bestand toe of maakt een nieuw bestand aan
- cli = opdrachtregelinterface
- kat = samenvoegen
- echo = toon regel tekst/tekenreeks die als argument is doorgegeven
- grep = Globaal zoeken naar een reguliere expressie
- ack = Ack is ontworpen als vervanging voor 99% van het gebruik van grep
## Opdracht
- Gebruik de echo-opdracht en uitvoeromleiding om een nieuwe zin in uw tekstbestand te schrijven met behulp van de opdrachtregel. De nieuwe zin moet het woord ‘techgrounds’ bevatten.
- Gebruik een opdracht om de inhoud van uw tekstbestand naar de terminal te schrijven. Maak gebruik van een commando om de output te filteren zodat alleen de zin met ‘techgrounds’ verschijnt.
- Lees je tekstbestand met het commando dat in de tweede stap is gebruikt, opnieuw filterend op het woord 'techgrounds'. Leid deze keer de uitvoer om naar een nieuw bestand met de naam 'techgrounds.txt'.
### Gebruikte bronnen
[ack - Documentation](https://beyondgrep.com/documentation/)

### Ervaren problemen
geen, Ik moest alleen nog de package ack installeren met `sudo apt-get install ack`.

### Resultaat
- *Gebruik de echo-opdracht en uitvoeromleiding om een nieuwe zin in uw tekstbestand te schrijven met behulp van de opdrachtregel. De nieuwe zin moet het woord ‘techgrounds’ bevatten.*
    
    Met `echo "techgrounds" >> atekstfile.txt"` Appenden we het woord techgrounds in de tekstbestand.
    
    ![echo](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/echo.JPG?raw=true)    

- *Gebruik een opdracht om de inhoud van uw tekstbestand naar de terminal te schrijven. Maak gebruik van een commando om de output te filteren zodat alleen de zin met ‘techgrounds’ verschijnt.*

    U kunt met `ack 'techgrounds' atekstfile.txt` de inhoud van een tekstbestand weergeven en controleren of het bestaat.
    
    ![ack](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/ack.JPG?raw=true)

- *Lees je tekstbestand met het commando dat in de tweede stap is gebruikt, opnieuw filterend op het woord 'techgrounds'. Leid deze keer de uitvoer om naar een nieuw bestand met de naam 'techgrounds.txt'.*

    Hiervoor gebruiken we de gedeeltelijk commando van de tweede opdracht `ack 'techgrounds' atekstfile.txt > techgrounds.txt` om de output op te slaan in techgrounds.txt.
    
    ![ackout](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/ackout.JPG?raw=true)
