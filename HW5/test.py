import turtle

turtle.speed(0) # Set speed to 0 for instant drawing
turtle.hideturtle() # Hide the turtle to clean up the screen

def draw_calendar_grid():
    """Draws a single calendar grid."""
    
    tlx = turtle.xcor()
    tly = turtle.ycor()

    # Draw the outer rectangle
    turtle.pendown()
    for _ in range(2):
        turtle.forward(210)
        turtle.right(90)
        turtle.forward(180)
        turtle.right(90)
    turtle.penup()

    # Draw the horizontal lines for the rows
    for i in range(1, 7):
        turtle.goto(tlx, tly - (i * 30))
        turtle.pendown()
        turtle.forward(210)
        turtle.penup()

    # Draw the vertical lines for the columns
    turtle.right(90)
    for i in range(1, 8):
        turtle.goto(tlx + (i * 30), tly)
        turtle.pendown()
        turtle.forward(180)
        turtle.penup()
    turtle.left(90)

def month_info(m, md, wd, dy, tlx, tly):
    """Writes the month name, day names, and all dates into the grid."""
    
    # Write the month name
    turtle.goto(tlx + 105, tly - 20)
    turtle.write(f"Month #{m}", align="center", font=("Arial", 14, "bold"))

    # Write the day names
    for i in range(1, 8):
        turtle.goto(tlx + 20 + (28 * (i-1)), tly - 46)
        turtle.write(wd[i], align="left", font=("Arial", 9, "normal"))

    # Loop to write all dates
    for date in range(1, md + 1):
        
        # Calculate the day number from the start of the week
        # 'dy' is the day number (e.g., 4 for Thursday)
        # 'date' is the date (1, 2, 3...)
        current_day_number = (dy + date - 2)
        
        # Calculate the row and column
        row = current_day_number // 7
        column = current_day_number % 7
        
        # Adjust vertical position based on the week (row)
        y_pos = tly - 75 - (row * 30)
        
        # Adjust horizontal position based on the day of the week (column)
        x_pos = tlx + 20 + (column * 28)

        # Go to the new position and write the date
        turtle.goto(x_pos, y_pos)
        turtle.write(str(date))


month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

week_days = {
    1: "Su", 2: "Mo", 3: "Tu", 4: "We", 5: "Th", 6: "Fr", 7: "Sa"
}

# Starting position for the top-left calendar
start_x = -450
start_y = 350
# Starting day of the week for January 1st (e.g., 4 for Thursday)
day_num = 4 

for i in range(1, 13):
    
    # Calculate the row and column for the current month's calendar
    row = (i - 1) // 3
    col = (i - 1) % 3
    
    # Calculate the top-left corner for the current calendar
    tlx = start_x + (col * 250)
    tly = start_y - (row * 220)
    
    # Go to the calculated position
    turtle.penup()
    turtle.goto(tlx, tly)

    # Get the month's data
    m_day = month_days[i]
    
    # Draw the calendar and add the month's info
    draw_calendar_grid()
    month_info(i, m_day, week_days, day_num, tlx, tly)
    
    # Update the starting day for the next month
    day_num = (day_num - 1 + m_day) % 7 + 1

turtle.done()