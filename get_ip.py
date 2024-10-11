import psutil
import socket
import ipaddress

def get_ip():

    interfaces = psutil.net_if_addrs()
    ip_adresses = []

    ip_wifi= 'Wi-Fi'

    if ip_wifi in interfaces:
        for interface in interfaces[ip_wifi]:
            if interface.family == socket.AF_INET:
                ip_adresses.append(interface.address)

                netmask= interface.netmask
                network = ipaddress.IPv4Network(f"{interface.address}/{netmask}", strict=False)
                netmask_bits = network.prefixlen               
                print(f'{interface.address}/{netmask_bits}')

    if ip_adresses:
        total_ips = 2**(32 - netmask_bits) 
        print(f'{total_ips}')
    else:
        print('Adresse IP intconnue')

if __name__ == '__main__':
    get_ip()



