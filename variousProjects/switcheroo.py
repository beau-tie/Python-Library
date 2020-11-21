
def switcheroo(word):
    switch = word[-1] + word[1:-1] + word[0]
    return switch

r = input("Enter a word: ")

print switcheroo(r)
