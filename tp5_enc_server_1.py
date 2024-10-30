import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 13337))
sock.listen(1)
client, client_addr = sock.accept()

while True:
    try:
        header = client.recv(4)
        if not header:
            break

        msg_len = int.from_bytes(header, byteorder='big')
        print(f"Lecture des {msg_len} prochains octets")

        chunks = []
        bytes_received = 0
        while bytes_received < msg_len:
            chunk = client.recv(min(msg_len - bytes_received, 1024))
            if not chunk:
                raise RuntimeError("Erreur de réception du message.")
            chunks.append(chunk)
            bytes_received += len(chunk)

        message_received = b"".join(chunks).decode('utf-8')

        if message_received.endswith("<clafin>"):
            print(f"Message reçu du client : {message_received}")

            try:
                message = message.replace('+', ',').replace('-', ', -') 
                operands = ast.literal_eval(f"[{message}]")
                res = sum(operands)
                client.send(str(res).encode())
            except Exception as e:
                client.send(f"Erreur: {str(e)}".encode())
            
        else:
            client.send("Erreur: message mal formé.".encode())

        break
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        break

client.close()
sock.close()
