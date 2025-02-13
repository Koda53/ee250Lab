import requests
import argparse
import pprint # For pretty printing

SERVER = 'http://localhost:5000'

def send_mail(recipient: str, sender: str, subject: str, body: str) -> bool:
    """
    Sends a mail entry to the server by making a POST request to the /mail endpoint.
    The JSON body of the request contains the following keys:
    - recipient
    - sender
    - subject
    - body
    
    Args:
        recipient (str): The recipient of the mail
        sender (str): The sender of the mail
        subject (str): The subject of the mail
        body (str): The body of the mail

    Returns:
        bool: True if the mail was sent successfully, False otherwise
    """
    mail_entry = {
        'recipient': recipient,
        'sender': sender,
        'subject': subject,
        'body': body,
    }
    response = requests.post(f'{SERVER}/mail', json=mail_entry)
    pprint.pprint(response.json())

def get_inbox(recipient: str) -> None:
    """TODO: fill out this docstring (using the send_mail docstring as a guide)

    Gets the inbox of the recipient by making a GET request to the /mail/inbox/{recipient} endpoint.
    Json body of the request contains the following keys:
    - list: list of dictionaires representing mail entries

    args: recipient (str): recipient of the mail

    returns: none
    """
    response = requests.get(f'{SERVER}/mail/inbox/{recipient}')
    pprint.pprint(response.json())

def get_sent(sender: str) -> None:
    """TODO: fill out this docstring (using the send_mail docstring as a guide)

    This gets the sent mail of the sender by making a GET request to the /mail/sent/{sender} endpoint
    The json body of the request containts the following keys:
    - list: a list of dictionaires representing the mail entires

    args: sender (str): sender of the mail

    returns: none
    """
    response = requests.get(f'{SERVER}/mail/sent/{sender}')
    pprint.pprint(response.json())

def get_mail(mail_id: str) -> None:
    """TODO: fill out this docstring (using the send_mail docstring as a guide)

    Gets the mail of the mail_id by making a GET request to the /mail/{mail_id} endpoint
    the json body of the request contains the folloiwng keys
    - mail_id
    - recipient
    - sender
    - subject
    - body

    Args: mail_id (str): id of the mail

    return: none
    """
    response = requests.get(f'{SERVER}/mail/{mail_id}')
    pprint.pprint(response.json())

def delete_mail(mail_id: str) -> None:
    """TODO: fill out this docstring (using the send_mail docstring as a guide)

    Deletes the mail of the mail_id by making a DELETE request to the /mail/{mail_id} endpoint
    the json body of the request contains the following keys:
    -mail_id

    args: mail_id (str): id of the mail

    returns: none
    """
    response = requests.delete(f'{SERVER}/mail/{mail_id}')
    pprint.pprint(response.json())

# Command Line Interface
# making CLIs with argparse may be helpful for you in the future
# see if you can understand what each line is doing
def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Mail Client')
    
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    send_parser = subparsers.add_parser('send', help='Send a mail')
    send_parser.add_argument('body', help='The body of the mail')
    send_parser.add_argument(
        '-t', "--to", 
        dest="recipient",
        help='The recipient of the mail'
    )
    send_parser.add_argument(
        '-f', "--from",
        dest="sender",
        help='The sender of the mail'
    )
    send_parser.add_argument(
        '-s', "--subject", 
        help='The subject of the mail', 
        default="No Subject"
    )

    inbox_parser = subparsers.add_parser('inbox', help='Get your inbox')
    inbox_parser.add_argument('-u', "--user", help='The recipient of the mail')

    sent_parser = subparsers.add_parser('sent', help='Get your sent mail')
    sent_parser.add_argument('-u', "--user", help='The sender of the mail')

    get_parser = subparsers.add_parser('get', help='Get a mail')
    get_parser.add_argument('mail_id', help='The id of the mail')

    delete_parser = subparsers.add_parser('delete', help='Delete a mail')
    delete_parser.add_argument('mail_id', help='The id of the mail')

    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.command == 'send':
        send_mail(args.recipient, args.sender, args.subject, args.body)
    elif args.command == 'inbox':
        get_inbox(args.user)
    elif args.command == 'sent':
        get_sent(args.user)
    elif args.command == 'get':
        get_mail(args.mail_id)
    elif args.command == 'delete':
        delete_mail(args.mail_id)

# TODO: run the code!
# to run the code, open a terminal and type:
#   python mail_client.py --help
# For example, to send a mail, type:
#   python mail_client.py send -t "recipient" -f "sender" -s "subject" "body"
# you'll need to demo sending, receiving, and deleting mail for checkoff.
if __name__ == '__main__':
    main()

