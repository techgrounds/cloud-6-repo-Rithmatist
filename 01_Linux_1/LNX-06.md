# Bestandsrechten
Elk bestand in Linux bevat een reeks machtigingen. Er zijn aparte rechten voor het lezen, schrijven en uitvoeren van bestanden (rwx). Er zijn ook drie soorten entiteiten die verschillende machtigingen kunnen hebben: de eigenaar van het bestand, een groep en alle anderen. Root heeft geen rechten nodig om een bestand te lezen, te schrijven of uit te voeren.

U kunt de machtigingen van een bestand bekijken door een lange lijst te maken. De machtigingen van een bestand, evenals de eigenaar en groep, kunnen ook worden gewijzigd.
Elke gebruiker vermeld in /etc/passwd kan worden toegewezen als eigenaar van een bestand.
Elke groep in /etc/group kan worden toegewezen als de groep van een bestand.

## Key-terms
- touch =
- 

## Opdracht
- [Maak een tekstbestand.](#Maak-een-tekstbestand.)
- Maak een lange lijst om de machtigingen van het bestand te bekijken. Wie is de eigenaar en groep van het bestand? Welke machtigingen heeft het bestand?
- Maak het bestand uitvoerbaar door de uitvoermachtiging (x) toe te voegen.
- Verwijder de lees- en schrijfrechten (rw) uit het bestand voor de groep en alle anderen, maar niet voor de eigenaar. Kun je het nog lezen?
- Wijzig de eigenaar van het bestand in een andere gebruiker. Als alles goed is gegaan, zou je het bestand niet moeten kunnen lezen, tenzij je root-privileges aanneemt met 'sudo'.
- Wijzig het groepseigendom van het bestand in een andere groep.


### Gebruikte bronnen
[Linux File Permission Tutorial: How to Check and Change Permissions](https://phoenixnap.com/kb/linux-file-permissions)

### Ervaren problemen
geen.
### Resultaat

#### Maak een tekstbestand.

    `touch tekstbestand.txt`

    ![touch]()

- Maak een lange lijst om de machtigingen van het bestand te bekijken. Wie is de eigenaar en groep van het bestand? Welke machtigingen heeft het bestand?

    `ls -l tekstbestand.txt`
    
  ![ls]()

- Maak het bestand uitvoerbaar door de uitvoermachtiging (x) toe te voegen.
- Verwijder de lees- en schrijfrechten (rw) uit het bestand voor de groep en alle anderen, maar niet voor de eigenaar. Kun je het nog lezen?
- Wijzig de eigenaar van het bestand in een andere gebruiker. Als alles goed is gegaan, zou je het bestand niet moeten kunnen lezen, tenzij je root-privileges aanneemt met 'sudo'.
- Wijzig het groepseigendom van het bestand in een andere groep.
