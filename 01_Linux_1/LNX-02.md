# Bestanden en mappen
Linux gebruikt bestanden en mappen, zoals je gewend bent met elk besturingssysteem dat je hebt gebruikt. Mappen in Linux worden mappen genoemd, dus gebruik dat woord bij het zoeken naar opdrachten of informatie.

Telkens wanneer u een terminal opent, begint u te werken vanuit uw thuismap. Van daaruit kunt u met slechts een paar commando's naar elke map in het hele systeem gaan.

Het Linux-bestandssysteem begint bij de hoofdmap, weergegeven door een schuine streep (/). Alle bestanden en mappen in Linux worden weergegeven door hun pad, beginnend bij root.

## Key-terms
- pwd = Werkmap weergeven
- dir = lijst van de inhoud van een map
- ls = lange lijst
- mkdir = map maken
- vi = visuele editor
- nano = teksteditor op de opdrachtregel
- cd = wijzig map

## Opdracht
- Ontdek uw huidige werkmap.
- Maak een lijst van alle bestanden en mappen in uw thuismap. U zou onder andere mappen als 'Desktop', 'Openbaar' en 'Afbeeldingen' moeten zien.
- Maak in je thuismap een nieuwe map met de naam 'techgrounds'.
- Maak in de techgrounds-directory een bestand met wat tekst.
- Beweeg door uw directorystructuur met zowel absolute als relatieve paden.

### Gebruikte bronnen
[Absolute and Relative Pathnames in UNIX](https://www.geeksforgeeks.org/absolute-relative-pathnames-unix/)

### Ervaren problemen
geen
### Resultaat
- *Ontdek uw huidige werkmap.*
 
    De `~` teken is uw 'home' werkmap, of gebruik `pwd` command om te zien wat de huidige werkmap is.
    
    ![pwd](https://raw.githubusercontent.com/Rithmatist/cloud-6-repo-Rithmatist/main/00_includes/pwd.JPG)
- *Maak een lijst van alle bestanden en mappen in uw thuismap. U zou onder andere mappen als 'Desktop', 'Openbaar' en 'Afbeeldingen' moeten zien.*

    Met de commando's `dir` en `ls` ziet u de andere mappen.
    
    ![dirls](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/dirls.JPG?raw=true)
- *Maak in je thuismap een nieuwe map met de naam 'techgrounds'.*

    `mkdir` gebruikt u om een nieuwe map aan te maken. 
    
    ![mkdir](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/mkdir.JPG?raw=true)
- *Maak in de techgrounds-directory een bestand met wat tekst.*

    Gebruik `cat /techgrounds/file.txt` of `touch /techgrounds/file.txt` om een bestand met wat tekst te maken.

- *Beweeg door uw directorystructuur met zowel absolute als relatieve paden*

    Om van de huidige werkmap naar de techgrounds folder te gaan kunnen we gebruik maken van `absolute` en `relatieve` paden.

- **Absolute path:**

    `cd /home/chris/techgrounds`
    

- **relative path:**

    `cd techgrounds`
    


