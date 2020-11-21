from sample_functions import simple_postage, sing_verse

num = input("Enter a number between 1 and 99: ")

if num >= 1 and num <= 99:
    sing_verse(num)

weight = input("Enter weight of letter: ")
print simple_postage(weight)
    



