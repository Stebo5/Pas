import socket
from typing import Optional


class SocketError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class SocketClient:

    def __init__(
            self,
            port: int,
            ip: Optional[str] = None,
            hostname: Optional[str] = None,
            socket_type: socket.SocketKind = socket.SOCK_STREAM,
            timeout: float = 0.1
    ):
        self.sock = socket.socket(socket.AF_INET, socket_type)
        self.sock.settimeout(timeout)
        if ip is None:
            ip = socket.gethostbyname(hostname)
        result = self.sock.connect_ex((ip, port))
        if result != 0:
            raise SocketError('Failed to connect')

    def send(self, data: str):
        bytes_sent = self.sock.send(data.encode('utf-8'))
        if bytes_sent < len(data):
            raise SocketError('Failed to send all data')

    def recv(self, buf_size: int = 4096) -> str:
        data = self.sock.recv(buf_size)
        return data.decode('utf-8')

    def __del__(self):
        self.sock.close()
