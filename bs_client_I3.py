import socket
import sys
import re  # Importer le module pour les expressions régulières

host = '10.2.2.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    
    while True:
        message = input("Que souhaites-tu écrire au serveur ? ")

        if type(message) is not str:
            raise TypeError("L'entrée doit être une chaîne de caractères.")
        
        if not re.search(r'\b(waf|meo)\b', message.lower()):
            raise TypeError("La chaîne doit contenir soit 'waf' soit 'meo'.")

        s.sendall(message.encode('utf-8'))  
        data = s.recv(1024)

        print(f"Le serveur a répondu : '{data.decode('utf-8')}'")
        break  

except TypeError as te:
    print(f"Erreur : {te}")
except Exception as e:
    print(f"Erreur lors de la connexion au serveur : {e}")

finally:
    s.close()

sys.exit(0)
