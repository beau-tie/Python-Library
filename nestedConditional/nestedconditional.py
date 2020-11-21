#Nested conditional statement problem 1
num = input("Sales total($): ")
if num <= 50000:
    print str(num + (num * 0.02))
else:
    if num <= 100000:
        print str(num + (num * 0.05))
    else:
        if num <= 400000:
            print str(num + (num * 0.07))
        else:
            print str(num + (num * 0.12))
    
