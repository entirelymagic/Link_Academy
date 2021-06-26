import tkinter as tk

import time

from tkinter import messagebox
from handlers import random_float
window = tk.Tk()

window.title("Feed me Game")

window.geometry(f"600x200+700+300")

feed_me_lbl = tk.Label(window, text="I am hungry! Press left mouse button 2 times as fast as you can to feed me!")
feed_me_lbl.pack()

btn_feed = tk.Button(window, text="Feed me!")
btn_feed.pack(fill="both")
running = True
start = 0
score = 0
max_score = 0


def event_handler1(event):
    global start
    global running
    global btn_feed
    global score
    global max_score
    if running:
        btn_feed.config(text="The button has been pressed!")
        start = time.time()
        running = False

    else:

        win_time = random_float()

        btn_feed.config(text="Feed me")
        end = time.time()
        total = end - start
        print(total)
        if total < win_time:
            score += 1
            if max_score < score:
                max_score = score
            messagebox.showinfo(title="Congratulation",
                                message=f"You won, you ware faster than {str(win_time)}\n"
                                        f"You have quesed {score} times in a row!\n"
                                        f"Max score {max_score}"
                                )
        else:
            messagebox.showinfo(title="Sorry",
                                message=f"You Lost, you ware slower than {win_time}\n"
                                        f"Max score {max_score}"
                                )
            score = 0
        running = True


btn_feed.bind("<Button-1>", event_handler1)


window.mainloop()
