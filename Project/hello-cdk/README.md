
# Welkom bij mijn CDK Python project!

Dit is een leeg project voor Python ontwikkeling met CDK.

Het `cdk.json` bestand vertelt de CDK Toolkit hoe uw app uitgevoerd moet worden.

Dit project is opgezet als een standaard Python project.  Het initialisatie
proces maakt ook een virtualenv aan binnen dit project, opgeslagen onder de `.venv`
map.  Om de virtualenv aan te maken wordt er verondersteld dat er een `python3`
(of `python` voor Windows) op je pad staat met toegang tot het `venv`
pakket. Als om wat voor reden dan ook de automatische creatie van de virtualenv mislukt,
kunt u de virtualenv handmatig aanmaken.

De parameters handleiding bevind zich [**hier**](/Project/hello-cdk/parameters.md).

Om handmatig een virtualenv aan te maken op MacOS en Linux:

```
$ python -m venv .venv
```

Nadat het init proces is voltooid en de virtualenv is aangemaakt, kunt u de volgende
stap gebruiken om uw virtualenv te activeren.

```
$ source .venv/bin/activate
```

Als u een Windows platform bent, zou u de virtualenv als volgt activeren:

```
% .venv\Scripts\activate.bat
```

Zodra de virtualenv is geactiveerd, kunt u de benodigde dependencies installeren.

```
$ pip install -r requirements.txt
```

Op dit punt kunt u nu de CloudFormation template voor deze code synthetiseren.

```
$ cdk synth
```

Om extra afhankelijkheden toe te voegen, bijvoorbeeld andere CDK bibliotheken, voegt u
ze toe aan uw `setup.py` bestand en voer het `pip install -r requirements.txt`
commando.

Parameters overzicht vind u hier.

## Nuttige commando's

 * `cdk ls` lijst alle stacks in de app
 * `cdk synth` zendt de gesynthetiseerde CloudFormation template uit
 * `cdk deploy` deploy deze stack naar uw standaard AWS account/regio
 * `cdk diff` vergelijk de uitgezette stack met de huidige status
 * `cdk docs` open CDK documentatie

Veel plezier!