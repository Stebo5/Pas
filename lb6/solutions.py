import base64
import smtplib
import socket
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'interia.pl'
SMTP_PORT = 587
CRLF = b'\r\n'


def ex1():
    """
    telnet interia.pl 587
    EHLO example.com
    MAIL FROM: <nadawca@gmail.com>
    RCPT TO: <odbiorca@interia.pl>
    DATA
    To: <odbiorca@interia.pl>
    From: <nadawca@gmail.com>
    Subject: Subject
    Body
    .
    QUIT
    """


def ex2():
    """
    telnet interia.pl 587
    EHLO example.com
    MAIL FROM: <nadawca@gmail.com>
    RCPT TO: <odbiorca1@interia.pl>
    RCPT TO: <odbiorca2@interia.pl>
    DATA
    To: <odbiorca1@interia.pl>, <odbiorca2@interia.pl>
    From: <nadawca@gmail.com>
    Subject: Subject
    Body
    .
    QUIT
    """


def ex4():
    """
    telnet interia.pl 587
    EHLO example.com
    MAIL FROM: <nadawca@gmail.com>
    RCPT TO: <odbiorca@interia.pl>
    DATA
    To: <odbiorca@interia.pl>
    From: <nadawca@gmail.com>
    Subject: Subject
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary="boundary-string"

    --boundary-string
    Content-Type: text/plain; charset="UTF-8"
    Content-Transfer-Encoding: quoted-printable

    Body

    --boundary-string
    Content-Type: text/plain; charset="UTF-8"
    Content-Disposition: attachment; filename="file.txt"
    Content-Transfer-Encoding: base64

    <cat file.txt | openssl base64>

    --boundary-string--
    .
    QUIT
    """


def ex5():
    """
    telnet interia.pl 587
    EHLO example.com
    MAIL FROM: <nadawca@gmail.com>
    RCPT TO: <odbiorca@interia.pl>
    DATA
    To: <odbiorca@interia.pl>
    From: <nadawca@gmail.com>
    Subject: Subject
    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary="boundary-string"

    --boundary-string
    Content-Type: text/plain; charset="UTF-8"
    Content-Transfer-Encoding: quoted-printable

    Body

    --boundary-string
    Content-Type: image/jpeg
    Content-Disposition: attachment; filename="image.jpeg"
    Content-Transfer-Encoding: base64

    <cat image.jpeg | openssl base64>

    --boundary-string--
    .
    QUIT
    """


def ex6():
    sender = input("Enter your email address: ")
    password = input("Enter your password: ")
    recipient = input("Enter recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject

    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender, password)

        server.send_message(message)
        print("Email sent successfully!")

    except Exception as e:
        print(f"Sending the email failed: {e}")

    finally:
        server.quit()


def smtp_send(sock, command):
    sock.sendall(command.encode() + CRLF)
    response = sock.recv(1024).decode()
    print(response)


def ex7():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    attachment_file = input("Enter attachment file path: ")

    with open(attachment_file, 'rb') as file:
        attachment_data = file.read()
    attachment_encoded = base64.b64encode(attachment_data).decode('utf-8')

    boundary = 'boundary-string'
    email = (
        f'From: {sender}{CRLF}'
        f'To: {recipient}{CRLF}'
        f'Subject: {subject}{CRLF}'
        f'MIME-Version: 1.0{CRLF}'
        f'Content-Type: multipart/mixed; boundary={boundary}{CRLF * 2}'
        f'--{boundary}{CRLF}'
        f'Content-Type: text/plain; charset=utf-8{CRLF}'
        f'Content-Disposition: inline{CRLF * 2}'
        f'{body}{CRLF}'
        f'--{boundary}{CRLF}'
        f'Content-Type: text/plain; charset=utf-8{CRLF}'
        f'Content-Disposition: attachment; filename=\"{attachment_file}\"{CRLF}'
        f'Content-Transfer-Encoding: base64{CRLF * 2}'
        f'{attachment_encoded}{CRLF * 2}'
        f'--{boundary}{CRLF}'
    )

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SMTP_SERVER, SMTP_PORT))
        response = client_socket.recv(1024).decode()
        print(response)

        smtp_send(client_socket, 'EHLO example.com')
        smtp_send(client_socket, 'STARTTLS')
        smtp_send(client_socket,
                  f'AUTH LOGIN {base64.b64encode(username.encode()).decode()}')
        smtp_send(client_socket,
                  f'{base64.b64encode(password.encode()).decode()}')
        smtp_send(client_socket, f'MAIL FROM: <{sender}>')
        smtp_send(client_socket, f'RCPT TO: <{recipient}>')
        smtp_send(client_socket, 'DATA')
        client_socket.sendall(email.encode())
        smtp_send(client_socket, 'QUIT')

        print("Email sent successfully!")

    except Exception as e:
        print(f"Sending the email failed: {e}")

    finally:
        client_socket.close()


