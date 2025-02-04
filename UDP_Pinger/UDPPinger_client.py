# Importing module
import time
import socket

# Create the server address and port
server_addr = ("127.0.0.1", 12000)


# create the udp socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)  # set timeout to 1 second


# Record the send time
for sequence_number in range(1, 11):
    send_time = time.time()
    message = f' Hey, I am Ping {sequence_number}, {send_time}'

    try:
        # send message to the server
        client_socket.sendto(message.encode(), server_addr)

        # Waiting and Receiving a response
        response, _ = client_socket.recvfrom(1024)
        receive_time = time.time()

        rtt = receive_time - send_time

        print(f"Received: {response.decode()} | RTT:{rtt:.6f} sec")

    except socket.timeout:
        print("Request Timed out")


# close the socket
client_socket.close()
