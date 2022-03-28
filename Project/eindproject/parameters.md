| **Parameter**    	| **Beschrijving**      	|
|------------	|----------------	|
|    name 	|   identificatienaam. 	|
| bucket_name	| Fysieke naam van deze bucket.           	|
| versioned  	|    Of deze bucket versiebeheer aan moet hebben of niet.  	|
| auto_delete_objects 	| Of alle objecten automatisch moeten worden verwijderd wanneer de bucket uit de stapel wordt verwijderd of wanneer de stapel wordt verwijderd.	|
|   sources	|   De bronnen van waaruit de inhoud van deze bucket moet worden ingezet.   	|
|    max_az 	|    Bepaal het maximum aantal AZ's dat u in deze regio wilt gebruiken.	|
| 	cidr    |    Het IPv4-adresbereik, in CIDR-notatie, van waaruit client-IP-adressen moeten worden toegewezen.   |
|   subnet_name	|    Logische naam voor de subnetgroep.   	|
|   cidr_mask 	|   Het aantal eerste 1 bits in het routingmasker.	|
| 	peer_region    |    De regiocode voor de accepterende VPC.   |
| 	role_service_principal   |    Een IAM principal die een AWS dienst vertegenwoordigt.   |
|   role_managed_policy_name	|    Importeer een beheerd beleid van een van de beleidsregels die AWS beheert.  	|
|   description  	|    beschrijving.	|
| 	allow_all_outbound    |   Of de SecurityGroup geconfigureerd is om alle uitgaand verkeer toe te staan.    |
|   ssh_allowed_ipv4	|   Elk IPv4 adres.   	|
|   ssh_allowed_port 	|   Een enkele TCP-poort.	|
|    ssh_port_description 	|   Poort beschrijving. 	|
| 	 rdp_allowed_ipv4   |    Elk IPv4 adres.   |
|   rdp_allowed_port	|   Een enkele TCP-poort.   	|
|   rdp_port_description 	|   Poort beschrijving.	|
|   http_allowed_port  	|    Een enkele TCP-poort.	|
| 	 http_port_description   |   Poort beschrijving.    |
|   https_allowed_port	|   Een enkele TCP-poort.   	|
|   https_port_description 	|   Poort beschrijving.	|
| 	store_public_key    |    Configuratie voor het opslaan van het publieke sleutel.   |
|   instance_type 	|   Instantietype voor EC2-instanties.	|
|   availability_zone  	|   In welk AZ de instantie binnen de VPC moet worden geplaatst.  	|
| 	root_device_directory    |   hoofdmap directory    |
|   volume_size	|    De volumegrootte, in Gibibytes (GiB).   	|
|   encrypted_volume 	|   Geeft aan of het EBS-volume is versleuteld.	|
|   asset_bucket  	|   Naam van de S3 bucket om van te downloaden. 	|
| 	asset_path    |    De sleutel van het te downloaden bestand. De schijflocatie van het bestand.   |
|   asset_region	|    De regio van de S3 bucket.  	|
|    backup_plan_name 	|    De weergavenaam van het back-upplan.	|
| 	 backup_vault_name   |    De naam van een logische container waar back-ups worden opgeslagen. |
|   backup_rule_name	|   Een weergavenaam voor de backup regel.   	|
|    delete_backup_after_days	|   Specificeert de tijdsduur na creatie dat een herstelpunt wordt verwijderd.	|
|    cron_minute 	|  Cron tijd minuut	|
| 	  cron_hour  |   Cron tijd uur  |
|   cron_month	|   Cron tijd maand |
|    cron_week_day	|  Cron tijd weekdag 	|
| 	 backup_selection_name   |   De naam voor deze selectie.    |