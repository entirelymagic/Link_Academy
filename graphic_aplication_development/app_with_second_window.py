import tkinter

window = tkinter.Tk()
window.geometry("500x500")

frame1 = tkinter.Frame(window, height=500, width=500, bg="red")
frame1.grid(column=0, row=0, sticky="news")

frame2 = tkinter.Frame(window)
frame2.grid(column=0, row=0, sticky="news")
frame2.configure(bg="blue")

frame3 = tkinter.Frame(window)
frame3.grid(column=0, row=0, sticky="news")
frame3.config(bg="green")

frame_count = 0

def new_frame(event):
    global frame_count
    frame_count = frame_count + 1
    if frame_count == 3:
        frame_count = 0
    [frame1, frame2, frame3][frame_count].tkraise()

frame1.bind("<Button-1>", new_frame)
frame2.bind("<Button-1>", new_frame)
frame3.bind("<Button-1>", new_frame)


# btn1 = tkinter.Button(frame1, text="Go to Frame 2", bg="red", command=lambda :change_frame(frame2))
# btn1.grid(column=0, row=0, sticky="nesw")


# btn2 = tkinter.Button(frame2, text="Go to Frame 3",  bg="blue", command=lambda :change_frame(frame3))
# btn2.grid(column=0, row=0, sticky="nesw")


# btn3 = tkinter.Button(frame3, text="Go to Frame 1", bg="green", command=lambda :change_frame(frame1))
# btn3.grid(column=0, row=0, sticky="nesw")


def change_frame(frame):
    frame.tkraise()



window.mainloop()
