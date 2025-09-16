# #Task 1
# num = int(input("Enter an integer: "))
# binary = ""

# if num == 0:
#     print("It is 0.")
# elif num < 0:
#     print("It is negative.")
# else:
#     #integer to binary
#     quotient = num

#     while quotient > 0:
#         remainder = quotient % 2
#         binary = str(remainder) + binary
#         quotient //= 2

#     print(f"Integer to binary: {binary}")

#     #binary to integer
#     count = 0
#     integer = 0

#     for i in reversed(binary):
#         integer += int(i) * (2 ** count)
#         count += 1

#     print(f"Binary to integer: {integer}")

# #Task 2
# string = str(input("Enter a string: "))

# count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
#     'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
#     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
#     'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

# for i in string:
#     if i in count:
#         count[i] += 1

# for i in count:
#     if count[i] == 0:
#         continue
#     else:
#         percent = (count[i] / len(string)) * 100
#         print(f"{i}: {percent:.2f}%")

# #Task 3
# import turtle
# string = str(input("Enter a string: "))

# count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
#     'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
#     'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
#     'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

# for i in string:
#     if i in count:
#         count[i] += 1

# chars_used = 0
# highest = 0
# for i in count:
#     if count[i] == 0:
#         continue
#     else:
#         chars_used += 1
#         if highest < count[i]:
#             highest = count[i]

# #draw graph
# corner_x, corner_y = turtle.xcor(), turtle.ycor()
# turtle.pd()
# turtle.forward(chars_used * 40)
# turtle.pu()
# turtle.goto(corner_x, corner_y)
# turtle.left(90)
# turtle.pd()
# turtle.forward(highest * 20)
# turtle.pu()
# turtle.goto(corner_x, corner_y)
# turtle.right(90)

# #draw graph bars
# prev = 30
# for i in count:
#     if count[i] == 0:
#         continue
#     else:
#         turtle.goto(prev, corner_y - 20)
#         turtle.write(i)
#         turtle.goto(prev, corner_y)
#         turtle.left(90)
#         turtle.pd()
#         turtle.forward(count[i] * 20)
#         turtle.right(90)
#         turtle.forward(10)
#         turtle.right(90)
#         turtle.forward(count[i] * 20)
#         turtle.left(90)
#         turtle.pu()
#         prev += 30

# turtle.hideturtle()
# turtle.done()

#Task 4
ISBN_9 = str(input("Enter the first 9 digits of an ISBN-10 number: "))

ISBN_10th = 0
count = 1
for i in ISBN_9:
    ISBN_10th += int(i) * count
    count += 1
   
ISBN_10 = ISBN_9 
if ISBN_10th % 11 == 10:
    ISBN_10 += "X"
else:
    ISBN_10 += str(ISBN_10th % 11)

print(f"Your ISBN-10 number is {ISBN_10}")
