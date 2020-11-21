#Easy consistent phone numbers

num = input("Enter a 10 digit phone number: ")
if len(num) == 10:
    print "("+num[0:3]+")"+num[3:6]+"-"+num[6: ]
else:
    print "Error"
