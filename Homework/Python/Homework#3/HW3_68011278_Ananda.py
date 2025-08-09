# #Task 1: Payroll

name = input("Enter employee's name: ")
hours = float(input("Enter hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

gross_pay = hours * pay_rate
federal_deduction = gross_pay * federal_tax
state_deduction = gross_pay * state_tax
total_deduction = federal_deduction + state_deduction
net_pay = gross_pay - total_deduction

print(f"\nEmployee Name: {name}\nHours Worked: {hours}\nPay Rate: {pay_rate}\nGross Pay: {gross_pay:.2f}")
print("Deductions:")
print(f"  Federal Withholding ({federal_tax * 100:.2f}%): {federal_deduction:.2f}")
print(f"  State Withholding ({state_tax * 100:.2f}%): {state_deduction:.2f}")
print(f"  Total Deduction: {total_deduction:.2f}")
print(f"Net Pay: {net_pay:.2f}")

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

turtle.pensize(5)
turtle.speed(20)
turtle.hideturtle()
turtle.penup()

# Top row of rings
turtle.goto(-2.5 * radius, 0)
turtle.pendown()
turtle.color("blue")
turtle.circle(radius)
turtle.penup()

turtle.goto(0, 0)
turtle.pendown()
turtle.color("black")
turtle.circle(radius)
turtle.penup()

turtle.goto(2.5 * radius, 0)
turtle.pendown()
turtle.color("red")
turtle.circle(radius)
turtle.penup()

# Bottom row of rings
turtle.goto(-1.25 * radius, -radius)
turtle.pendown()
turtle.color("yellow")
turtle.circle(radius)
turtle.penup()

turtle.goto(1.25 * radius, -radius)
turtle.pendown()
turtle.color("green")
turtle.circle(radius)
turtle.penup()

turtle.done()


#Task 5: Make a triangle (using points)

import turtle

p1x,p1y = input("Enter first point for triangle (x,y): ").split(",")
p2x,p2y = input("Enter second point for triangle (x,y): ").split(",")
p3x,p3y = input("Enter third point for triangle (x,y): ").split(",")

#Convert x, y points to floating point
p1x = float(p1x)
p2x = float(p2x)
p3x = float(p3x)

p1y = float(p1y)
p2y = float(p2y)
p3y = float(p3y)

area = 1/2 * abs(p1x * (p2y - p3y) + p2x * (p3y - p1y) + p3x * (p1y - p2y))

turtle.penup()
turtle.goto(p1x, p1y)
turtle.pendown()
turtle.goto(p2x, p2y)
turtle.goto(p3x, p3y)
turtle.goto(p1x, p1y)
turtle.penup()

turtle.goto((p1x + p2x + p3x)/3, -(p1x + p2y + p3y)/3)
turtle.write(f"Area: {area:.2f}")

turtle.hideturtle()
turtle.done()
