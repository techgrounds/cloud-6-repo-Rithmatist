# LNX-04 Working with text (CLI)

## Oefeningen:
- *Gebruik de echo-opdracht en uitvoeromleiding om een nieuwe zin in uw tekstbestand te schrijven met behulp van de opdrachtregel. De nieuwe zin moet het woord ‘techgrounds’ bevatten.*
    
    Met `echo "techgrounds" >> atekstfile.txt"` Appenden we het woord techgrounds in de tekstbestand.
    
    ![echo](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/echo.JPG?raw=true)    

- *Gebruik een opdracht om de inhoud van uw tekstbestand naar de terminal te schrijven. Maak gebruik van een commando om de output te filteren zodat alleen de zin met ‘techgrounds’ verschijnt.*

    U kunt met `ack 'techgrounds' atekstfile.txt` de inhoud van een tekstbestand weergeven en controleren of het bestaat.
    
    ![ack](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/ack.JPG?raw=true)

- *Lees je tekstbestand met het commando dat in de tweede stap is gebruikt, opnieuw filterend op het woord 'techgrounds'. Leid deze keer de uitvoer om naar een nieuw bestand met de naam 'techgrounds.txt'.*

    Hiervoor gebruiken we de gedeeltelijk commando van de tweede opdracht `ack 'techgrounds' atekstfile.txt > techgrounds.txt` om de output op te slaan in techgrounds.txt.
    
    ![ackout](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/ackout.JPG?raw=true)
