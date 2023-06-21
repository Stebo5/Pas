import random

from utils import tcp_socket


def ex1():
    server_ip = '212.182.24.27'
    server_port = 2912

    with tcp_socket(server_ip, server_port) as sock:
        while True:
            guess = input("Enter your guess: ")
            if not guess.isdigit():
                print("Invalid number")
                continue

            sock.send(guess.encode('utf-8'))

            response = sock.recv(1024).decode('utf-8')
            if response == 'TAK':
                print(f"Congratulations! The number was {guess}")
                break
            else:
                print("Try again")


def ex2():
    server_ip = '127.0.0.1'
    server_port = 1234

    with tcp_socket(server_ip, server_port) as sock:
        sock.listen(100)

        connection, address = sock.accept()
        number = random.randint(0, 9)

        try:
            while True:
                data = connection.recv(1024).decode('utf-8')
                if not data.isdigit():
                    connection.send("Invalid number".encode('utf-8'))
                    continue

                guess = int(data)
                if guess < number:
                    response = "Higher"
                elif guess > number:
                    response = "Lower"
                else:
                    connection.send(
                        f"Congratulations! The number was {guess}".encode(
                            'utf-8'))
                    break
        finally:
            connection.close()
