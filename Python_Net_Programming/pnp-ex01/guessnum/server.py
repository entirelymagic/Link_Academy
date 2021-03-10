import socket
import random

# create Socket
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# accept connection from any connection
sSocket.bind(("0.0.0.0", 8005))
sSocket.listen()
print('Server is listening...')
userSocket, addr = sSocket.accept()

player_number = int(userSocket.recv(128).decode("utf-8"))
comp_number = random.randint(1, 5)

# send a message
if player_number == comp_number:
    userSocket.send(b"Nice! I guessed that number")
else:
    userSocket.send(f"Wrong! I guessed {comp_number} and you typed {player_number}".encode("utf-8"))
