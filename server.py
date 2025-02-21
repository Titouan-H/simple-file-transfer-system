import socket
import threading

#TODO : change host value to local adress or 0.0.0.0 for every connexions
HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET for IPv4
#SOCK_STREAM for TCP socket

server_socket.bind((HOST,PORT))

client_socket, client_adress = server_socket.accept()
print(f"Connexion from {client_adress}")

message = client_socket.recv(1024).decode("utf-8")
print(f"Message received from client :\n{message}")

client_socket.close()
server_socket.close()
