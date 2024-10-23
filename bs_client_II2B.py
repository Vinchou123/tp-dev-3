import socket
import sys
import re
import logging
import os

log_dir = os.path.join(os.path.expanduser("~"), "temp_logs")
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, 'bs_client.log')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.FileHandler(log_file_path)]
)

host = '10.2.2.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    logging.info(f"Connexion réussie à {host}:{port}")
    print(f"Connecté avec succès au serveur {host} sur le port {port}")

    while True:
        message = input("Que souhaites-tu écrire au serveur ? ")

        if type(message) is not str:
            raise TypeError("L'entrée doit être une chaîne de caractères.")
        
        if not re.search(r'\b(waf|meo)\b', message.lower()):
            raise TypeError("La chaîne doit contenir soit 'waf' soit 'meo'.")

        s.sendall(message.encode('utf-8'))
        logging.info(f"Message envoyé au serveur {host}:{port} : {message}")

        data = s.recv(1024)
        logging.info(f"Réponse reçue du serveur {host}:{port} : {data.decode('utf-8')}")

        print(f"Le serveur a répondu : '{data.decode('utf-8')}'")
        break

except TypeError as te:
    print(f"\033[31mErreur : {te}\033[0m")
except socket.error as e:
    error_message = f"Impossible de se connecter au serveur {host} sur le port {port}."
    print(f"\033[31mERROR {error_message}\033[0m")
    logging.error(error_message)
except Exception as e:
    print(f"\033[31mErreur : {e}\033[0m")

finally:
    s.close()

sys.exit(0)
