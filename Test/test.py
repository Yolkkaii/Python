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
