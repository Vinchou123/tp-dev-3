import socket
import re
from sys import argv

if len(argv) != 2:
    print("Usage: python lookuip.py <nom_de_domaine>")
else: 
    nom_de_domaine = argv[1]
    pattern = r'^[a-zA-Z0-9]+(\.[a-z0-9]+)+$'
    if not re.match(pattern, nom_de_domaine):
        print("Nom de domaine invalide")
    else:
        try: 
            ip_adress = socket.gethostbyname(nom_de_domaine)
            print(f'Adresse IP de {nom_de_domaine} : {ip_adress}')
        except socket.gaierror:
            print("Nom de domaine inconnu")

            
