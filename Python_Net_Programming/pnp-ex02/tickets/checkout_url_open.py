import socket
import urllib.request, urllib.error
from urllib.request import HTTPRedirectHandler

while True:
    try:
        ticketCode = input("Scan or enter ticket code:")
        body = urllib.request.urlopen('http://localhost:8005/checkout', ticketCode.encode("ascii"))
        message = body.read().decode("ascii")

        if body.status != 200:
            print("Invalid server response")
        else:
            if message == "True":
                print("Ticket is valid..open the door")
            else:
                print("Ticket is not valid, do not open the door")
    except urllib.error.HTTPError as e:
        print(f'HTTP Error {e.code}: {e.msg}')


    # ticketCode = input("Scan or enter ticket code:")
    # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client.connect(("localhost", 8005))
    # client.send(f"POST /checkout HTTP/1.1\r\n\r\n{ticketCode}".encode("utf-8"))
    # parts = client.recv(1024).decode("utf-8").splitlines()
    # description = parts[0].split(" ")
    # statusCode = description[1]
    # if statusCode != "200":
    #     print("Invalid server response")
    # else:
    #     body = parts[len(parts) - 1]
    #     if body == "True":
    #         print("Ticket is valid..open the door")
    #     else:
    #         print("Ticket is not valid, do not open the door")
