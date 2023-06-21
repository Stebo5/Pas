import email
import imaplib

SERVER = '212.182.24.27'
PORT = 143
USER = 'pasinf2017@infumcs.edu'
PASS = 'P4SInf2017'


def ex1():
    """
    telnet SERVER PORT
    LOGIN USER PASS
    LIST "" *
    SELECT INBOX
    SEARCH ALL
    FETCH 1 BODY[TEXT]
    STORE 1 +FLAGS (\\Seen)
    LOGOUT
    """


def ex2():
    with imaplib.IMAP4(SERVER, PORT) as imap_conn:
        imap_conn.login(USER, PASS)
        imap_conn.select('Inbox')
        _, response = imap_conn.status('Inbox', '(MESSAGES)')
        message_count = int(response[0].split()[2])
        print(f'Total messages in \'Inbox\': {message_count}')


def ex3():
    with imaplib.IMAP4(SERVER, PORT) as imap_conn:
        imap_conn.login(USER, PASS)

        _, mailbox_list = imap_conn.list()

        total_message_count = 0

        for mailbox in mailbox_list:
            _, mailbox_name = mailbox.decode().split(' "/" ')
            mailbox_name = mailbox_name.strip(' "')

            imap_conn.select(mailbox_name)

            _, response = imap_conn.status(mailbox_name, '(MESSAGES)')

            message_count = int(response[0].split()[2])

            total_message_count += message_count

        print(f"Total messages in all inboxes: {total_message_count}")


def ex4(inbox):
    with imaplib.IMAP4(SERVER, PORT) as imap_conn:
        imap_conn.select(inbox)
        _, message_nums = imap_conn.search(None, 'UNSEEN')

        if message_nums[0]:
            message_nums = message_nums[0].split()

            for num in message_nums:
                _, msg_data = imap_conn.fetch(num, '(RFC822)')
                raw_email = msg_data[0][1]

                email_message = email.message_from_bytes(raw_email)
                print(email_message.get_payload())

                imap_conn.store(num, '+FLAGS', '\\Seen')

                print('-' * 20 + '\n')

            print(f"Total unread messages: {len(message_nums)}")
        else:
            print("No unread messages in the Inbox.")


def ex5(inbox, to_delete):
    with imaplib.IMAP4(SERVER, PORT) as imap_conn:
        imap_conn.select(inbox)
        _, message_nums = imap_conn.search(None, 'ALL')

        if message_nums[0]:
            message_nums = message_nums[0].split()

            if str(to_delete).encode() in message_nums:
                imap_conn.store(str(to_delete), '+FLAGS', '\\Deleted')
                imap_conn.expunge()
                print(f"Message {to_delete} deleted successfully.")
            else:
                print(f"Message {to_delete} not found in the Inbox.")
        else:
            print("No messages in the Inbox.")
