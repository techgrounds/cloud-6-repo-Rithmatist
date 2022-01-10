# Elastic File System
Amazon EFS is een set-and-forget, serverless, elastisch bestandssysteem dat het eenvoudig maakt om bestandsopslag op te zetten, te schalen en te optimaliseren op de AWS Cloud. Met een paar klikken in de AWS Management Console kunt u bestandssystemen maken die toegankelijk zijn via een bestandssysteeminterface (met behulp van standaard besturingssysteem file I/O API's) voor Amazon EC2-instanties, Amazon-containerservices (Amazon Elastic Container Service (ECS), Amazon Elastic Kubernetes Service (EKS) en AWS Lambda-functies, en volledige bestandssysteemtoegangssemantiek ondersteunen (zoals sterke consistentie en bestandsvergrendeling).
Zonder de noodzaak om opslag toe te wijzen, kunnen Amazon EFS-bestandssystemen automatisch schalen van gigabytes tot petabytes aan gegevens. Een Amazon EFS bestand kan worden benaderd door tientallen, honderden of zelfs duizenden computerinstanties.
## Key-terms

## Opdracht

In deze Oefening leert u hoe u Amazon EFS kunt gebruiken om uw bestanden in de cloud op te slaan.
- Het maken van een Amazon EFS-bestandssysteem, 
- Het gebruiken van een Amazon EC2 om een Linux virtuele machine te starten, 
- Leren koppelen van systemen, maken van een bestand, 
- beëindigen van instances en vernietigen van bestandssystemen.

### Oefening 1: Creëer een bestandssysteem

- Open de EFS Console.
- In de Amazon EFS console, open Create file system.
- Als de Standaard VPC niet is geselecteerd in het VPC dropdown veld, selecteer dan de dropdown pijl en selecteer de Standaard VPC. Accepteer alle standaardwaarden en klik op volgende stap.
- Accepteer alle standaardwaarden en klik op volgende stap.
- Accepteer alle standaardwaarden en klik op bestandssysteem maken.

### Oefening 2: Creëer en configureer een virtuele machine met Amazon EC2

- Open de Amazon EC2 console en klik op Launch Instance om uw virtuele machine aan te maken en te configureren.
- Zoek Amazon Linux AMI op en klik op Selecteren.
- De standaard optie van t2.micro zou al aangevinkt moeten zijn. Klik op Review and Launch onderaan de pagina.
- Klik op Starten onderaan de pagina.
- Selecteer Kies een bestaand sleutelpaar en selecteer het sleutelpaar en klik op Launch Instances om uw Linux instance te starten
- Klik op View Instances op het volgende scherm om uw instanties te bekijken en de status te zien van de instantie die u zojuist hebt gestart.
- Noteer het publieke IP adres van uw AWS instance, u heeft dit nodig om verbinding te maken met de instance
- Geef uw instantie netwerktoegang tot het bestandssysteem. Met uw instantie geselecteerd, selecteer Acties > Netwerken > Wijzig beveiligingsgroepen.
- Schakel het selectievakje voor de standaard VPC beveiligingsgroep in en klik op Beveiligingsgroepen toewijzen.

### Oefening 3: Maak verbinding met uw instance

- Download Git voor Windows [hier](https://git-scm.com/download/win). Start het gedownloade installatieprogramma en accepteer de standaardinstellingen
- Klik met de rechtermuisknop op je bureaublad (niet op een pictogram of bestand) en selecteer Git Bash Hier om een Git Bash opdrachtprompt te openen.
- Use SSH to connect to your instance. In this case the user name is ec2-user, the SSH key is stored in the directory we saved it


    The format is ssh -i {full path of your .pem file} ec2-user@{instance IP address}.


### Oefening 4: Mount uw bestandssysteem

- Open de Amazon EFS console en selecteer vervolgens het keuzerondje naast uw bestandssysteem om de details weer te geven.
- Selecteer de Amazon EC2 mount instructies link.
- Vanuit het Amazon EC2 mount instructies venster kunt u de sectie Uw EC2 instance opzetten doornemen. Deze sectie leidt u door de stappen om de nfs client op uw EC2 instance te installeren. De nfs client is al geïnstalleerd op de EC2 instance die u heeft gestart, dus u kunt verder gaan naar de volgende stap.
- Maak een nieuwe map aan op je instantie door het sudo mkdir efs commando te kopiëren.
- Plak en voer het commando sudo mkdir efs uit in uw SSH-venster.
- Ga terug naar het Amazon EC2 mount instructies venster. Mount je bestandssysteem als je nieuwe directory.
  - Kopieer het hele sudo mount -t nfs4... commando. 
  - Klik op Sluiten onderaan het venster.
- Plak en voer het hele sudo mount -t nfs4... commando uit in je SSH venster.
- Controleer of uw bestandssysteem succesvol is gemount door het volgende commando uit te voeren: 

`df -h`

- Maak een testbestand in uw nieuwe bestandssysteem door een eenvoudig dd commando uit te voeren om een 1GiB bestand te genereren in uw nieuwe directory. Voer het volgende dd commando uit in uw SSH venster:


    sudo dd if=/dev/zero of=~/efs/1GiB bs=1M count=1024 status=progress

### Oefening 5: Termineer uw resources
- Open de Amazon EC2 console, selecteer het vakje naast de instantie die u heeft aangemaakt. Klik vervolgens op de knop Actions, navigeer naar Instance State en klik op Terminate.
- Open de Amazon EFS console, selecteer het keuzerondje naast het bestandssysteem dat u hebt gemaakt. Klik vervolgens op de knop Acties en klik op Bestandssysteem verwijderen.

### Gebruikte bronnen
- [Amazon EFS FAQs](https://aws.amazon.com/efs/faq/)
- [Create a Network File System](https://aws.amazon.com/getting-started/tutorials/create-network-file-system/)
### Ervaren problemen

### Resultaat
