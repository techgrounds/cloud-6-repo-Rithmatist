# Epic 03
 ## Als team willen wij een duidelijk overzicht hebben van de Cloud Infrastructuur die de applicatie nodig heeft
| Item | Opmerking |
| ---- | --------- |
| Kenmerk | Exploratie |
| Omschrijving | Je hebt al heel wat informatie gekregen. En al een ontwerp. Alleen in het ontwerp ontbreken nog zaken als IAM/AD. Identificeer deze extra diensten die je nodig zal hebben en maak een overzicht van alle diensten |
| Doel | Een overzicht van alle diensten die gebruikt gaan worden. |
| Team problem | Niet alle te gebruiken AWS diensten zijn benoemd in het Project Document | | Team value | Overzicht van de AWS diensten die gebruikt gaan worden |
| Aannames | Het Project document is incompleet v.w.b. de AWs diensten |
| Doen we niet | Alle diensten en oplossingen die buiten AWS liggen en die **niet** beschreven zijn in de PRD |
| Acceptatie criteria | Overzicht van te gebruiken AWS diensten |

## Overzicht AWS diensten
- S3 (bucket t.b.v. bootstrap scripts)
- EC2 (webserver/management server, AMI, Snapshots)
- VPC (Subnets, peering, netwrok ACL)
- KMS
- IAM (users, roles, policies)
- AWS Backup
- Cloudformation (stacks)