def ex8():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")
    attachment_file = input("Enter attachment file path: ")

    with open(attachment_file, 'rb') as file:
        attachment_data = file.read()
    attachment_encoded = base64.b64encode(attachment_data).decode('utf-8')

    boundary = 'boundary-string'
    email = (
        f'From: {sender}{CRLF}'
        f'To: {recipient}{CRLF}'
        f'Subject: {subject}{CRLF}'
        f'MIME-Version: 1.0{CRLF}'
        f'Content-Type: multipart/mixed; boundary={boundary}{CRLF * 2}'
        f'--{boundary}{CRLF}'
        f'Content-Type: text/plain; charset=utf-8{CRLF}'
        f'Content-Disposition: inline{CRLF * 2}'
        f'{body}{CRLF}'
        f'--{boundary}{CRLF}'
        f'Content-Type: image/png{CRLF}'
        f'Content-Disposition: attachment; filename=\"{attachment_file}\"{CRLF}'
        f'Content-Transfer-Encoding: base64{CRLF * 2}'
        f'{attachment_encoded}{CRLF * 2}'
        f'--{boundary}{CRLF}'
    )

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SMTP_SERVER, SMTP_PORT))
        response = client_socket.recv(1024).decode()
        print(response)

        smtp_send(client_socket, 'EHLO example.com')
        smtp_send(client_socket, 'STARTTLS')
        smtp_send(client_socket,
                  f'AUTH LOGIN {base64.b64encode(username.encode()).decode()}')
        smtp_send(client_socket,
                  f'{base64.b64encode(password.encode()).decode()}')
        smtp_send(client_socket, f'MAIL FROM: <{sender}>')
        smtp_send(client_socket, f'RCPT TO: <{recipient}>')
        smtp_send(client_socket, 'DATA')
        client_socket.sendall(email.encode())
        smtp_send(client_socket, 'QUIT')

        print("Email sent successfully!")

    except Exception as e:
        print(f"Sending the email failed: {e}")

    finally:
        client_socket.close()


def ex9():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    sender = input("Enter sender email address: ")
    recipient = input("Enter recipient email address: ")
    subject = input("Enter email subject: ")
    body = input("Enter email body: ")

    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.add_alternative(body, subtype='html')

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(username, password)
        server.send_message(message)
    print("Email sent successfully!")


def ex10():
    def handler(client_socket):
        client_address = client_socket.getpeername()
        print("Accepted connection from:", client_address)

        server_greeting = "220 SMTP Server\r\n"
        client_socket.sendall(server_greeting.encode())

        while True:
            client_data = client_socket.recv(1024).decode()
            if not client_data:
                break
            print("Received:", client_data.strip())

            if client_data.startswith("QUIT"):
                response = "221 Bye\r\n"
                client_socket.sendall(response.encode())
                break
            elif client_data.startswith("HELO") or client_data.startswith(
                    "EHLO"):
                response = f"250 Hello {client_address[0]}\r\n"
                client_socket.sendall(response.encode())
            elif client_data.startswith("MAIL FROM:"):
                response = "250 OK\r\n"
                client_socket.sendall(response.encode())
            elif client_data.startswith("RCPT TO:"):
                response = "250 OK\r\n"
                client_socket.sendall(response.encode())
            elif client_data.startswith("DATA"):
                response = "354 Start mail input; end with <CRLF>.<CRLF>\r\n"
                client_socket.sendall(response.encode())

                while True:
                    email_data = client_socket.recv(1024).decode()
                    if email_data.strip() == ".":
                        break
                response = "250 OK\r\n"
                client_socket.sendall(response.encode())
            else:
                response = "500 Command not recognized\r\n"
                client_socket.sendall(response.encode())

        client_socket.close()
        print("Connection closed for:", client_address)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", SMTP_PORT))
    server_socket.listen(1)

    print("SMTP mail server is running on port", SMTP_PORT)

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            handler(client_socket)

    except KeyboardInterrupt:
        print("SMTP mail server stopped.")

    finally:
        server_socket.close()
