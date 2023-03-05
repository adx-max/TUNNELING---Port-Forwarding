print('CREATED BY ANESTUS UDUME FROM BENTECH SECURITY')
import socket

# Define the local and remote ports to forward
local_port = 12345
remote_port = 80

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the local address and port
server_socket.bind(('localhost', local_port))

# Listen for incoming connections
server_socket.listen(1)

print(f'Listening on port {local_port}...')

while True:
    # Wait for a client connection
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    # Connect to the remote host
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect(('example.com', remote_port))

    # Forward data between the client and remote host
    while True:
        # Receive data from the client
        client_data = client_socket.recv(4096)
        if not client_data:
            break
        # Forward data to the remote host
        remote_socket.sendall(client_data)

        # Receive data from the remote host
        remote_data = remote_socket.recv(4096)
        if not remote_data:
            break
        # Forward data to the client
        client_socket.sendall(remote_data)

    # Close the sockets
    client_socket.close()
    remote_socket.close()
