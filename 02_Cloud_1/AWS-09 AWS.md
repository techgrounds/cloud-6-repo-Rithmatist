# Beveiligingsgroepen
Beveiligingsgroepen zijn stateful virtuele firewalls die aan instanties kunnen worden toegewezen. Ze draaien niet in het besturingssysteem, maar in de VPC.

Eén beveiligingsgroep kan aan meerdere instanties worden toegewezen. Omgekeerd kan één instantie maximaal 5 beveiligingsgroepen hebben.

Beveiligingsgroepen hebben alleen regels voor toestaan. Alles wat niet expliciet is toegestaan, wordt automatisch impliciet geweigerd.

Een Network Access Control List (NACL) is een stateless firewall die op subnetniveau in een VPC draait.
Een NACL heeft zowel expliciete regels voor toestaan als weigeren. Aan regels is een nummer toegewezen. Dit nummer geeft de volgorde aan waarin de regels worden toegepast.

Standaard is een NACL geconfigureerd om al het verkeer in en uit het netwerk toe te staan.
## Key-terms

## Opdracht
#### bestudeer:
- Beveiligingsgroepen in AWS
- Netwerktoegangscontrolelijsten in AWS
### Gebruikte bronnen

### Ervaren problemen

### Resultaat
