import socket
import sys

host = ''
port = 13337

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(1)

conn, addr = s.accept()

print('Connecting by', addr)

while True: 
    try:
        data = conn.recv(1024)
        if not data:
         break
        print(f"Données reçu du client: {data}")
        conn.sendall("Hi mate ! ")
    
    except socket.error : 
        print("Error Occured.")
        break
    
conn.close()    

exit(0)

        