import socket
import sys

host = ''
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)

print(f"Serveur en attente de connexions sur le port {port}...")

conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr[0]}.")

while True:
    try:
        data = conn.recv(1024)
        if not data:
            break
        
        print(f"Données reçues du client : {data.decode()}")
        
        if "meo" in data.decode().lower():
            response = "Meo à toi confrère."
        elif "waf" in data.decode().lower():
            response = "ptdr t ki"
        else:
            response = "Mes respects humble humain."
        
        conn.sendall(response.encode())
    
    except socket.error:
        print("Une erreur est survenue.")
        break
    
conn.close()

sys.exit(0)
