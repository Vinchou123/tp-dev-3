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
        
        decoded_data = data.decode('utf-8')
        print(f"Données reçues du client : {decoded_data()}")
        
        if "meo" in decoded_data().lower():
            response = "Meo à toi confrère."
        elif "waf" in decoded_data().lower():
            response = "ptdr t ki"
        else:
            response = "Mes respects humble humain."
        
        conn.sendall(response.encode('utf-8'))
    
    except socket.error as e:
        print("Une erreur est survenue : {e}")
        break
    except Exception as e:
        print(f"Erreur : {e}")
        break
    
conn.close()

sys.exit(0)
