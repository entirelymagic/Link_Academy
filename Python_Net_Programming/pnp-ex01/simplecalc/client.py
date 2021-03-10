import socket

# Open Socket
cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect(("10.20.40.191", 8005))

# create the first answer
firstNum = input(cSocket.recv(256).decode("utf-8"))
# send the first answer
cSocket.send(bytes(firstNum, "utf-8"))

# create second answer
secondNum = input(cSocket.recv(256).decode("utf-8"))
# send the second answer
cSocket.send(bytes(secondNum, "utf-8"))

# print the result received from the server
print("Result is: ", cSocket.recv(256).decode("utf-8"))
