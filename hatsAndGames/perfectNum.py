# This program will determine if a number inputed is a perfect number or not

def is_plus_perfect(n):
    digitsN = len(str(n))
    number = str(n)
    digitPowerSum = 0

    for i in number:
        x = int(i)
        digitPowerSum += x**digitsN
    return digitPowerSum

n = input("Enter a number: ")

print is_plus_perfect(n)

if is_plus_perfect(n) == n:
    print "Number ", n , " is a perfect number."
else:
    print "Number ", n , " is not a perfect number."


