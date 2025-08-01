#Task 1: Payroll
'''
name = input("Enter employee's name: ")
hours = float(input("Enter hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

print(f"\nEmployee Name: {name}\nHours Worked: {hours}\nPay Rate: {pay_rate}\nGross Pay: {float(hours) * float(pay_rate)}")
print(f"Deductions:\n  Federal Withholding ({federal_tax * 100}%): {round(float(hours) * float(pay_rate) * float(federal_tax), 2)}\n  State Withholding ({state_tax * 100}%): {round(float(hours) * float(pay_rate) * float(state_tax), 2)}")
print(f"  Total Deduction: {round(float(hours) * float(pay_rate) * (float(federal_tax) + float(state_tax)), 2)}")
print(f"Net Pay: {round(float(hours) * float(pay_rate) - (float(hours) * float(pay_rate) * (float(federal_tax) + float(state_tax))), 2)}")
'''

#Task 2: Reversed numbers
'''
number = input("Enter a four digit number: ")
reversed = int(number[::-1])
print(reversed)
'''

#Task 3: Make a star
import turtle
length = int(input("Enter the length of the star: "))

turtle.pensize(2)
turtle.speed(8)
down = turtle.pendown()
up = turtle.penup()

for i in range(5):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(144)
    turtle.penup()

turtle.hideturtle()
turtle.done()

#Task 4: Olympic Rings

#Task 5: Make a triangle (using points)
