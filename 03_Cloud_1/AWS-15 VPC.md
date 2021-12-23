# Virtuele privécloud (VPC)
De Amazon VPC is een virtueel privé datacenter in de cloud. U kunt subnets, internet gateways (igw), NAT gateways, VPN-verbindingen en meer aanmaken. VPC's werken op regionaal niveau, terwijl subnetten alleen in één beschikbaarheidszone kunnen worden geplaatst.
## Key-terms

## Opdracht

### Oefening 1:
- Navigeer naar het VPC menu in uw sandbox omgeving.
- Wijs een Elastic IP-adres toe aan uw account.
  - Gebruik de optie Launch VPC Wizard om een nieuwe VPC aan te maken met de volgende vereisten:
  - Regio: Frankfurt (eu-central-1)
  - VPC met een publiek en een privaat subnet
  - Naam: Lab VPC
  - CIDR: 10.0.0.0/16
- Vereisten voor het publieke subnet:
  - Naam: Publiek subnet 1
  - CIDR: 10.0.0.0/24
  - AZ: eu-central-1a
- Eisen aan het private subnet:
  - Naam: Particulier subnet 1
  - CIDR: 10.0.1.0/24
  - AZ: eu-central-1a
  
### Oefening 2:
- Maak een extra publiek subnet met de volgende vereisten:
  - VPC: Lab VPC
  - Naam: Openbaar Subnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.2.0/24
- Maak een extra privésubnet met de volgende vereisten:
  - VPC: Lab VPC
  - Naam: Privésubnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.3.0/24
- Bekijk de hoofdroutetabel voor Lab VPC. Deze zou een entry moeten hebben voor de NAT gateway. Hernoem deze route tabel naar Private Route Table.
- Koppel de private route tabel expliciet aan uw twee private subnetten.
- Bekijk de andere route tabel voor Lab VPC. Deze zou een entry moeten hebben voor de internet gateway. Hernoem deze route tabel naar Public Route Table.
- Koppel de publieke route tabel expliciet aan uw twee publieke subnetten.

### Oefening 3:
- Maak een Beveiligingsgroep met de volgende vereisten:
  - Naam: Web SG
  - Beschrijving: HTTP-toegang mogelijk maken
  - VPC: Lab VPC
  - Inkomende regel: HTTP toegang overal vandaan toestaan
  - Uitgaande regel: Sta alle verkeer toe

### Oefening 4:
- Start een EC2 instance met de volgende vereisten:
   - AMI: Amazon Linux 2
   - Type: t3.micro
   - Subnet: Openbaar subnet 2
   - Auto-toewijzen publiek IP: Inschakelen
   - Gebruikersgegevens:

            #!/bin/bash
            yum install -y httpd mysql php
            wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
            unzip lab-app.zip -d /var/www/html/
            chkconfig httpd on
            service httpd start

   - Tag:

      Key: Naam:

      Waarde: Webserver

   - Beveiligingsgroep: Web SG
   - Sleutelpaar: geen sleutelpaar
- Maak verbinding met uw server met de openbare IPv4 DNS naam.

### Gebruikte bronnen


### Ervaren problemen
Webpagina moest ik van `https` veranderen naar `http`.

### Resultaat

### Oefening 1:
- Navigeer naar het VPC menu in uw sandbox omgeving.

![vpcmenu](../00_includes/vpcmenu.JPG)
- Wijs een Elastic IP-adres toe aan uw account.

![allocateip](../00_includes/allocateip.JPG)
  - Gebruik de optie Launch VPC Wizard om een nieuwe VPC aan te maken met de volgende vereisten:

![20wizard](../00_includes/vpc%20wizard.JPG)
  - Regio: Frankfurt (eu-central-1)
  - VPC met een publiek en een privaat subnet
  - Naam: Lab VPC
  - CIDR: 10.0.0.0/16
  - Vereisten voor het publieke subnet:
    - Naam: Publiek subnet 1
    - CIDR: 10.0.0.0/24
    - AZ: eu-central-1a
  - Eisen aan het private subnet:
    - Naam: Particulier subnet 1
    - CIDR: 10.0.1.0/24
    - AZ: eu-central-1a

![excercise1](../00_includes/excercise1.JPG)

### Oefening 2:
- Maak een extra publiek subnet met de volgende vereisten:
  - VPC: Lab VPC
  - Naam: Openbaar Subnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.2.0/24

![publicsub](../00_includes/publicsub.JPG)
- Maak een extra privésubnet met de volgende vereisten:
  - VPC: Lab VPC
  - Naam: Privésubnet 2
  - AZ: eu-central-1b
  - CIDR: 10.0.3.0/24

![privatesub](../00_includes/privatesub.JPG)
- Bekijk de hoofdroutetabel voor Lab VPC. Deze zou een entry moeten hebben voor de NAT gateway. Hernoem deze route tabel naar Private Route Table.

![mainnat](../00_includes/mainnat.JPG)
- Koppel de private route tabel expliciet aan uw twee private subnetten.

![main](../00_includes/main.JPG)
- Bekijk de andere route tabel voor Lab VPC. Deze zou een entry moeten hebben voor de internet gateway. Hernoem deze route tabel naar Public Route Table.

![otherig](../00_includes/otherig.JPG)
- Koppel de publieke route tabel expliciet aan uw twee publieke subnetten.

![other](../00_includes/other.JPG)

### Oefening 3:
- Maak een Beveiligingsgroep met de volgende vereisten:
  - Naam: Web SG
  - Beschrijving: HTTP-toegang mogelijk maken
  - VPC: Lab VPC
  - Inkomende regel: HTTP toegang overal vandaan toestaan
  - Uitgaande regel: Sta alle verkeer toe

![excercise3](../00_includes/excercise3.JPG)

### Oefening 4:
- Start een EC2 instance met de volgende vereisten:
   - AMI: Amazon Linux 2
  
![awslinux2](../00_includes/awslinux2.JPG)

  - Type: t3.micro

![instancetype](../00_includes/instancetype.JPG)
  - Subnet: Openbaar subnet 2
  - Auto-toewijzen publiek IP: Inschakelen
  - Gebruikersgegevens:

           #!/bin/bash
           yum install -y httpd mysql php
           wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
           unzip lab-app.zip -d /var/www/html/
           chkconfig httpd on
           service httpd start

![instancedetails](../00_includes/instancedetails.JPG)

   - Tag:

      Key: Naam:

      Waarde: Webserver

![tags](../00_includes/tags.JPG)

   - Beveiligingsgroep: Web SG

![securitygroup](../00_includes/securitygroup.JPG)
   - Sleutelpaar: geen sleutelpaar

![nokey](../00_includes/nokey.JPG)
   - Maak verbinding met uw server met de openbare IPv4 DNS naam.

![result](../00_includes/result.JPG)