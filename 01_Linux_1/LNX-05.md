# Gebruikers en groepen
Linux heeft gebruikers, vergelijkbaar met accounts op Windows en MacOS. Elke gebruiker heeft zijn eigen homedirectory. Gebruikers kunnen ook deel uitmaken van groepen.
Er is een speciale gebruiker genaamd 'root'. Root mag alles doen.
Om tijdelijke root-rechten te krijgen, kun je 'sudo' typen voor een opdracht, maar dat werkt alleen als je dat mag doen.

## Key-terms
- adduser = Om een nieuwe gebruiker toe te voegen
- usermod = Om een gebruiker aan een groep toe te voegen
- sudo = Staat reguliere gebruikers toe om programma's uit te voeren met de beveiligingsrechten van de superuser of root

## Opdracht
- Maak een nieuwe gebruiker in uw virtuele machine.
  - De nieuwe gebruiker moet deel uitmaken van een beheerdersgroep die ook de gebruiker bevat die u tijdens de installatie hebt gemaakt.
  - De nieuwe gebruiker moet een wachtwoord hebben.
  - De nieuwe gebruiker moet 'sudo' kunnen gebruiken
- Zoek de bestanden waarin gebruikers, wachtwoorden en groepen zijn opgeslagen. Kijk of u de gegevens van uw nieuw aangemaakte gebruiker daar kunt vinden. 

### Gebruikte bronnen
[How To Add User To Sudoers & Add User To Sudo Group on Ubuntu](https://phoenixnap.com/kb/how-to-create-sudo-user-on-ubuntu)

### Ervaren problemen
Geen.

### Resultaat
- Maak een nieuwe gebruiker in uw virtuele machine.

  `sudo adduser test`

  ![adduser](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/adduser.JPG?raw=true)

  - De nieuwe gebruiker moet deel uitmaken van een beheerdersgroep die ook de gebruiker bevat die u tijdens de installatie hebt gemaakt.
  - 
    `groups test`
  
    ![groups](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/group.JPG?raw=true)
  
  - De nieuwe gebruiker moet een wachtwoord hebben.
  
    ![password](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/password.JPG?raw=true)
  - De nieuwe gebruiker moet 'sudo' kunnen gebruiken
  
    `sudo usermod -aG sudo test`
    
    ![usermod](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/usermod.JPG?raw=true)
- Zoek de bestanden waarin gebruikers, wachtwoorden en groepen zijn opgeslagen. Kijk of u de gegevens van uw nieuw aangemaakte gebruiker daar kunt vinden. 
  
  `cd /`

  `cat /ect/passwd`

  ![catpasswd](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/catpasswd.JPG?raw=true)
  
  Gebruiker gevonden:
  
  ![usertest](https://github.com/Rithmatist/cloud-6-repo-Rithmatist/blob/main/00_includes/usertest.JPG?raw=true)
