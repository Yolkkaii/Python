#Task 1: Payroll

name = input("Enter employee's name: ")
hours = float(input("Enter hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

print(f"\nEmployee Name: {name}\nHours Worked: {hours}\nPay Rate: {pay_rate}\nGross Pay: {float(hours) * float(pay_rate)}")
print(f"Deductions:\n  Federal Withholding ({federal_tax * 100}%): {round(float(hours) * float(pay_rate) * float(federal_tax), 2)}\n  State Withholding ({state_tax * 100}%): {round(float(hours) * float(pay_rate) * float(state_tax), 2)}")
print(f"  Total Deduction: {round(float(hours) * float(pay_rate) * (float(federal_tax) + float(state_tax)), 2)}")
print(f"Net Pay: {round(float(hours) * float(pay_rate) - (float(hours) * float(pay_rate) * (float(federal_tax) + float(state_tax))), 2)}")


#Task 2: Reversed numbers

number = input("Enter a four digit number: ")
reversed = int(number[::-1])
print(reversed)


#Task 3: Make a star

import turtle

length = int(input("Enter the length of the star: "))

turtle.pensize(2)
turtle.speed(8)

for i in range(5):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(144)
    turtle.penup()

turtle.hideturtle()
turtle.done()


#Task 4: Olympic Rings

import turtle

radius = int(input("Enter the radius: "))

def create_ring(rad):
    turtle.pendown()
    turtle.circle(radius)
    turtle.penup()

turtle.penup()
turtle.pensize(2)
turtle.speed(15)

turtle.goto(-150, 0)
create_ring(radius)

turtle.forward(radius/5)
turtle.right(108)
create_ring(radius)

turtle.left(108)
turtle.forward(radius*2 - (radius * 0.1))
turtle.right(12)
create_ring(radius)


turtle.forward(radius * 0.4)
turtle.right(88)
create_ring(radius)
turtle.left(102)

turtle.forward(radius*2 - (radius * 0.08))
turtle.right(12)
create_ring(radius)

turtle.hideturtle()
turtle.done()


#Task 5: Make a triangle (using points)

import turtle

p1x,p1y = input("Enter first point for triangle (x,y): ").split(",")
p2x,p2y = input("Enter second point for triangle (x,y): ").split(",")
p3x,p3y = input("Enter third point for triangle (x,y): ").split(",")

turtle.penup()
turtle.goto(int(p1x), int(p1y))
turtle.pendown()
turtle.goto(int(p2x), int(p2y))
turtle.goto(int(p3x), int(p3y))
turtle.goto(int(p1x), int(p1y))
turtle.penup()
turtle.hideturtle()
turtle.done()
