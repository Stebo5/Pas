import argparse
import socket
from typing import Iterator

from socket_client import SocketClient, SocketError


def tcp_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    return sock


def udp_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    return sock


def get_input() -> tuple[str, int]:
    parser = argparse.ArgumentParser()

    parser.add_argument('--port')
    parser.add_argument('--hostname')
    parser.add_argument('--ip')

    args = parser.parse_args()

    if args.ip is None and args.hostname is None:
        parser.exit(message='No ip or hostname provided')

    if args.ip is not None and args.hostname is not None:
        parser.exit(message='Both hostname and ip cannot be provided')

    if args.hostname is not None:
        ip = args.hostname
    else:
        ip = args.ip

    if args.port is not None:
        port = int(args.port)
    else:
        port = None

    return ip, port


def available_ports(ip: str) -> Iterator[int]:
    max_port = (1 << 16) - 1
    for port in range(0, max_port):
        try:
            SocketClient(port, ip=ip)
            yield port
        except SocketError:
            continue


def chunked(s: str, size: int) -> Iterator[str]:
    for i in range(0, len(s), size):
        chunk = s[i:i + size]
        if len(chunk) < size:
            yield chunk.ljust(size)
            return
        yield chunk
