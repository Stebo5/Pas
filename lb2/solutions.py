import re
import socket
from io import StringIO

import utils
from utils import SocketClient, SocketError


def ex1():
    sc = SocketClient(13, hostname='ntp.task.gda.pl')
    data = sc.recv()
    print(data)


def ex2():
    sc = SocketClient(2900, ip='127.0.0.1')
    message = input()
    sc.send(message)
    data = sc.recv()
    print(data)


def ex3():
    sc = SocketClient(2900, ip='127.0.0.1')
    while True:
        try:
            data = input()
            sc.send(data)
            print(sc.recv())
        except EOFError:
            break


def ex4():
    sc = SocketClient(2901, ip='127.0.0.1', socket_type=socket.SOCK_DGRAM)
    message = input()
    sc.send(message)
    data = sc.recv()
    print(data)


def ex5():
    sc = SocketClient(2901, ip='127.0.0.1', socket_type=socket.SOCK_DGRAM)
    while True:
        try:
            data = input()
            sc.send(data)
            print(sc.recv())
        except EOFError:
            break


def ex6():
    pattern = re.compile(r'(\d+)\s*([+-\\*/])\s*(\d+)')
    operation = input('Enter an operation:')
    lhs, op, rhs = pattern.match(operation).groups()
    sc = SocketClient(2902, ip='127.0.0.1', socket_type=socket.SOCK_DGRAM)
    sc.send(lhs)
    sc.send(op)
    sc.send(rhs)
    result = sc.recv()
    print(result)


def ex7():
    ip, port = utils.get_input()
    try:
        SocketClient(port, ip=ip)
        print(f'Successfully connected to {ip} on port {port}')
    except SocketError as e:
        print(e.message)
    try:
        service = socket.getservbyport(port, 'tcp')
        print(f'Available service: {service}')
    except OSError:
        print("No services available")


def ex8():
    ip, _ = utils.get_input()
    available_ports = utils.available_ports(ip)
    for port in available_ports:
        try:
            service = socket.getservbyport(port, 'tcp')
            print(f'Available service: {service}')
        except OSError:
            print("No services available")


def ex9():
    sc = SocketClient(2906, ip='127.0.0.1', socket_type=socket.SOCK_DGRAM)
    ip = input('Enter the IP:')
    sc.send(ip)
    print(f'The corresponding hostname is {sc.recv()}')


def ex10():
    sc = SocketClient(2907, ip='127.0.0.1', socket_type=socket.SOCK_DGRAM)
    hostname = input('Enter the hostname:')
    sc.send(hostname)
    print(f'The corresponding IP is {sc.recv()}')


def ex11():
    sc = SocketClient(2908, ip='127.0.0.1')
    message = input()

    message = message.ljust(20)[:20]

    sc.send(message)

    print(sc.recv(20))


def ex12():
    sc = SocketClient(2908, ip='127.0.0.1')
    message = input()

    chunks = utils.chunked(message, 20)

    data = StringIO()
    for chunk in chunks:
        sc.send(chunk)
        data.write(sc.recv(20))

    print(data.getvalue())
