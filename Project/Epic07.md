# Epic 07
## Als klant wil ik een opslagoplossing hebben waarin bootstrap/post-deployment script opgeslagen kunnen worden
| Item                | Opmerking                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Kenmerk             | v1.0                                                                                                                                    |
| Omschrijving        | Er moet een locatie beschikbaar zijn waar bootstrap scripts beschikbaar worden. Deze script moeten niet publiekelijk toegankelijk zijn. |
| Doel                | IaC-code voor een opslagoplossing voor scripts                                                                                          |
| User problem        | SCripts die de klant wil gaan gebruiken moeten veilig opgeslagen worden                                                                 |
| User value          | Op eenvoudige wijze bij de scripts kunnen in een veilige omgeving                                                                       |
| Aannames            | S3 bucket wordt gebruikt met versioning en encryptie                                                                                    |
| Doen we niet        | Aannames doen over de mate van opvragingen uit de S3 bucket                                                                             |
| Acceptatie criteria | Als de S3 Bucket er is en niet publiekelijk te benaderen is                                                                             |