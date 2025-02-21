import socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


#server ip and port
#TODO : change
HOST = "127.0.0.1"
PORT = 5000

client_socket.connect((HOST,PORT))

message = "Hello, world!"
client_socket.send(message.encode("utf-8"))

client_socket.close()