#Username creation tool

def findUserName(name):
    name1 = name.strip().lower().split()
    first = name1[1]
    last = name1[0]
    index = last.find(",")
    username = first[ :1] + last[ :index]
    return username

name = input("Enter your last, first name: ")

print findUserName(name)
