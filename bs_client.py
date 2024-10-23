import socket
import sys

host = '10.2.2.2'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    
    message = input("Que souhaites-tu écrire au serveur ?")
    s.sendall(message.encode())  
    data = s.recv(1024)
    
except Exception as e:
    print(f"Erreur lors de la connexion au serveur : {e}")

finally:
    s.close()

print(f"Le serveur a répondu : {repr(data)}")
sys.exit(0)
