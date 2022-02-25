# Epic 09
## Als klant wil ik iedere dag een backup hebben dat 7 dagen behouden wordt
| Item                | Opmerking                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Kenmerk             | v1.0                                                                                                                                                                                 |
| Omschrijving        | De klant wil graag dat er een backup beschikbaar is, mocht het nodig zijn om de servers terug te brengen naar een eerdere staat. (Zorg ervoor dat de Backup ook daadwerkelijk werkt) |
| Doel                | IaC-code voor backup voorzieningen                                                                                                                                                   |
| User problem        | Elke dag een backup van de webserver                                                                                                                                                 |
| User value          | Indien er iets fout gaat, kan het hersteld worden m.b.v. een backup van één dag oud                                                                                                  |
| Aannames            | Management server ook meenmenen in een backup structuur (1x per week, 1 behouden)                                                                                                    |
| Doen we niet        | Snapshots                                                                                                                                                                            |
| Acceptatie criteria | Als de backups zijn gedraaid en er zijn                                                                                                                                              |