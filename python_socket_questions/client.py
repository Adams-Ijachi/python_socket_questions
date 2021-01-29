import socket
import threading
from colorama import init , Fore 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
init()

ip = "127.0.0.1"
port = 12345
client_socket.connect((ip, port))

def recive_msg():
    while True:
        message = client_socket.recv(1024).decode('utf-8').strip(' ')
        print(message)



def write_msg():
    while True:
        msg = input('')
        if msg:
            client_socket.send(bytes(msg, "utf-8"))




recive_msg_thread = threading.Thread(target=recive_msg)
recive_msg_thread.start()

write_msg_thread = threading.Thread(target=write_msg)
write_msg_thread.start()