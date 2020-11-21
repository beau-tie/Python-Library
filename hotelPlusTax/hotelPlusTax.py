x = input("How many nights: ")

if x <= 3:
    num = x * 1.05
    q = num * 50
else:
    num = x * 1.05
    q = num * 65

print "Number of nights:", x
print "Tax: ", num
print "Total: ", q
