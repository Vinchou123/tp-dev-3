import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('10.2.2.222', 13337))
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
            message = message_received[:-8] 
            print(f"Message reçu du client : {message}")

            try:
                res = eval(message)
                client.send(str(res).encode())
            except Exception as e:
                client.send(f"Erreur: {str(e)}".encode())
        else:
            print("Le message ne se termine pas par la séquence de fin.")

    except socket.error:
        print("Une erreur de socket est survenue.")
        break

client.close()
sock.close()
