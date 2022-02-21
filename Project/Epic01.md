# Epic 01
## Als team willen wij duidelijk hebben wat de eisen zijn van de applicaties

| Item | Opmerking |
| ---- | --------- |
| Kenmerk | Exploratie |
| Omschrijving | Je hebt al heel wat informatie gekregen. Mogelijk zijn er vragen die geen van de stakeholders heeft kunnen beantwoorden. Je team moet een overzicht kunnen produceren van de aannames die je daardoor maakt. |
| Doel | Een puntsgewijze overzicht van alle aannames |
| Team problem | Projectdocument is op een aantal punten niet duidelijk | 
| Team value | A.d.h.v. het vragen document duidelijkheid krijgen over de eisen |
| Aannames | De product Owner heeft antwoord op alle vragen |
| Doen we niet | Alvast antwoorden invullen bij de vragen |
| Acceptatie criteria | De Product Owner heeft alle vragen naar onze tevredenheid beantwoord |

## Vragen document met de antwoorden
OP 10 februari 2022, hebben wij het gesprek gehad met de Product Owner. In het document [Project Cloud6.Sentia1](https://docs.google.com/document/d/1pNPWIce4kDnR9kopbH4t7jD9nX6LFySnBpsTfaWT_r4/edit#heading=h.higkk7mphvwd) staan alle vragen inclusief de antwoorden die wij hebben gekregen.

## Opsomming van de Eisen
- VM disks worden ge-encrypt (AWS KMS)
- Gebruik CDK
- Webserver: dagelijkse backup (7 dagen behouden)(AWs Backup)
- Webserver: extern toegankelijk via HTTP/HTTPS
- Webserver: geautomatiseerd geïnstalleerd (maak gebruik van User Data)
- Webserver: SSH toegang alleen via de Admin/Management server
- Admin/Management server: bereikbaar via Public IP
- Admin/Management server: alleen bereikbaar vanaf vertrouwde locaties (Development Team) (Network ACL of GuardDuty)
- IP ranges: 10.10.10.0/24 en 10.20.20.0/24
- Subnets: firewalls op subnet niveau (Network ACL)
- S3 bucket via de Admin/managment server
- Lege Availablity Zone is voor de failover (autoscaling)
- Scrum master meeting dagelijks om 15:30 uur
