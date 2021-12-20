# AWS wereldwijde infrastructuur
In de cloud is alles, van servers tot netwerken, gevirtualiseerd. Als AWS-klant hoef je je geen zorgen te maken over de onderliggende fysieke infrastructuur. Dat gezegd hebbende, kan de fysieke locatie van een applicatie in de cloud belangrijk zijn.

AWS heeft een wereldwijde infrastructuur die bestaat uit de volgende componenten:
Regio's
Beschikbaarheidszones
Randlocaties

Als klant heb je verschillende hoeveelheden controle over waar je spullen zich bevinden, afhankelijk van de service die je gebruikt.
IAM is bijvoorbeeld een wereldwijde service, dus u krijgt geen controle over waar de informatie wordt opgeslagen. U kunt daarentegen specifieke Beschikbaarheidszones voor RDS-instanties selecteren.

## Key-terms

## Opdracht
#### Bestudeer:
- Wat is een AWS beschikbaarheidszone?
- Wat is een regio?
- Wat is een Edge locatie?
- Waarom zou je de ene regio verkiezen boven de andere? (bijv. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).

### Gebruikte bronnen
- [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [Concepts](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concepts.wa-concepts.en.html)
### Ervaren problemen

### Resultaat

#### Wat is een AWS beschikbaarheidszone?
Een afzonderlijke locatie binnen een regio die is geïsoleerd van storingen in andere beschikbaarheidszones, en goedkope netwerkconnectiviteit met lage latency biedt met andere beschikbaarheidszones in dezelfde regio.

#### Wat is een regio?
Een benoemde set van AWS resources in hetzelfde geografische gebied. Een regio omvat ten minste twee beschikbaarheidszones.

#### Wat is een Edge locatie?
Een site die CloudFront gebruikt om kopieën van uw inhoud in de cache op te slaan voor snellere levering aan gebruikers op elke locatie.

#### Waarom zou je de ene regio verkiezen boven de andere? (bijv. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).
Bijv. voor u-central-1 (Frankfurt) gaan omdat het meer dichterbij is dan over us-west-2 (Oregon).
Dus dan heb je ook een beter/sneller verbinding. (low latency).
