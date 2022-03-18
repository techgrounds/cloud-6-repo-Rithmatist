import boto3
import certmaker
from os.path import exists


def generated_certificate():
    if exists("arn.txt"):
        f = open("arn.txt", "r+")
        return f.read()
    else:
        acm = boto3.client('acm')
        response = acm.import_certificate(
            Certificate=certmaker.certifictate_pem,
            PrivateKey=certmaker.private_key_pem,
            CertificateChain=certmaker.ca_certifictate_pem,
        )
        arn = response['CertificateArn']
        f = open("arn.txt", "w+")
        f.write(arn)

        return arn

