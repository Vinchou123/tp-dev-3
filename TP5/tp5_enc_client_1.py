import socket
import re


HOST = '127.0.0.1'
PORT = 9999
END_SEQUENCE = b"<clafin>"  

def is_valid_expression(value: str):
    """Valide si l'expression est du type x opérateur y"""
    return re.match(r'^-?\d+\s*[\+\-\*]\s*-?\d+$', value)

def check_number_limits(numbers: list):
    """Vérifie que les nombres sont dans la plage autorisée"""
    return all(-1048575 <= int(num) <= 1048575 for num in numbers)

msg = input("Calcul à envoyer : ")
if not is_valid_expression(msg):
    raise ValueError("L'expression saisie n'est pas valide.")

numbers = re.findall(r'-?\d+', msg)
if not check_number_limits(numbers):
    raise ValueError("Les nombres doivent être compris entre -1048575 et 1048575.")

msg_len = len(msg.encode("'utf-8'"))
header = msg_len.to_bytes(4, byteorder='big')  
payload = header + msg.encode("utf-8") + END_SEQUENCE

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('10.2.2.2', 9999))
    print("Connexion au serveur établie.")
    s.sendall(payload)
    print("Message envoyé :", payload)
    
   
    response = s.recv(1024)
    print("Réponse du serveur :", response.decode())
