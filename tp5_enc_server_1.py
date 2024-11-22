import socket


HOST = '127.0.0.1'
PORT = 9999
END_SEQUENCE = b"<clafin>"  

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 9999))
sock.listen(5)

print(f"Serveur en écoute sur {HOST}:{PORT}")

while True:
    client, client_addr = sock.accept()
    print(f"Connexion acceptée depuis {client_addr}")
    
    try:
        
        header = client.recv(4)
        if not header:
            break
        
        msg_len = int.from_bytes(header, byteorder='big')
        print(f"Taille du message : {msg_len} octets")
        
        
        message = client.recv(msg_len)
        footer = client.recv(len(END_SEQUENCE))
        
        if footer == END_SEQUENCE:
            print(f"Message reçu : {message.decode("utf-8")}")
            client.sendall("Message reçu avec succès".encode("utf-8"))
        else:
            print("Erreur : Séquence de fin invalide")
            client.sendall("Erreur : Séquence de fin invalide".encode("utf-8"))
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        client.close()
        print("Connexion fermée avec le client")
