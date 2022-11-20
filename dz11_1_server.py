# Socket Communicatiion
# First Attemp
# Server

import socket

sock_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_com.bind(('127.0.0.1', 55000))

sock_com.listen(10)

print("I am waiting for your message.")
# Endless cycle for communication with the client
while True:
    # If you want to interrupt a cycle press Q
    signal_to_stop = input("\nTo stop connection, press Q\nTo continue connection, press any symbol: ")
    if signal_to_stop != "Q":
        # Sending and connection
        conn, address = sock_com.accept()
        print('\nconnected:', address)
        sending_data = conn.recv(1024)
        print(str(sending_data))

        # The letters are reversed
        #conn.send(sending_data.swapcase())

        # Returning message with adding words
        adding_words = b", my dear client"
        conn.send(sending_data + adding_words)
    else:
        break

    conn.close()