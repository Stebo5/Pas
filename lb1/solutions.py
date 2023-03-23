import ipaddress
import shutil
import socket
import sys

import utils


def ex1():
    filename = input("Enter the filename:")
    shutil.copy(filename, "lab1zad1.txt")


def ex2():
    filename = input("Enter the filename:")
    shutil.copy(filename, "lab1zad2.png")


def is_valid_ip(ip: str) -> bool:
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    return True


def ex3():
    ip = input("Enter the IP address:")
    print(is_valid_ip(ip))


def ex4():
    if len(sys.argv) < 1:
        return

    ip = sys.argv[1]
    hostname, *_ = socket.gethostbyaddr(ip)
    print(hostname)


def ex5():
    if len(sys.argv) < 1:
        return

    hostname = sys.argv[1]
    ip = socket.gethostbyname(hostname)
    print(ip)


def can_connect(address: tuple[str, int]) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        result = sock.connect_ex(address)

        if result != 0:
            return False
        return True
    finally:
        sock.close()


def ex6():
    ip, port = utils.get_input()

    if can_connect((ip, port)):
        print(f'Successfully connected to {ip} on port {port}')
        return
    print('Failed to connect')


def ex7():
    ip, _ = utils.get_input()
    available = utils.available_ports(ip)
    print(f'Available ports: {list(available)}')
