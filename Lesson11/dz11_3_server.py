# Socket Communicatiion
# Third Attemp
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

        # Convertation from byte type to string type
        client_message = sending_data.decode()
        # Counting words in phrase
        phrase_lenth = len(client_message.split())
        # Convertation from interger type to string type
        l = "There are " + str(phrase_lenth) + " words in your phrase."
        print(l)
        # Convertation from string type to byte type
        b_phrase_lenth = l.encode()
        print(b_phrase_lenth)

        conn.send(b_phrase_lenth)
    else:
        break

    conn.close()
