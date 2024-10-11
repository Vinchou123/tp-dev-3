import socket
import re
from sys import argv
from os import system
import ipaddress
import tempfile
from datetime import datetime
import os
import logging
import psutil
import platform



TEMP_DIR = os.path.join(tempfile.gettempdir(), "network_tp3")
LOG_FILE = os.path.join(TEMP_DIR, "network.log")

os.makedirs(TEMP_DIR, exist_ok=True)
log_entries = []


def log_command(command, argument=None, error=False):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error:
        log_message = f"{timestamp} [ERROR] Command {command} called with bad arguments : {argument}.\n"
    else:
        log_message = f"{timestamp} [INFO] Command {command} called successfully"
        if argument:
            log_message += f" with argument {argument}.\n"
        else:
            log_message += ".\n"

   
    log_entries.append(log_message)

def lookup(nom_de_domaine):
   
        pattern = r'^[a-zA-Z0-9]+(\.[a-z0-9]+)+$'
        if not re.match(pattern, nom_de_domaine):
            return "Nom de domaine invalide"
        
        try: 
            ip_adress = socket.gethostbyname(nom_de_domaine)
            return ip_adress
        except socket.gaierror:
            return "Nom de domaine inconnu"
                
def ping(ip_adress):
   
    try: 
        ipaddress.ip_address(ip_adress)
        response = system(f'ping -n 1 {ip_adress} > NUL 2>&1')

        if response == 0 :
           return 'UP !'

        else:
            return 'DOWN !'

    except ValueError:
        return "Adresse IP invalide"
    
    
        
def ip():
    interfaces = psutil.net_if_addrs()
    ip_wifi= 'enp0s3'

    if ip_wifi in interfaces:
        for interface in interfaces[ip_wifi]:
            if interface.family == socket.AF_INET:
                ip_address = interface.address
                netmask= interface.netmask
                network = ipaddress.IPv4Network(f"{ip_address}/{netmask}", strict=False)
                netmask_bits = network.prefixlen               
                return f'{ip_address}/{netmask_bits}'

    return 'Adresse IP inconnue'

def read_log():
    log_file_path = LOG_FILE  
    try:
        with open(log_file_path, 'r') as log_file:
            content = log_file.read()
            print(content)
    except FileNotFoundError:
        print("Le fichier de log n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la lecture du fichier de log : {e}")

        
if __name__ == '__main__':
    
    

    if len(argv) < 3 and argv[1] != "ip": 
        print("Usage: python network.py <lookup|ping|ip> <argument>")
    else:
        command = argv[1]
        argument = argv[2] if len(argv) > 2 else None
        result = ""

    if command == "lookup" and argument:
            result = lookup(argument)
            log_command("lookup", argument, result != "Nom de domaine invalide")
    elif command == "ping" and argument:
            result = ping(argument)
            log_command("ping", argument, result != "Adresse IP invalide")
    elif command == "ip":
            result = ip()
            log_command("ip")
    else:
            log_command(command, argument, success=False)
            result = f"Commande ou argument invalide : {command} {argument}"
            
    with open(LOG_FILE, 'a') as log_file:
        log_file.writelines(log_entries)
        
    print(result)
    
    read_log()
    
    
        

    
    