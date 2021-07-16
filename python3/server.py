import socket

#server = socket.gethostname()
server = "192.168.0.9"
port = 8080

print(f"server is {server}. port no is {port}.start service.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))  # IPとポート番号を指定します
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", 'utf-8'))
    clientsocket.close()