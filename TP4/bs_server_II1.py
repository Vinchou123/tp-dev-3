import socket
import sys
import argparse
import ipaddress


def validate_port(port):
    try:
        port = int(port)
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"Le port spécifié '{port}' n'est pas un nombre entier valide."
        )

    if not (0 <= port <= 65535):
        raise argparse.ArgumentTypeError(
            f"Le port spécifié {port} n'est pas un port valide (de 0 à 65535)."
        )
    if port <= 1024:
        raise argparse.ArgumentTypeError(
            f"Le port spécifié {port} est un port privilégié. Spécifiez un port au-dessus de 1024."
        )

    return port


def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip not in [
            ip[4][0] for ip in socket.getaddrinfo(socket.gethostname(), None)
        ]:
            raise argparse.ArgumentTypeError(
                f"L'adresse {ip} n'est pas l'une des adresses IP de cette machine."
            )
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"L'adresse {ip} n'est pas une adresse IP valide."
        )
    return ip


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--port",
        type=validate_port,
        default=13337,
        help="Numéro de port (défaut: 13337).",
    )
    parser.add_argument(
        "-l", "--listen", type=validate_ip, help="Adresse IP sur laquelle écouter."
    )

    args = parser.parse_args()

    host = args.listen if args.listen else ""
    port = args.port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"Serveur en attente de connexions sur {host}:{port}...")

    conn, addr = s.accept()
    print(f"Un client vient de se connecter, son IP c'est {addr[0]}.")

    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break

            decoded_data = data.decode("utf-8")
            print(f"Données reçues du client : {decoded_data}")

            if "meo" in decoded_data.lower():
                response = "Meo à toi confrère."
            elif "waf" in decoded_data.lower():
                response = "ptdr t ki"
            else:
                response = "Mes respects humble humain."

            conn.sendall(response.encode("utf-8"))

        except socket.error as e:
            print(f"Une erreur est survenue : {e}")
            break
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            break

    conn.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
