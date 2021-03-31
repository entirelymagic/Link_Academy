import socket
import urllib.request


while True:
    input("Press enter to get a ticket code:")
    ticket_resp = urllib.request.urlopen('http://localhost:8005/insert')
    hdrs = ticket_resp.getheaders()
    print(hdrs)
    token = ticket_resp.read()
    print(f"Your ticket token is {token.decode('utf-8')}")


    # for i in range(1000):
    #     client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     client.connect(("localhost", 8005))
    #     client.send("GET /insert HTTP/1.1\r\n\r\n".encode("utf-8"))
    #     parts = client.recv(1024).decode("utf-8").splitlines()
    #     description = parts[0].split(" ")
    #     statusCode = description[1]
    #     if statusCode != "200":
    #         print("Invalid server response")
    #     else:
    #         ticketToken = parts[len(parts) - 1]
    #         print("Your ticket code: ", ticketToken)
    #     client.close()
