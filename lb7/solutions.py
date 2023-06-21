import email
import poplib

SERVER = 'interia.pl'
PORT = 110
USER = 'pas2017@interia.pl'
PASS = 'P4SInf2017'


def ex1():
    """
    telnet SERVER PORT
    USER USER
    PASS PASS
    LIST
    QUIT
    """


def ex2():
    """
    telnet SERVER PORT
    USER USER
    PASS PASS
    LIST
    QUIT
    """


def ex3():
    """
    telnet SERVER PORT
    USER USER
    PASS PASS
    LIST
    QUIT
    """


def ex4():
    """
    telnet SERVER PORT
    USER USER
    PASS PASS
    RETR largest_message
    LIST
    QUIT
    """


def ex5():
    """
    telnet SERVER PORT
    USER USER
    PASS PASS
    DELE smallest_message
    LIST
    QUIT
    """


def ex6():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        count = len(pop_conn.list()[1])

        print(f'Message count: {count}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()


def ex7():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        total_bytes = pop_conn.stat()[1]

        print(f'Total bytes: {total_bytes}')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()


def ex8():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        response = pop_conn.list()[1]

        for msg in response:
            number, size = msg.decode().split()
            print(f'Message {number}: {size} bytes')

    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()


def ex9():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        response = pop_conn.list()[1]

        largest_size = 0
        largest_number = None

        for msg in response:
            number, size = msg.decode().split()
            size = int(size)
            if size > largest_size:
                largest_size = size
                largest_number = number

        if largest_number is None:
            print('No messages found in inbox')
            return
        response = pop_conn.retr(largest_number)[1]
        print(b'\n'.join(response).decode())

    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()


def ex10():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        response = pop_conn.list()[1]

        for msg in response:
            number, _ = msg.decode().split()

            r = pop_conn.retr(number)[1]
            content = b'\n'.join(r).decode()
            print(content)
            print('-' * 20)

    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()


def ex11():
    try:
        pop_conn = poplib.POP3(SERVER, PORT)
        pop_conn.user(USER)
        pop_conn.pass_(PASS)
        response = pop_conn.list()[1]

        for msg in response:
            number, _ = msg.decode().split()
            response = pop_conn.retr(number)[1]
            content = b"\n".join(response).decode()

            email_message = email.message_from_string(content)

            for part in email_message.walk():
                if part.get_content_type().startswith('image/'):
                    filename = part.get_filename()

                    if filename:
                        with open(filename, 'wb') as file:
                            file.write(part.get_payload(decode=True))
                        print(f"Saved attachment: {filename}")

    except Exception as e:
        print(f'Error: {e}')
    finally:
        pop_conn.quit()
