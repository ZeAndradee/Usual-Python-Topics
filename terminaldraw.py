# Exercise 5
height = int(input("Enter an odd number for the height of the diamond: "))
width = height

for i in range(height):
    for j in range(width):
        if i + j == height // 2 or i - j == height // 2 or j - i == height // 2 or i + j == 3 * (height // 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
