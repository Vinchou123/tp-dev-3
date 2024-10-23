import socket
import sys
import re
import logging
import os
import tempfile

log_dir = os.path.join(os.path.expanduser("~"), "temp_logs")
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, 'bs_client.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler(log_file_path)]
)


def log_error(message):
    print(f"\033[31m{message}\033[0m")
    logging.error(message)

host = '10.2.2.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    logging.info(f"Connexion réussie à {host} sur le port {port}")
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    
    while True:
        expression = input("Entrez une opération arithmétique : ")
        
        if not re.match(r'^-?\d+\s*[\+\-\*]\s*-?\d+$', expression):
            log_error("Erreur : L'entrée doit être une opération arithmétique valide avec des entiers.")
            continue

        num1, operator, num2 = re.split(r'\s*([\+\-\*])\s*', expression)
        
        num1 = int(num1)
        num2 = int(num2)

        if not (-100000 <= num1 <= 100000) or not (-100000 <= num2 <= 100000):
            log_error("Erreur : Les nombres doivent être compris entre -100000 et +100000.")
            continue

        s.sendall(expression.encode('utf-8'))
       
        data = s.recv(1024)
        print(f"Le serveur a répondu : {data.decode('utf-8')}")
        logging.info(f"Message envoyé : '{expression}'")

except Exception as e:
    log_error(f"Erreur lors de la connexion au serveur : {e}")

finally:
    s.close()
    sys.exit(0)
