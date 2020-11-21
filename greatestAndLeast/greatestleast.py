# Gets numbers from user and prints avg, <, >

num1 = input("Enter first integer: ")

num2 = input("Enter second integer: ")

num3 = input("Enter third integer: ")

avg = num1 + num2 + num3

numList = [num1, num2, num3]

for i in numList:
    if num2 > num1:
        if num3 > num2:
            greatest = num3
        else:
            greatest = num2
    else:
        greatest = num1

for i in numList:
    if num2 < num1:
        if num3 < num2:
            least = num3
        else:
            least = num2
    else:
        least = num1
        
str(num1)
str(num2)
str(num3)
str(greatest)
str(least)

print("The average of {}, {}, and {} is {}").format(num1, num2, num3, avg)

print("The greatest interger out of {}, {}, and {}, is {}").format(num1, num2, num3, greatest)

print("The smallest integer out of {}, {}, and {}, is {}").format(num1, num2, num3, least)
      
