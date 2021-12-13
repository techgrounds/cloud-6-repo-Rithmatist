# Protocols
Een netwerk protocol is een afspraak die wij mensen gemaakt hebben over hoe computers met elkaar communiceren. Deze afspraken maken het mogelijk dat het Internet kan bestaan, zonder dat je voor iedere verbinding een andere standaard moet aanhouden.
Het OSI-model is een goed hulpmiddel om te beschrijven waar een protocol ‘leeft’ en wat het doel is van een protocol. Vaak genoeg ‘leeft’ een protocol in meerdere lagen van het OSI-model.

Twee protocols die in laag 4 ‘leven’ is TCP en UDP. Deze protocols zijn verantwoordelijk voor het transport van internet pakketten. 
TCP, veel gebruikt op het web, heeft een aantal stappen waarin er zeker gesteld wordt dat de verbinding gemaakt kan worden en om zeker te zijn dat alle data is overgekomen. Dit is ook wel de ‘three-way handshake’ genoemd. Dit maakt TCP erg betrouwbaar.
UDP heeft een hele andere aanpak: ‘fire and forget’. UDP maakt geen zorgen over of een pakketje aankomt. Dit maakt dit protocol onbetrouwbaar, maar wel veel sneller. UDP wordt veel gebruikt in omstandigheden waar snelheid belangrijker is dan verbinding. Zoals de video data van een Zoom-call.

Protocols die ‘leven’ in hogere lagen van het OSI-model hebben meestal specifieke toepassingen. HTTP(s) of SSH zijn enkele voorbeelden van hogere level protocols.

Onderdeel van de afspraken die wij gemaakt hebben over protocols is dat deze meestal een ‘standaard poort’ hebben. Voor SSH is dit poort 22.

## Key-terms

## Opdracht
- Begrijp hoe een HTTPS TCP/IP-pakket opgebouwd is
- Begrijp wie bepaalt welke protocols wij gebruiken en wat je zelf moet doen om een nieuw protocol te introduceren.
- Identificeer op zijn minst één protocol per OSI-laag.
- Facebook was recent een lange tijd niet beschikbaar. Ontdek waarom. Tip: BGP.

