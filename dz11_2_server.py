# Socket Communicatiion
# Second Attemp
# Server

import socket

sock_com = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_com.bind(('127.0.0.1', 55000))

sock_com.listen(10)

print("I am waiting for your message.")
# Dictionary for communication
dict_for_communication = {
        'How are you?': 'Not bad',
        'What is up?': 'Nothing much',
        'How is it going?': 'Good'
    }
# Endless cycle for communication with the client
while True:

    # If you want to interrupt a cycle press Q
    signal_to_stop = input("\nTo stop connection, press Q\nTo continue connection, press any symbol: ")
    if signal_to_stop != "Q":
        # Sending and connection
        conn, address = sock_com.accept()
        print('\nconnected:', address)
        sending_data = conn.recv(1024)
        client_message = sending_data.decode()
        print(str(sending_data))
        print(client_message)

        # If server recieved undefined message, the programm is broken
        if client_message != "What is up?" and client_message != "How are you?" and client_message != "How is it going?":
            print("I do not understand you")
            conn.send(b"I do not understand you")
            break

        # Returning message from dictionary

        for key, value in dict_for_communication.items():

            if key == client_message:
                k = key
                sending_message = dict_for_communication[k]
                # Answer as string
                #print(sending_message)
                b_sending_message = sending_message.encode()
                #Answer as byte
                print(b_sending_message)

            else:
               print("That is all right witn me")

        conn.send(b_sending_message)

    else:
        break

conn.close()