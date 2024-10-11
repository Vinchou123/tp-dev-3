from os import system
from sys import argv

if len(argv) != 2:
    print("Usage: python ping_arg.py <IP>")
else:
    ip_adress = argv[1]
    print(f'Ping de l\'adresse IP : {ip_adress}')

    system(f'ping {ip_adress}')

