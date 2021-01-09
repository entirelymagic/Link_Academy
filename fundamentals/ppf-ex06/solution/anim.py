import time
import keyboard

target = 50
x = 0
c = keyboard.on_release('q')

while c:
    for i in range(target):
        for j in range(target):
            print("#" if j == x else " ", end="")
        x += 1
        print("\r", end="")
        time.sleep(0.1)
