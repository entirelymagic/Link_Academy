x = 5
y = 6
width = 5
height = 4
# Your code here

user_x = int(input("Enter x: "))
user_y = int(input("Enter y: "))

box_x_end = x + int(width)
box_y_end = y + int(height)

in_box = x <= user_x <= box_x_end and y <= user_y <= box_y_end

print(in_box)
