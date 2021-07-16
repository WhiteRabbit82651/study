import socket

#server = socket.gethostname()
server = "192.168.0.18"
port = 8080

print(f"server is {server}. port no is {port}.start connection.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, port))



full_msg = b''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg

print(full_msg.decode("utf-8"))