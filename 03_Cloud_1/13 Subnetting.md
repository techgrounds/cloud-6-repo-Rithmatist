# Subnetting
Een Local Area Network (LAN) wordt vaak uitgedrukt als een reeks IP-adressen. Elk apparaat (host) krijgt zijn eigen adres binnen die reeks. Netwerken hebben een subnetmasker dat bepaalt hoeveel bits van het IP-adres deel uitmaken van het netwerkadres, en hoeveel bits gereserveerd zijn voor de host.

## Key-terms

- **LAN** = Lokaal netwerk
- **NAT** = vertaling van netwerkadressen
- **WAN** = Breed gebiedsnetwerk

## Opdracht
- Maak een netwerkarchitectuur die voldoet aan de volgende eisen:
  - 1 private subnet dat alleen van binnen het LAN bereikbaar is. Dit subnet moet minimaal 15 hosts kunnen plaatsen.
  - 1 private subnet dat internet toegang heeft via een NAT gateway. Dit subnet moet minimaal 30 hosts kunnen plaatsen (de 30 hosts is exclusief de NAT gateway).
  - 1 public subnet met een internet gateway. Dit subnet moet minimaal 5 hosts kunnen plaatsen (de 5 hosts is exclusief de internet gateway).
- Plaats de architectuur die je hebt gemaakt inclusief een korte uitleg in de Github repository die je met de learning coach hebt gedeeld.


### Gebruikte bronnen

### Ervaren problemen

### Resultaat


![netwerk](../00_includes/netwerk.png)

/25 vertaald zich hoeveel "0" er zijn in de Subnet Mask en 126 hosts.
Dit verdeel ik met twee private subnet en public subnet.
Om in de private subnet internet te krijgen, plaats je een NAT gateway in de public subnet die een verbdinding heeft met een internet gateway.