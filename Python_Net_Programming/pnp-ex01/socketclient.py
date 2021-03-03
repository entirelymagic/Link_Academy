import socket

# create socket
sClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to server
print('Try to connect')
sClient.connect(("10.20.40.31", 8005))

# set some data to send
data = "Salut Dragos!! \n"
# send data to server
sClient.send(data.encode())
sClient.sendall(data.encode())

sClient.close()
