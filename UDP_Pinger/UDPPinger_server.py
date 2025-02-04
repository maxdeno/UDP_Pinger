
# We will need the following module to generate randomized lost packets
import random
import signal
from socket import *
import sys


# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets

serverSocket = socket(AF_INET, SOCK_DGRAM)


# Assign IP address and port number to socket

serverSocket.bind(('0.0.0.0', 12000))
print(f"connection running and waiting for connections...")


try:
    while True:

     # Generate random number in the range of 0 to 10
        rand = random.randint(0, 10)
        print(f"Generated random number: {rand}")

      # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        print(f"connection established by {address}")

      # Capitalize the message from the client
        message = message.upper()

     # If rand is less is than 4, we consider the packet lost and do not respond
        if rand < 4:
            print("Packet lost. Not responding!")
            continue

      # Otherwise, the server responds
        serverSocket.sendto(message, address)
        print("Response sent")

except Exception as e:
    print(f"Error: {e}")
    serverSocket.close()

except KeyboardInterrupt:
    print("\nPress Ctrl + C to exit...")
    sys.stdin.read()


def handle_exit(sig, frame):
    print("\nServer shutting down gracefully...")
    serverSocket.close()
    sys.exit(0)

    signal.signal(signal.SIGINT, handle_exit)
