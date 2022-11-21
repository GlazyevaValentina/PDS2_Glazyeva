import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
a = input("Enter number A: ")
b = input("Enter number B: ")
n = f'{a} {b}'
sock.send(bytes(str(n), encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data.decode('UTF-8'))