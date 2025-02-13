"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

HOST = "192.168.0.118"
PORT = 56789

def main():
    # DONE: Create a socket and connect it to the server at the designated IP and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # DONE: Get user input and send it to the server using your TCP socket
    user_in = input("Input something to send to the server: ")
    s.sendall(str.encode(user_in))
    # DONE: Receive a response from the server and close the TCP connection
    data = s.recv(256).decode("utf-8")
    print(data)
    s.close()


if __name__ == '__main__':
    main()