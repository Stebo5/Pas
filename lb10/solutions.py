import socket

HOST = 'ws://echo.websocket.org'
PORT = 80


def ex1():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: {}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
            "Sec-WebSocket-Protocol: chat\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        ).format(HOST)

        sock.send(request.encode())

        handshake_response = sock.recv(4096)
        print(handshake_response.decode())


def ex2(message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        request = (
            "GET / HTTP/1.1\r\n"
            "Host: {}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
            "Sec-WebSocket-Protocol: chat\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        ).format(HOST)

        sock.send(request.encode())

        handshake_response = sock.recv(4096)
        print(handshake_response.decode())

        frame = bytearray()
        frame.append(0x81)

        length = len(message)

        if length > 125:
            print('Message cannot be longer than 125 bytes')
            return

        frame.append(length)
        sock.send(frame + message.encode())
