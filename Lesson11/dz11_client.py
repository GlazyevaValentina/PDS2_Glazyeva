# Socket communicatiion

# Client
###########
# First Attemp (dz11_1): Hello, Hi, Good morning
###########
# Second Attemp (dz11_2): What is up? How are you? How is it going?
# Any other phrase causeses programme stop
###########
# Third Attemp (dz11_3)
# Any phrase
############
import socket

sock_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_com.connect(('localhost', 55000))
message = input("Enter your phrase: ")
sock_com.send(bytes(message, encoding='UTF-8'))
sending_data = sock_com.recv(1024)
sock_com.close()

print(sending_data)
