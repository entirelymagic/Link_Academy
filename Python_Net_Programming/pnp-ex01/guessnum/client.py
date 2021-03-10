import socket

# create socket
playerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
playerSocket.connect(("10.20.40.191", 8005))

# send a message
playerSocket.send(bytes(input("Enter number: "), "utf-8"))

# print the message received from server.
print(playerSocket.recv(128).decode("utf-8"))
