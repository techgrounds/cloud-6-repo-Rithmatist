# Bestandsrechten
Elk bestand in Linux bevat een reeks machtigingen. Er zijn aparte rechten voor het lezen, schrijven en uitvoeren van bestanden (rwx). Er zijn ook drie soorten entiteiten die verschillende machtigingen kunnen hebben: de eigenaar van het bestand, een groep en alle anderen. Root heeft geen rechten nodig om een bestand te lezen, te schrijven of uit te voeren.

U kunt de machtigingen van een bestand bekijken door een lange lijst te maken. De machtigingen van een bestand, evenals de eigenaar en groep, kunnen ook worden gewijzigd.
Elke gebruiker vermeld in /etc/passwd kan worden toegewezen als eigenaar van een bestand.
Elke groep in /etc/group kan worden toegewezen als de groep van een bestand.

## Key-terms
- touch = a standard command used in Linux operating system which is used to __create, change and modify timestamps of a file.__
- chmod = change mode (permissions)
- chown = change owner
- ls = long listing

## Opdracht
- [Maak een tekstbestand.](#maak-een-tekstbestand)
- [Maak een lange lijst om de machtigingen van het bestand te bekijken. Wie is de eigenaar en groep van het bestand? Welke machtigingen heeft het bestand?](#maak-een-lange-lijst-om-de-machtigingen-van-het-bestand-te-bekijken-wie-is-de-eigenaar-en-groep-van-het-bestand-welke-machtigingen-heeft-het-bestand)
- [Maak het bestand uitvoerbaar door de uitvoermachtiging (x) toe te voegen.](#maak-het-bestand-uitvoerbaar-door-de-uitvoermachtiging-x-toe-te-voegen)
- [Verwijder de lees- en schrijfrechten (rw) uit het bestand voor de groep en alle anderen, maar niet voor de eigenaar. Kun je het nog lezen?](#verwijder-de-lees--en-schrijfrechten-rw-uit-het-bestand-voor-de-groep-en-alle-anderen-maar-niet-voor-de-eigenaar-kun-je-het-nog-lezen)
- [Wijzig de eigenaar van het bestand in een andere gebruiker. Als alles goed is gegaan, zou je het bestand niet moeten kunnen lezen, tenzij je root-privileges aanneemt met 'sudo'.](#wijzig-de-eigenaar-van-het-bestand-in-een-andere-gebruiker-als-alles-goed-is-gegaan-zou-je-het-bestand-niet-moeten-kunnen-lezen-tenzij-je-root-privileges-aanneemt-met-sudo)
- [Wijzig het groepseigendom van het bestand in een andere groep.](#wijzig-het-groepseigendom-van-het-bestand-in-een-andere-groep)


### Gebruikte bronnen

- [Linux File Permission Tutorial: How to Check and Change Permissions](https://phoenixnap.com/kb/linux-file-permissions)
- [How to Use the chmod Command on Linux](https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/)
- [Chown Command in Linux (File Ownership)](https://linuxize.com/post/linux-chown-command/)

### Ervaren problemen
geen.
### Resultaat

##### Maak een tekstbestand.

`touch tekstbestand.txt`

![touch](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/touch.JPG?raw=true)


##### Maak een lange lijst om de machtigingen van het bestand te bekijken. Wie is de eigenaar en groep van het bestand? Welke machtigingen heeft het bestand?

`ls -l tekstbestand.txt`
    
![ls](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/ls.JPG?raw=true)

##### Maak het bestand uitvoerbaar door de uitvoermachtiging (x) toe te voegen.
`chmod a+x tekstbestand.txt`

![chmodx](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/chmodx.JPG?raw=true)

##### Verwijder de lees- en schrijfrechten (rw) uit het bestand voor de groep en alle anderen, maar niet voor de eigenaar. Kun je het nog lezen?
`chmod go-rw tekstbestand.txt`

![chmodgo-rw](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/chmodgo-rw.JPG)

##### Wijzig de eigenaar van het bestand in een andere gebruiker. Als alles goed is gegaan, zou je het bestand niet moeten kunnen lezen, tenzij je root-privileges aanneemt met 'sudo'.
`sudo chown test tekstbestand.txt`

![chown-denied](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/chown-denied.JPG)

##### Wijzig het groepseigendom van het bestand in een andere groep.
`sudo chown :test tekstbestand.txt`

![chowngroup](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/chowngroup.JPG)
