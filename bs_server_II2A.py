import socket
import sys
import argparse
import ipaddress
import logging
import time

log_file_path = '/var/log/bs_server/bs_server.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

def log_info(message):
    logging.info(message)
    print(f"\033[37m{message}\033[0m")

def log_warn(message):
    logging.warning(message)
    print(f"\033[33m{message}\033[0m") 

def validate_port(port):
    try:
        port = int(port)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Le port spécifié '{port}' n'est pas un nombre entier valide.")
    
    if not (0 <= port <= 65535):
        raise argparse.ArgumentTypeError(f"Le port spécifié {port} n'est pas un port valide (de 0 à 65535).")
    if port <= 1024:
        raise argparse.ArgumentTypeError(f"Le port spécifié {port} est un port privilégié. Spécifiez un port au-dessus de 1024.")
    
    return port

def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip not in [ip[4][0] for ip in socket.getaddrinfo(socket.gethostname(), None)]:
            raise argparse.ArgumentTypeError(f"L'adresse {ip} n'est pas l'une des adresses IP de cette machine.")
    except ValueError:
        raise argparse.ArgumentTypeError(f"L'adresse {ip} n'est pas une adresse IP valide.")
    return ip

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=validate_port, default=13337,
                        help='Numéro de port (défaut: 13337).')
    parser.add_argument('-l', '--listen', type=validate_ip,
                        help='Adresse IP sur laquelle écouter.')

    args = parser.parse_args()

    host = args.listen if args.listen else ''
    port = args.port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    log_info(f"Le serveur tourne sur {host}:{port}")

    last_client_time = time.time()

    while True:
        conn, addr = None, None
        try:
            conn, addr = s.accept()
            log_info(f"Un client ({addr[0]}) s'est connecté.")
            last_client_time = time.time()

            while True:
                try:
                    data = conn.recv(1024)
                    if not data:
                        break
                    
                    decoded_data = data.decode('utf-8')
                    log_info(f"Le client {addr[0]} a envoyé \"{decoded_data}\".")

                    if "meo" in decoded_data.lower():
                        response = "Meo à toi confrère."
                    elif "waf" in decoded_data.lower():
                        response = "ptdr t ki"
                    else:
                        response = "Mes respects humble humain."
                        
                    log_info(f"Le client a envoyé {addr[0]} : \"{decoded_data}\".")

                    conn.sendall(response.encode('utf-8'))
                    log_info(f"Réponse envoyée au client {addr[0]} : \"{response}\".")

                except socket.error as e:
                    log_warn(f"Une erreur est survenue : {e}")
                    break
                except Exception as e:
                    log_warn(f"Erreur inattendue : {e}")
                    break

        except socket.error as e:
            log_warn(f"Une erreur est survenue lors de l'acceptation d'une connexion : {e}")
            break
        except Exception as e:
            log_warn(f"Erreur inattendue : {e}")
            break
        finally:
            if conn:
                conn.close()

        if time.time() - last_client_time > 60:
            log_warn("Aucun client depuis plus de une minute.")
            time.sleep(60)

    s.close()
    sys.exit(0)

if __name__ == "__main__":
    main()
