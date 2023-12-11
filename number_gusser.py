import socket
import threading

# Define server address and port
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 8000

# Create a new socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Function to handle incoming messages from the server
def handle_messages():
    while True:
        message = client_socket.recv(1024)
        print(message.decode())

# Start a new thread to handle incoming messages
message_thread = threading.Thread(target=handle_messages)
message_thread.start()

# Send messages to the server
while True:
    message = input("Enter message: ")
    client_socket.send(message.encode())
