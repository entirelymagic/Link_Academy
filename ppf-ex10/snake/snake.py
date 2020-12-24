import time
import os
import keyboard
from symbols import *

H = 10
W = 20
SLEEP = 0.5
MC = "#"

x = H // 2
y = 1
snake_len = 3
direction = "RIGHT"
c = RIGHTC

clearScreen = lambda: os.system('cls')


def getDirectionAndChar(direction, c):
    # Read user key
    if keyboard.is_pressed('up'):
        direction = "UP"
        c = UPC
    elif keyboard.is_pressed('left'):
        direction = "LEFT"
        c = LEFTC

    elif keyboard.is_pressed('down'):
        direction = "DOWN"
        c = DOWNC

    elif keyboard.is_pressed('right'):
        direction = "RIGHT"
        c = RIGHTC

    return direction, c


def move(direction, x, y):
    # Move snake according to direction
    if direction == "UP":
        x -= 1
    elif direction == "LEFT":
        y -= 1
    elif direction == "DOWN":
        x += 1
    elif direction == "RIGHT":
        y += 1

    return x, y


def renderScreen(x, y, c):
    clearScreen()
    for i in range(H):
        for j in range(W):
            if i == 0 or i == H - 1 or j == 0 or j == W - 1:
                print(MC, end="")
            elif i == x and j == y:
                print(c, end="")
            else:
                print(" ", end="")

        print("")


def printGameOver():
    clearScreen()
    print("#################################")
    print("#           GAME OVER           #")
    print("#################################")


while True:

    direction, c = getDirectionAndChar(direction, c)
    x, y = move(direction, x, y)
    if x <= 0 or x >= H or y <= 0 or y >= W:
        printGameOver()
        break
    else:
        renderScreen(x, y, c)

    time.sleep(SLEEP)

    # print(direction)
    # print(c)
    # print(x, y)
