# Exercise 3
def hanoi_tower(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from {} to {}".format(source, destination))
    else:
        hanoi_tower(n - 1, source, auxiliary, destination)
        print("Move disk {} from {} to {}".format(n, source, destination))
        hanoi_tower(n - 1, auxiliary, destination, source)

# Request the value of n from the user and validate if it's within the allowed range
while True:
    n = int(input("Enter the number of disks (n) (3 to 8): "))
    if 3 <= n <= 8:
        break
    else:
        print("Invalid value. Please enter again.")

# Call the hanoi_tower function to solve the problem
hanoi_tower(n, "Source", "Destination", "Auxiliary")
