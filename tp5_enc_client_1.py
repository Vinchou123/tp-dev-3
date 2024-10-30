import socket
import re

def validate_expression(expression):
    pattern = r'^-?\d{1,7}\s*[\+\-\*]\s*-?\d{1,7}$'
    if re.match(pattern, expression):
        operands = re.split(r'[\+\-\*]', expression)
        try:
            x, y = int(operands[0].strip()), int(operands[1].strip())
            if -1048575 <= x <= 1048575 and -1048575 <= y <= 1048575:
                return True
        except ValueError:
            return False
    return False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('10.2.2.2', 13337))
s.send('Hello'.encode())

while True:
    msg = input("Entrez une expression arithmétique: ")
    if validate_expression(msg):
        break
    else:
        print("Expression invalide. Essayez un format simple: x opérateur y, avec x et y entre -1048575 et 1048575.")

encoded_msg = msg.encode('utf-8')
msg_len = len(encoded_msg)

header = msg_len.to_bytes(4, byteorder='big')
sequence_fin = "<clafin>".encode('utf-8')

payload = header + encoded_msg + sequence_fin
sock.send(payload)

s_data = sock.recv(1024)
print("Résultat:", s_data.decode())

sock.close()
