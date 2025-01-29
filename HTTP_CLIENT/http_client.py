import sys
import socket


def http_client(server_addr, server_port, filename):
    try:
        # create a socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # connect to server
        client_socket.connect((server_addr, int(server_port)))

        # create an HTTP GET request
        request = f"GET {
            filename} HTTP/1.1\r\nHost: {server_addr}\r\nconnection: close\r\n\r\n"

        # send the request
        client_socket.sendall(request.encode())

        # Receive and Display the response
        response = b" "
        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break

            response += chunk

            print(response.decode(errors="ignore"))

        # close the connection
        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_addr> <server_port> <filename>")

    else:
        http_client(sys.argv[1], sys.argv[2], sys.argv[3])
