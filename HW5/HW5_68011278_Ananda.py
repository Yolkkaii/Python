# Task 1: Newton's Method
n = int(input("Input a number: "))
guess = n/2


for i in range(0,5):
    temp = float(n/guess)
    guess = (guess + temp)/2
    print(round(guess, 3))

#Task 2: Calendar
import turtle
import math

turtle.speed(50)

def draw_calendar(num_rows):
    tlx = turtle.xcor()
    tly = turtle.ycor()
    turtle.pendown()

    calendar_height = 25 * (num_rows + 1) + 25
    
    for _ in range(2):
        turtle.forward(200)
        turtle.right(90)
        turtle.forward(calendar_height)
        turtle.right(90)
    turtle.penup()

    for i in range(1, num_rows + 3):
        turtle.goto(tlx, tly - (i * 25))
        turtle.pendown()
        turtle.forward(200)
        turtle.penup()

    turtle.right(90)
    for i in range(1,7):
        turtle.goto(tlx + (28 * i), tly - 25)
        turtle.pendown()
        turtle.forward(calendar_height - 25)
        turtle.penup()
    turtle.left(90)


def month_info(m, md, wd, dt, dy, tlx, tly):
    num_rows = math.ceil((md + (dy - 1)) / 7)
    
    turtle.goto(tlx + 10, tly - 22)
    turtle.write(f"Month #{m}")

    for i in range(1, 8):
        turtle.goto(tlx + 8 + (28 * (i - 1)), tly - 46)
        turtle.write(wd[i])

    for date in range(1, md + 1):
        current_day_number = (dy + date - 2)
        
        row = current_day_number // 7
        column = current_day_number % 7
        
        y_pos = tly - 75 - (row * 25)
        
        x_pos = tlx + 8 + (column * 28)

        turtle.goto(x_pos, y_pos)
        turtle.write(str(date))

month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

week_days = {
    1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"
}

month = 1
m_day = month_days[month]
date = 1
day_num = 4
day = week_days[day_num]

for i in range(1,13):
    row = (i - 1) // 3
    col = (i - 1) % 3

    tlx = -400 + (col * 250)
    tly = 450 - (row * 220)

    turtle.penup()
    turtle.goto(tlx, tly)

    m_day = month_days[i]

    num_rows = math.ceil((m_day + (day_num - 1)) / 7)
    
    draw_calendar(num_rows)
    month_info(i, m_day, week_days, date, day_num, tlx, tly)

    day_num = (day_num - 1 + m_day) % 7 + 1

turtle.hideturtle()
turtle.done()

# #Task 3
num = 0
valid = False
while valid != True:
    num = int(input("Enter a number greater than zero: "))
    if num <= 0:
        print("Invalid number.")
    else:
        valid = True

for a in range(num, 0, -1):
    if a == num or a == 1:
        for i in range(1, a + 1):
            for j in range(i):
                print("*", end="")
            print()
    else:
        for i in range(2, a + 1):
            for j in range(i):
                print("*", end="")
            print()

    for i in range(a - 1, 0, -1):
        for j in range(i):
            print("*", end="")
        print()
