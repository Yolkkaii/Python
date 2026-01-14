import math

def lg_of_int(n): #This function requires an integer
    return math.log2(n)

num = float(input("Enter a number greater than or equal to 1: "))

while num < 1:
    num = float(input("Invalid input, please enter a new number: "))

print(f"Result = {int(lg_of_int(int(num)))}")