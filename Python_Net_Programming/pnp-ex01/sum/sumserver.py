import socket

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sSocket.bind(("0.0.0.0", 8005))
sSocket.listen()

# THis will start the server
while True:

    client, addr = sSocket.accept()
    info_message = """
    Enter numbers to be added:
    For each number press enter.
    When you would like to see the total press enter as a blank line. \n 
    """
    client.send(info_message.encode("utf-8"))
    sum = 0
    while True:
        try:
            val = client.recv(128).decode("utf-8")
            if val == "#":
                client.send(f"{sum}".encode("utf-8"))
                break
            else:
                sum += int(val)
        except ValueError:
            client.send("YOu have entered invalid value".encode("utf-8"))
    client.close()
