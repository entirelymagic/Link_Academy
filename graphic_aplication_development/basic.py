import tkinter as tk

window = tk.Tk()  # create tkinter app
window.title("Basic Tkinter App")  # app title

window_height = 500
window_width = 900

window.resizable(False, False)  # This code helps to disable windows from resizing

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))
login_user_label = tk.Label(window, text="User Login").grid(row=0, column=2)
# the label for user_name
user_name = tk.Label(window, text="Username").grid(row=1, column=1)
# the label for user_password
user_password = tk.Label(window, text="Password").grid(row=3, column=1)
# Entry areas for username and password
user_name_input_area = tk.Entry(window, width=30).grid(columnspan=4, row=2)
user_password_entry_area = tk.Entry(window, width=30).grid(row=4, columnspan=4)
# Buttons for submit and close
submit_button = tk.Button(window, text="Submit").grid(row=5, column=1)
close_button = tk.Button(window, text="Close").grid(row=5, column=3)
window.mainloop()
