#Task 1
'''
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))
num4 = int(input("Enter the 4th number: "))
num5 = int(input("Enter the 5th number: "))

sum = num1 + num2 + num3 + num4 + num5
average = sum / 5

print(f"The sum = {sum}\nThe average = {average}")
'''

#Task 2
import turtle

x = 0
y = 0

turtle.pensize(3)
turtle.speed(8)
def fill(outline, fill):
    turtle.color(outline, fill)
    turtle.begin_fill()

end_fill = turtle.end_fill

turtle.bgcolor('lightblue')

#Draw main house body
turtle.penup()
turtle.goto(x - 250, y)
fill('black', 'gray')
turtle.pendown()
turtle.begin_fill()
def draw_square(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
draw_square(500, 300)
end_fill()
turtle.penup()

#Draw the window
turtle.goto(x - 175, y - 200)
turtle.left(90)
fill('black', 'cyan')
turtle.pendown()
draw_square(100, 80)
end_fill()
turtle.penup()

turtle.goto(x - 135, y - 200)
turtle.pendown()
turtle.forward(100)
turtle.penup()

turtle.goto(x - 175, y - 150)
turtle.right(90)
turtle.pendown()
turtle.forward(80)
turtle.penup()

#Draw the roof
turtle.left(90)
turtle.goto(x - 300, y)
turtle.right(60)
fill('black', 'brown')
turtle.pendown()
turtle.begin_fill()
turtle.forward(350)
turtle.right(60)
turtle.forward(350)
turtle.right(150)
turtle.forward(605)
end_fill()

#Draw chimnet
turtle.penup()
turtle.right(150)
turtle.forward(100)
turtle.left(60)
fill('black', 'brown')
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(32)
end_fill()

#Draw house door
turtle.penup()
turtle.goto(x + 75, y - 300)
fill('black', 'brown')
turtle.pendown()
turtle.right(180)
turtle.forward(180)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(100)
end_fill()
turtle.penup()

#Draw door handle
turtle.goto(x + 80, y - 225)
turtle.left(90)
turtle.pendown()
fill('black', 'yellow')
turtle.circle(10)
end_fill()
turtle.penup()

#Draw stone path
turtle.goto(x + 75, y - 350)
turtle.pendown()
turtle.pensize(2)
fill('black', 'gray')
turtle.circle(20)
end_fill()
turtle.penup()

turtle.goto(x + 125, y - 400)
turtle.begin_fill()
turtle.pendown()
turtle.circle(20)
end_fill()
turtle.penup()

#Draw bushes
for i in range(3):
    turtle.pensize(2)
    turtle.goto(x - 180, y - 300)
    turtle.pendown()
    fill('black', 'green')
    turtle.circle(50)
    end_fill()
    turtle.penup()
    x -= 50

turtle.hideturtle()
turtle.done()
