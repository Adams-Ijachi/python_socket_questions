import socket
import select
import threading
import random
import colorama
from colorama import init , Fore 

init()
print(Fore.RED+'hi')

HEADER = 10
IP = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((IP, PORT))

server.listen(5)

client_socket = []
client_nickname = []


questions_list = ['what is the capital of south africa ?','what is the capital of Nigeria ?','what is the capital of Egypt?','what is the capital of Ghana?','what is the capital of Cameroon','what is the capital of Uganda']

answer_list = ['petoria','abuja','cairo','accra','yaounde','kampala']


def handle_msg(client_socket):
    while questions_list:
        random_num = random.randrange(len(questions_list))
        client_socket.send(bytes(f'{questions_list[random_num]}', 'utf-8'))
        answer = client_socket.recv(1024).decode('utf-8').strip(' ').lower()
        if answer_list[random_num] != answer:
          
            client_socket.send(bytes(f'Incorrect {answer_list[random_num]}', 'utf-8'))
        else:
            client_socket.send(bytes(f'Correct !!', 'utf-8'))
        del questions_list[random_num]
        del answer_list[random_num]
        
    


def recive_connection():
    while True:
        client_socket , address = server.accept()

        client_socket.send(bytes(f'Please enter a nickname : ', 'utf-8'))
        nickname = client_socket.recv(1024).decode('utf-8').strip(' ')

        if nickname:
            client_nickname.append(nickname)
            client_socket.send(bytes(f'Welcome {client_nickname[0]} ', 'utf-8'))
            thread = threading.Thread(target=handle_msg, args=(client_socket,))
            thread.start()




recive_connection()



    


