import socket
import threading
import base64

import persistentFileHandler
import authentication_service


def accept(sock):
    conn, addr = sock.accept()
    hh = HttpHandler(conn)
    hh.daemon = True
    hh.start()


class HttpHandler(threading.Thread):
    sock = None

    def __init__(self, sock):
        super().__init__()
        self.sock = sock

    def run(self):
        request = self.sock.recv(1024).decode("utf-8")
        parts = request.split("\r\n")

        bodyData = parts[len(parts) - 1]

        description = parts[0].split(" ")
        resource = description[1].replace("/", "")
        method = description[0]
        code = "200 OK"
        user = None
        password = None
        body = None
        cache_control = "Cache-Control: no-store\r\n"
        www_auth_header = ""

        # we check the header in order to get the authentication header and decode the user and password.
        for header in parts:
            if header.split(":")[0] == "Authorization":
                if " " in header and len(header.split(" ")) == 3:
                    encoded_credentials = header.split(" ")[-1]
                    decoded_credentials = base64.b64decode(encoded_credentials).decode("ascii")
                    user = decoded_credentials.split(":")[0]
                    password = decoded_credentials.split(":")[1]

        if not resource:
            body = "This is not a valid page"
            code = "404 Not Found"
        else:
            if resource == "insert":
                authenticated = False
                # TODO authenticator
                if user is not None and password is not None:
                    authenticated = authentication_service.authenticate(user, password)
                # now check if the user is authenticated
                if authenticated:
                    body = persistentFileHandler.insertticket()
                else:
                    code = "401 Unauthorized"
                    www_auth_header = "WWW-Authenticate: Basic realm='myapp'\r\n"
            elif resource == "checkout":
                if method.lower() != "post":
                    body = "You must use post method on this page"
                    code = "405 Method Not Allowed"
                elif not bodyData:
                    body = "Not a valid body"
                    code = "400 Bad Request"
                else:
                    print(f"Validating ticket {bodyData}")
                    if not bodyData.isnumeric():
                        body = "Not a valid ticket code"
                        code = "400 Bad Request"
                    else:
                        body = persistentFileHandler.checkout(bodyData)
                        if not body:
                            code = "400"
            else:
                body = "Not a valid command"
                code = "400 Bad Request"

            print(F"Returning {body}")
            protocol = "HTTP/1.1"
            self.sock.send(
                f"{protocol} {code}\r\n{cache_control}{www_auth_header}Content-Type: text/html\r\nConnection: Close\r\n\r\n{body}".encode("utf-8"))
            self.sock.close()


sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sSocket.bind(("localhost", 8005))
sSocket.listen()

while True:
    accept(sSocket)
