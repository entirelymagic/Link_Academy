import socket
import random

objects = {1: "Paper", 2: "Stone", 3: "Scissors"}
selection = random.randint(1, 3)
selectedObject = objects[selection]
print("I select ", selectedObject)
gameServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gameServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
gameServer.bind(("0.0.0.0", 8005))
gameServer.listen()
conn, addr = gameServer.accept()

msg = ""
for k in objects:
    msg += f"{k} = {objects[k]}\n"
conn.send(bytes(msg, "utf-8"))

clientSelection = int(conn.recv(10))
clientSelectedObject = objects[clientSelection]
print(f"Player selected {clientSelectedObject}")
conn.send(bytes(f"You selected {clientSelectedObject}\n "
                f"I select {selectedObject}\n", "utf-8"))

if clientSelection == selection:
    print("Draw game")
    conn.send(b"Draw game\n")
elif clientSelection - 1 == selection or (clientSelection == 1 and selection == 3):
    conn.send(b"Server won game\n")
    print("I won")
else:
    conn.send(b"You won\n")
    print("Player won game")

