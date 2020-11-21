# This script will output the volume of a cylinder by taking user input of the
# area of a circle and height

def circle_area(radius):
    area_of_circle = 3.14 * radius * radius
    return area_of_circle

radius = input("Enter a number for radius: ")
height = input("Enter a number for height: ")

volume_of_cylinder = height * circle_area(radius)

print "Volume of the cylinder is: ", volume_of_cylinder
