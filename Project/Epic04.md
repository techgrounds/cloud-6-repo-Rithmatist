# Epic 04
 ## Als klant wil ik een werkende applicatie hebben waarmee ik een veilige netwerk kan deployen
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De applicatie moet een netwerk opbouwen dat aan alle eisen voldoet. Een voorbeeld van een genoemde eis is dat alleen verkeer van trusted sources de management server mag benaderen. |
| Doel                | IaC-code voor het netwerk en alle onderdelen                                                                                                                                         |
| User problem        | Alleen trusted sources (IP Adressen) mogen de management server benaderen                                                                                                            |
| User value          | Afschermen van ongewenst verkeer naar de Admin/Management server                                                                                                                     |
| Aannames            | Trusted Sources is het DevOps team                                                                                                                                                   |
| Doen we niet        | De rest van de wereld toegang geven                                                                                                                                                  |
| Acceptatie criteria | Als bij test blijkt dat alleen DevOps toegang kunnen krijgen en al het andere verkeer niet                                                                                           |