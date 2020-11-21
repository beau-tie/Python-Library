# This will determine the total cost of hats ordered

def order_total(num):
    if num % 6 == 0:
        total = round((8.3334 * num) + (num * 2.00))
        return total
    else: 
        total = round((num * 10.00) + (num * 2.00))
        return total

# This determines the price of a hat or hats in the "onset of warm weather"

def order_total_overnight(num):
    if num <= 5:
        total = (num * 10) + 32
        return total
    else:
        if num > 5 and num <= 20:
            total = (num * 10) + 45
            return total
        else:
            total = (num * 10) + (num * 3)
            return total

# Script actually starts here, with the input taken from a user

num = input("How many hats would you like to order?: ")