### Gebruikte bronnen
[Wat is het OSI-model?](https://www.strato.nl/server/wat-is-het-osi-model/)

### Ervaren problemen

### Resultaat

![osi model](../00_includes/osimodel.jpg)

#### Toepassingsgeoriënteerde lagen

De bovenste lagen van het OSI-referentiemodel worden toepassingsgeoriënteerde lagen genoemd. Men maakt onderscheid tussen de toepassingslaag, de presentatielaag en de sessielaag.

- __Laag 7 – toepassingslaag (application layer):__
de toepassingslaag is het niveau van het OSI-model dat direct contact heeft met toepassingen als e-mailprogramma’s of webbrowsers. Hier worden gegevens uitgewisseld. De toepassingslaag brengt de verbinding met de lagere niveaus van het OSI-model tot stand en houdt functies voor toepassingen gereed. Aan de hand van het __voorbeeld van de e-mailoverdracht__ kan deze laag als volgt worden verduidelijkt: een gebruiker tikt een bericht in het e-mailprogramma op zijn eindapparaat. Dit bericht wordt in de vorm van een datapakket in de toepassingslaag geladen. Daarbij wordt extra informatie aan de e-mailgegevens toegevoegd in de vorm van een ‘application header’. Dat wordt ook wel ‘inkapselen’ genoemd. Deze header bevat onder andere de informatie dat het pakket gegevens bevat die afkomstig zijn van een e-mailprogramma. Daarnaast wordt het protocol bepaald dat gebruikt wordt voor de overdracht van de e-mail op de toepassingslaag (in het geval van een e-mail meestal SMTP).


- __Laag 6 – presentatielaag (presentation layer):__ een centrale taak bij de netwerkcommunicatie is ervoor te zorgen dat gegevens in standaardformaten worden overgedragen. In de presentatielaag worden lokale weergaven daarom vertaald naar gestandaardiseerde formaten. In het geval van de e-mailoverdracht wordt hier bepaald hoe het bericht moet worden weergegeven. Daarvoor wordt het datapakket aangevuld met een ‘presentation header’. Deze bevat informatie over hoe de e-mail gecodeerd is (in Nederland meestal ISO 8859-1 (Latin-1) of ISO 8859-15), in welk formaat eventuele bijlagen aanwezig zijn (bijv. JPEG of MPEG4) en hoe de gegevens gecomprimeerd of versleuteld zijn (bijv. SSL/TLS). Zo kan ervoor worden gezorgd dat het formaat van de e-mail ook door het doelsysteem wordt begrepen en het bericht daar correct wordt weergegeven.


- __Laag 5 – sessielaag (session layer):__ de centrale taak die in de sessielaag wordt volbracht, is het regelen van de verbinding tussen de twee eindsystemen. Daarom wordt deze laag ook wel communicatielaag genoemd. Hier zijn speciale regel- en controlemechanismen actief die het tot stand komen, onderhouden en beëindigen van de verbinding regelen. Voor deze __communicatieregeling__ is extra informatie nodig die door een ‘session header’ aan de e-mailgegevens wordt toegevoegd. De meest gangbare applicatieprotocollen, zoals SMTP of FTP, houden zich zelf met de sessies bezig of zijn net als HTTP toestandsloos. Het TCP/IP-model dat concurreert met het OSI-model vat daarom OSI 5, 6 en 7 samen tot één application layer. Andere standaards die aansluiten op laag 5 zijn NetBIOS, Socks en RPC.


#### Transportgeoriënteerde lagen
Op de drie toepassingsgeoriënteerde lagen van het OSI-model volgen vier transportgeoriënteerde lagen. Men maakt onderscheid tussen de transportlaag, de netwerklaag, de datalinklaag en de fysieke laag.

- __Laag 4 – transportlaag (transport layer):__ de transportlaag fungeert als schakel tussen de toepassingsgeoriënteerde en de transportgeoriënteerde lagen. Op dit niveau van het OSI-model wordt de logische end-to-endverbinding, het overdrachtskanaal, tussen de communicerende systemen gerealiseerd. Ook daarvoor moet aan de e-mailgegevens bepaalde informatie worden toegevoegd. Het datapakket, dat al met de headers van de toepassingsgeoriënteerde lagen is uitgebreid, wordt in laag 4 aangevuld met een ‘transport header’. Daarbij worden gestandaardiseerde netwerkprotocollen als TCP of UDP gebruikt. Bovendien wordt in de transportlaag bepaald via welke poorten toepassingen op het doelsysteem kunnen worden aangestuurd. In laag 4 wordt een datapakket dus ook aan een bepaalde toepassing toegewezen.


- __Laag 3 – netwerklaag (network layer):__ met laag 3 bereikt de gegevensoverdracht het internet. In de netwerklaag worden de __eindapparaten logisch geadresseerd.__ Hieraan wordt in laag 3 een eenduidig IP-adres toegewezen. Aan een datapakket, zoals de e-mailgegevens in het voorbeeld, wordt op het 3e niveau van het OSI-model een ‘network header’ toegevoegd, die informatie bevat over de routering en over de controle van de gegevensstroom. Ook hier maken de computersystemen gebruik van internetstandaards als IP, ICMP, X.25, RIP of OSPF. Bij het e-mailverkeer wordt meestal TCP over IP gebruikt.


- __Laag 2 – datalinklaag (data link layer):__ in de datalinklaag zorgen functies voor het herkennen van fouten, het verhelpen van fouten en de controle van de gegevensstroom ervoor dat __overdrachtsfouten__ worden voorkomen. Daarvoor wordt het datapakket inclusief application, presentation, session, transport en network header omgeven door een frame van data link header en data link trail. Daarnaast vindt in de 2e laag de hardware-adressering plaats. Daarbij worden zogenaamde MAC-adressen gebruikt. De toegang tot het medium wordt geregeld door protocollen als Ethernet of PPP.


- __Laag 1 – fysieke laag (physical layer):__ in de fysieke laag worden de bits van een datapakket omgezet in een fysiek signaal dat bij het overdrachtsmedium past. Alleen dit signaal kan via een medium als koperdraad, glasvezel of de lucht worden overgedragen. Het koppelvlak naar het overdrachtsmedium wordt bepaald door protocollen en normen als DSL, ISDN, Bluetooth, USB (fysieke laag) of Ethernet (fysieke laag).


![iso remember](../00_includes/iso-seven-layer-model.jpg)