import socket

# create Socket with protocol AF_INET
sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# create a bind, takes an ip and a port - Accept connection from all IP's
sSocket.bind(("0.0.0.0", 8005))
# start listening
sSocket.listen()
print("Server is listening...")
# accept socket
sSocket.accept()
print("It was pleasure")
sSocket.close()
