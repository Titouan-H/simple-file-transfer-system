import socket
import threading

#TODO : change host value to local adress or 0.0.0.0 for every connexions
HOST = "127.0.0.1"
PORT = 5000

def handle_client(client_socket,address):
  print(f"[+] Established connection with {address}")
  try :
    message = client_socket.recv(1024).decode()
    print(message)
  except Exception as E :
    print(f"[!] Something went wrong : \n{E}")

  client_socket.close()

def start_server():
  print(f"Starting server on host {HOST} and port {PORT}")
  server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  server_socket.bind((HOST,PORT))
  server_socket.listen(5)

  while True :
    client_socket, address = server_socket.accept()
    client_handler = threading.Thread(target=handle_client, 
      args = (client_socket,address))
    client_handler.start()

    
if __name__ == "__main__":
  start_server()