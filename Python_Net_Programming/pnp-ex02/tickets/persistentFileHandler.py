import os
import datetime
import json
import threading

DATABASE_FILE = "database.json"
locker = threading.Lock()


def deserialize():
    tickets = {}
    if os.path.exists(DATABASE_FILE) and os.stat(DATABASE_FILE).st_size > 0:
        fin = open(DATABASE_FILE)
        tickets = json.load(fin)
        fin.close()
    return tickets


def serialize(tickets):
    fout = open(DATABASE_FILE, "w")
    json.dump(tickets, fout)
    fout.close()


def insert_ticket():
    locker.acquire()
    tickets = deserialize()
    newTicketId = len(tickets.items()) + 1
    tickets[newTicketId] = {
        "date": str(datetime.datetime.now()),
        "used": False
    }
    serialize(tickets)
    locker.release()
    return newTicketId


def checkout(id):
    tickets = deserialize()
    ticketValid = False
    if id in tickets.keys():
        if not tickets[id]["used"]:
            tickets[id]["used"] = True
            ticketValid = True
    serialize(tickets)
    return ticketValid
