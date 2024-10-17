import socket
import sys


host= '10.2.2.2'
port = 13337

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.sendall(b"Meooooo !")

data=s.recv(1024)

s.close()
print(f"Le serveru à répondu  {repr(data)}")

exit(0)
