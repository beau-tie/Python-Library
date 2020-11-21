# This script will allow users to utilize two different functions
# based on whether they need overnight shipping or not

from hats import *

overnight = input("Use overnight shipping? (y/n): ")

if overnight.strip().lower().startswith("y") == "y":
    total = order_total_overnight(num)
else:
    total = order_total(num)

print "Your shipping total is ", total, " dollars"
