import socket


def sendmsg(data):
    msg = [0b10000001]
    msg.append(len(data))
    full_msg = bytearray(msg) + data
    global client
    client.send(full_msg)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8005))
msg = "GET / HTTP/1.1\r\n" + \
      "Host: localhost:8005\r\n" + \
      "Connection: Upgrade\r\n" + \
      "Upgrade: websocket\r\n" + \
      "Sec-WebSocket-Version: 13\r\n" + \
      "Sec-WebSocket-Key: AVa5oKdJHwm4EAPvxWEqkw==\r\n\r\n"

client.send(msg.encode("utf-8"))
print(client.recv(1024))

while True:
    msg = input("Message: ")
    sendmsg(msg.encode("utf-8"))
    res = client.recv(1024)
    print((res[2:len(res)]).decode("utf-8"))
