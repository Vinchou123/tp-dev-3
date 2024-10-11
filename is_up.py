from os import system
from sys import argv
import ipaddress


if len(argv) != 2:
    print("Usage: python ping_arg.py <IP>")
else:
    ip_adress = argv[1]

try: 
    ipaddress.ip_address(ip_adress)
    response = system(f'ping -n 1 {ip_adress} > NUL 2>&1')

    if response == 0 :
        print ('UP !')

    else:
        print ('DOWN !')

except ValueError:
        print ("Adresse IP invalide")
    


    


