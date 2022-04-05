# Epic Document

## Inhoud
- [Wat zijn de eisen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#wat-zijn-de-eisen-epic---01)
- [Een duidelijk overzicht van de aannames](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-aannames-epic---02)
- [Een duidelijk overzicht van de Cloud Infrastructuur](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-cloud-infrastructuur-epic---03)
- [Klant wil een veilig netwerk deployen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-een-veilig-netwerk-deployen-epic---04)
- [Klant wil een werkende webserver deployen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-een-werkende-webserver-deployen-epic---05)
- [Klant wil een werkende management server deployen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-een-werkende-management-server-deployen-epic---06)
- [Klant wil opslagoplossing voor bootstrapscript(s)](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-opslagoplossing-voor-bootstrapscripts-epic---07)
- [Klant wil alle data versleuteld hebben](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-alle-data-versleuteld-hebben-epic---08)
- [Klant wil iedere dag een backup, met bewaartermijn van 7 dagen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-iedere-dag-een-backup-met-bewaartermijn-van-7-dagen-epic---09)
- [Klant wil weten hoe hij/zij de applicatie kan gebruiken](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-weten-hoe-hijzij-de-applicatie-kan-gebruiken-epic---10)
- [Klant wil de MVP kunnen deployen om te testen](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#klant-wil-de-mvp-kunnen-deployen-om-te-testen-epic---11)
- [MPV v1.1 n.a.v. aanpassingen/aanvullingen van de klant]()

## Wat zijn de eisen (Epic - 01)
| Item                | Opmerking                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | Exploratie                                                                                                                                                                                                   |
| Omschrijving        | Je hebt al heel wat informatie gekregen. Mogelijk zijn er vragen die geen van de stakeholders heeft kunnen beantwoorden. Je team moet een overzicht kunnen produceren van de aannames die je daardoor maakt. |
| Doel                | Een overzicht van alle eisen                                                                                                                                                                    |
| Team problem        | Projectdocument is op een aantal punten niet duidelijk                                                                                                                                                       |
| Team value          | Meer duidelijkheid krijgen over bepaalde eisen                                                                                                                                             |
| Aannames            | Meer duidelijkheid                                                                                                                                                         |
| Doen we niet        | n.v.t                                                                                                                                                                 |
| Acceptatie criteria | De Product Owner heeft al onze vragen duidelijk beantwoord                                                                                                                                      |

### Vragen document met de antwoorden
Wij hebben meerdere gesprekken gehad met de Product Owner. In het document [Project Cloud6.Sentia1](https://docs.google.com/document/d/1pNPWIce4kDnR9kopbH4t7jD9nX6LFySnBpsTfaWT_r4/edit#heading=h.higkk7mphvwd) staan alle vragen inclusief de antwoorden die wij hebben gekregen, van het gesprek van 10 februari jl. De besluitenlijst is tot stand gekomen aan de hand van de antwoorden en toevoegingen van de Product Owner.

### Opsomming van de Eisen en Besluiten
| Eisen                                                                  |
| :--------------------------------------------------------------------- |
| VM disks worden ge-encrypt                                             |
| Gebruik CDK/Python                                                     |
| Webserver: dagelijkse backup (7 dagen behouden)                        |
| Webserver: extern toegankelijk voor publiek via HTTP/HTTPS             |
| Webserver: geautomatiseerd geïnstalleerd                               |
| Admin/Management server: bereikbaar via Public IP                      |
| Admin/Management server: alleen bereikbaar vanaf vertrouwde locaties   |
| Webserver alleen te bereiken vanaf Admin/Management Server via SSH/RDP |
| IP ranges: 10.10.10.0/24 en 10.20.20.0/24                              |
| Subnets: firewalls op subnet niveau                                    |

| Besluiten                                                                      |
| :----------------------------------------------------------------------------- |
| Webserver: Linux VM                                                            |
| Admin/Management server: Windows Server VM                                     |
| Lege Availablity Zone is voor de failover                                      |
| Trusted resources = AWS Team                                                   |
| Admin/Management server meenemen in de backup cyclus (1x per week/ 1 behouden) |
| testomgeving is separate omgeving. Parameterfile gebruiken!                    |
| Documentatie wordt geschreven voor een Engineer                                |

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Een duidelijk overzicht van de aannames (Epic - 02)
| Item                | Opmerking                                                                                                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | Exploratie                                                                                                                                                                                                                                              |
| Omschrijving        | Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten                                      |
| Doel                | Een puntsgewijze overzicht van alle aannames                                                                                                                                                                                                            |
| Team problem        | Product Owner heeft, tijdens het eerste gesprek, bij een aantal vragen aangegeven dat van ons het antwoord/advies wordt verwacht. Er zijn meerdere gesprekken geweest met de Product Owner. Daardoor zijn alle aannames inmiddels omgezet in besluiten. |
| Team value          | Overzicht van de aannames per Epic                                                                                                                                                                                                                      |
| Aannames            | geen aannames                                                                                                                                                                                                                                           |
| Doen we niet        | Alles wat buiten de scope van het project document en PRD ligt                                                                                                                                                                                          |
| Acceptatie criteria | Als er bij de Epics aannames zijn benoemd of is aangegven dat ze er niet zijn                                                                                                                                                                           |

| Epic no.                                                                                                                                                                                                    | Aannames                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [03]([../Project/Epic03.md](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#een-duidelijk-overzicht-van-de-cloud-infrastructuur-epic---03))           | Aanname: Project document is incompleet. |

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Een duidelijk overzicht van de Cloud Infrastructuur (Epic - 03)
| Item                | Opmerking                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | Exploratie                                                                                                                                                                                                         |
| Omschrijving        | Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten |
| Doel                | Een overzicht van alle diensten die gebruikt gaan worden.                                                                                                                                                          |
| Team problem        | Niet alle AWS diensten zijn benoemd in het Project Document                                                                                                                                           |
| Team value          | Overzicht van de AWS diensten die we gaan gebruiken                                                                                                                                                             |
| Aannames            | Het Project document is niet compleet                                                                                                                                                        |
| Doen we niet        | n.v.t                                                                                                                       |
| Acceptatie criteria | Overzicht van de gebruikte AWS diensten                                                                                                                                                                         |

### Overzicht AWS diensten
* S3 (bucket t.b.v. bootstrap scripts)
* EC2 (webserver/management server, AMI, Snapshots)
* VPC (Subnets, peering, Security Groups)
* KMS
* IAM (users, roles, policies)
* AWS Backup
* Cloudformation (stacks)
* Lambda
* Secrets Manager

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)

## Klant wil een veilig netwerk deployen (epic - 04)
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen. |
| Doel                | een beveiligd netwerk                                                                                                                                       |
| User problem        | Alleen trusted sources (IP Adressen) mogen de management server benaderen                                                                                                            |
| User value          | Afschermen van ongewenst verkeer naar de Admin/Management server                                                                                                                     |
| Aannames            | Alleen verbindingen via trusted sources.                                                                                                                                              |
| Doen we niet        | n.v.t                                                              |
| Acceptatie criteria | Als alles werkt.                                                                                    |

###  veilig netwerk 
Management-server is alleen toegankelijk via trusted sources.

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil een werkende webserver deployen (Epic - 05)
| Item                | Opmerking                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                      |
| Omschrijving        | De applicatie moet een webserver starten en deze beschikbaar maken voor algemeen publiek. |
| Doel                | een webserver                                         |
| User problem        | Er moet een webserver komen                                                               |
| User value          | Een webserver met een public ip address                       |
| Aannames            | geen aannames                                                                             |
| Doen we niet        | Een complete website bouwen.                              |
| Acceptatie criteria | Als de website toegankelijk is van buitenaf.                                                    |

###  webserver 
Webserver is bereikbaar met een public ip address.

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil een werkende management server deployen (epic - 06)
| Item                | Opmerking                                                                                            |
| ------------------- | ---------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                 |
| Omschrijving        | De applicatie moet een management server starten en deze beschikbaar maken voor een beperkt publiek. |
| Doel                | een management server                                        |
| User problem        | Admin/Management server met beperkte toegang                                                         |
| User value          | Een Admin/Management server die "restricted" is                                          |
| Aannames            | Geen aannames                                   |
| Doen we niet        | n.v.t                                                   |
| Acceptatie criteria | Als toegang naar de Management server restricted is.                            |

### management-server
Management-server is alleen toegankelijk voor de benodigde gebruikers.

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil opslagoplossing voor bootstrapscript(s) (epic - 07)
| Item                | Opmerking                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                    |
| Omschrijving        | Er moet een locatie beschikbaar zijn waar bootstrap scripts beschikbaar worden. Deze script moeten niet publiekelijk toegankelijk zijn. |
| Doel                | een opslagplaats voor scripts                                                                                          |
| User problem        | Scripts die de klant wil gaan gebruiken moeten veilig opgeslagen worden                                                                 |
| User value          | Scripts opslaan in een veilige omgeving.                                                                      |
| Aannames            | S3 bucket wordt gebruikt met versioning en encryptie                                                                                    |
| Doen we niet        | n.v.t                                                                            |
| Acceptatie criteria | Als de bootstrap scripts in de s3 Bucket niet toegankelijk is voor public                                                                           |

### Bootstrap-script-opslag
Bootstrap scripts worden opgeslagen in een s3 bucket met kms managed encryptie.

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil alle data versleuteld hebben (epic - 08)
| Item                | Opmerking                                                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                                            |
| Omschrijving        | Er wordt veel gehecht aan de veiligheid van de data at rest en in motion. Alle data moet versleuteld zijn met een encryptie sleutel in het beheer van de klant. |
| Doel                | versleuteling aka "encryption everywhere!"                                                                                                                      |
| User problem        | Data moet versleuteld worden, zowel in Rest als in Motion                                                                                                       |
| User value          | Als de data versleuteld is, is dat veiliger                                                                                                                     |
| Aannames            | Geen aannames                                                                                                                                                   |
| Doen we niet        | n.v.t                                                                                                                                           |
| Acceptatie criteria | Als alles versleuteld is                                                                                                           |

### Encryptie
De versleutelde sleutels zijn terug te vinden in de KMS en de Secrets Manager.  

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil iedere dag een backup, met bewaartermijn van 7 dagen (Epic - 09)
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De klant wil graag dat er een backup beschikbaar is, mocht het nodig zijn om de servers terug te brengen naar een eerdere staat. (Zorg ervoor dat de Backup ook daadwerkelijk werkt) |
| Doel                | backups!                                                                                                                                                 |
| User problem        | Elke dag een backup van de webserver                                                                                                                                                 |
| User value          | Indien er iets fout gaat, dan heb je nog een backup                                                                                                 |
| Aannames            | ook voor de management server backups maken (1x per week, 1 behouden)                                                                                                    |
| Doen we niet        | Snapshots                                                                                                                                                                            |
| Acceptatie criteria | Als het werkt.
### Backup
Voor zowel de Webserver en de Management-server is er een Backup dienst aangemaakt.

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil weten hoe hij/zij de applicatie kan gebruiken (Epic - 10)

| Item                | Opmerking                                                                                                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                                         |
| Omschrijving        | Zorg dat de klant kan begrijpen hoe deze de applicatie kan gebruiken. Zorg dat het duidelijk is wat de klant moet configureren voor de deployment kan starten en welke argumenten het programma nodig heeft. |
| Doel                | Documentatie voor het gebruik van de applicatie                                                                                                                                                              |
| User problem        | Heeft geen idee hoe het allemaal werkt                                                                                                                                                                             |
| User value          | Handleiding met Jip en Janneke taal                                                                                                                                                                     |
| Aannames            | User weet niets                                                                                                                                                                                              |
| Doen we niet        | ELI5                                                                                                                                                                        |
| Acceptatie criteria | Als de user het zelf kan deployen                                                                                                                                                        |

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## Klant wil de MVP kunnen deployen om te testen (Epic - 11)
| Item                | Opmerking                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                                                                   |
| Omschrijving        | De klant wilt zelf intern je architectuur testen voordat ze de code gaan gebruiken in productie. Zorg ervoor dat er configuratie beschikbaar is waarmee de klant een MVP kan deployen. |
| Doel                | Configuratie voor een MVP deployment                                                                                                                                                   |
| User problem        | User wil zelf testen                                                                                                                                               |
| User value          | User wilt dat het allemaal werkt in een test omgeving                                                                                                                                  |
| Aannames            | Wij maken gaan parameters maken                                                                                                                          |
| Doen we niet        | test omgeving inrichten                                                                                                                                     |
| Acceptatie criteria | Als de user aangeeft dat het werkt                                                                                                                            |

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)
## MPV v1.1 aanpassingen/aanvullingen van de klant
**Doel:**  

   | Item       | Opmerking                                                                                          |
   | ---------- | -------------------------------------------------------------------------------------------------- |
   | Visie      | MPV v1.1 aanpassingen/aanvullingen van de klant                                             |
   | Doelen     | Opleveren van een werkende MVP v1.1 script. |
   | Persona(s) | Product Owner, DevOps Team                                                                         |

**Releases:**

   | Item             | Opmerking                                             |
   | ---------------- | ----------------------------------------------------- |
   | Release          | MVP v1.1                                              |
   | Datum            | 08-04-2022                                            |
   | Initiatief       | Aanpassingen/aanvullingen op MVP v1.0                 |
   | Mijlpalen        | 25-03-2022 Tussentijdse voortgangsrapportage MVP v1.1 |
   |                  | 08-04-2022 MVP v1.1 opgeleverd     |
   | Kenmerken        | Aanpassingen zijn vooral gericht op de Webserver omgeving       |
   | Afhankelijkheden | IaC, Python, AWs CDK, eisen Product Owner             |

[naar boven](https://github.com/techgrounds/cloud-6-repo-Rithmatist/blob/main/Project/Epic%20Document.md#inhoud)

**Diagram:**

![mvp1.1](../00_includes/finalversion.JPG)