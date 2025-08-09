#Task 1

import turtle

p0x, p0y = input("Enter the first point (x,y): ").split(",")
p1x, p1y = input("Enter the second point (x,y): ").split(",")
p2x, p2y = input("Enter the third point (x,y): ").split(",")

p0x, p0y, p1x, p1y, p2x, p2y = int(p0x), int(p0y), int(p1x), int(p1y), int(p2x), int(p2y)

turtle.penup()
turtle.pensize(2)
turtle.speed(8)
turtle.goto(p0x, p0y)
turtle.dot(5)
turtle.write("P0")
turtle.pendown()
turtle.goto(p1x, p1y)
turtle.dot(5)
turtle.write("P1")
turtle.penup()

turtle.goto(p2x, p2y)
turtle.dot(5)
turtle.write("P2")
turtle.pendown()
turtle.penup()

turtle.goto(p2x, p2y - 20)
#cross product
#left hand side will have positive number, right hand is negative
side_value = (p1x - p0x) * (p2y - p0y) - (p1y - p0y) * (p2x - p0x)

if side_value > 0:
    turtle.write("Point 2 is on the left side of the line")
elif side_value < 0:
    turtle.write("Point 2 is on the right side of the line")
else:
    turtle.write("Point 2 is on the line")

turtle.hideturtle()
turtle.done()

#Task 2

import turtle

x1, y1 = input("Enter the first rectangle's point (x,y): ").split(",")
width1, height1 = input("Enter the first rectangle's point (x,y): ").split(",")
x2, y2 = input("Enter the second rectangle's point (x,y): ").split(",")
width2, height2 = input("Enter the second rectangle's point (x,y): ").split(",")

x1, y1 = int(x1), int(y1)
width1, height1 = int(width1), int(height1)
x2, y2 = int(x2), int(y2)
width2, height2 = int(width2), int(height2)

def draw_rectangle(x, y, width, height):
    turtle.penup()
    turtle.goto(x - width / 2, y - height / 2)
    turtle.pendown()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.penup()    

def is_inside(x1, y1, width1, height1, x2, y2, width2, height2):
    left1, right1 = x1 - width1 / 2, x1 + width1 / 2
    bottom1, top1 = y1 - height1 / 2, y1 + height1 / 2

    left2, right2 = x2 - width2 / 2, x2 + width2 / 2
    bottom2, top2 = y2 - height2 / 2, y2 + height2 / 2
    
    is_left_inside = left1 >= left2
    is_right_inside = right1 <= right2
    is_bottom_inside = bottom1 >= bottom2
    is_top_inside = top1 <= top2
    
    return is_left_inside and is_right_inside and is_bottom_inside and is_top_inside


draw_rectangle(x1, y1, width1, height1)
turtle.goto(x1,y1)
turtle.write("(x1, y1)")
draw_rectangle(x2, y2, width2, height2)
turtle.goto(x2,y2)
turtle.write("(x2, y2)")

dx = abs(x1 - x2)
dy = abs(y1 - y2)

wsum = (width1 / 2) + (width2 / 2)
h_sum = (height1 / 2) + (height2 / 2)

overlaps = dx < wsum and dy < h_sum

r1_in_r2 = is_inside(x1, y1, width1, height1, x2, y2, width2, height2)
r2_in_r1 = is_inside(x2, y2, width2, height2, x1, y1, width1, height1)

turtle.penup()
turtle.goto(0, -250)
if r1_in_r2:
    turtle.write("Rectangle 1 is inside Rectangle 2.")
elif r2_in_r1:
    turtle.write("Rectangle 2 is inside Rectangle 1.")
elif overlaps:
    turtle.write("The rectangles overlaps.")
else:
    turtle.write("The rectangles doesn't overlap.")

turtle.done()
turtle.hideturtle()
