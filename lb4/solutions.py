import socket
from datetime import datetime

from socket_client import SocketClient
from utils import tcp_socket, udp_socket

LOCALHOST = 'localhost'
PORT = 4200


def ex1():
    with tcp_socket(LOCALHOST, PORT) as sock:
        sock.listen(1000)
        while True:
            connection, address = sock.accept()
            try:
                while True:
                    data = connection.recv(1024).decode()
                    print(data)
                    if data:
                        connection.sendall(
                            (str(datetime.utcnow()).encode()))
                        break
            except:
                pass


def ex2():
    with tcp_socket(LOCALHOST, PORT) as sock:
        sock.listen(1000)
        while True:
            connection, address = sock.accept()
            try:
                while True:
                    data = connection.recv(1024).decode()
                    print(data)
                    if data:
                        connection.sendall(
                            (str(data).encode()))
                        break
            except:
                pass


def ex3():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                while True:
                    data, address = sock.recvfrom(1024)
                    data = data.decode("utf-8")
                    print(data)
                    if data:
                        sock.sendto((str(data).encode("utf-8")), address)
                        break
            except:
                pass


def ex4():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                while True:
                    data, address = sock.recvfrom(1024)
                    data = data.decode("utf-8")
                    print(data)
                    if data:
                        sock.sendto((str(eval(data)).encode("utf-8")), address)
                        break
            except:
                pass


def ex5():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                while True:
                    data, address = sock.recvfrom(1024)
                    data = data.decode("utf-8")
                    print(data)
                    if data:
                        sock.sendto(
                            (str(socket.gethostbyaddr(data)).encode("utf-8")),
                            address)
                        break
            except:
                pass


def ex6():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                while True:
                    data, address = sock.recvfrom(1024)
                    data = data.decode("utf-8")
                    print(data)
                    if data:
                        sock.sendto(
                            (str(socket.gethostbyname(data)).encode("utf-8")),
                            address)
                        break
            except:
                pass


def ex7():
    sc = SocketClient(2900, ip='127.0.0.1')
    message = input()
    sc.send(message[:20])
    data = sc.recv()
    print(data)


def ex9():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                data, address = sock.recvfrom(1024)
                data = data.decode("utf-8").split(";")
                match data:
                    case ["zad14odp", "src", "60788", "dst", "2901", "data",
                          "programming in python is fun"]:
                        sock.sendto("TAK".encode("utf-8"), address)
                    case ["zad14odp", "src", _, "dst", _, "data", _]:
                        sock.sendto("NIE".encode("utf-8"), address)
                    case _:
                        sock.sendto("BAD SYNTAX".encode("utf-8"), address)
            except:
                break


def ex10():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                data, address = sock.recvfrom(1024)
                data = data.decode("utf-8").split(";")
                match data:
                    case ["zad13odp", "src", "2900", "dst", "35211", "data",
                          "hello :)"]:
                        sock.sendto("TAK".encode("utf-8"), address)
                    case ["zad13odp", "src", _, "dst", _, "data", _]:
                        sock.sendto("NIE".encode("utf-8"), address)
                    case _:
                        sock.sendto("BAD SYNTAX".encode("utf-8"), address)
            except:
                break


def ex11():
    with udp_socket(LOCALHOST, PORT) as sock:
        while True:
            try:
                data, address = sock.recvfrom(1024)
                data = data.decode("utf-8").split(";")
                match data:
                    case ["zad15odpA", "ver", "4", "srcip", "212.182.24.27",
                          "dstip",
                          "192.168.0.2", "type", "6"]:
                        sock.sendto("TAK".encode("utf-8"), address)
                    case ["zad15odpA", "ver", _, "srcip", _, "dstip",
                          _, "type", _]:
                        sock.sendto("NIE".encode("utf-8"), address)
                    case _:
                        sock.sendto("BAD SYNTAX".encode("utf-8"), address)

                data, address = sock.recvfrom(1024)
                data = data.decode("utf-8").split(";")
                match data:
                    case ["zad15odpB", "srcport", "2900", "dstport", "4752",
                          "data",
                          "network programming is fun"]:
                        sock.sendto("TAK".encode("utf-8"), address)
                    case ["zad15odpB", "srcport", _, "dstport", _, "data",
                          _]:
                        sock.sendto("NIE".encode("utf-8"), address)
                    case _:
                        sock.sendto("BAD SYNTAX".encode("utf-8"), address)
            except:
                break
