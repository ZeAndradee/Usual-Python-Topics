# Exercise 1
num = int(input("Enter a number: "))

if num > 1:
    if num == 2:
        print("2 is a prime number.")
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
        else:
            print(f"{num} is a prime number.")
            break
else:
    print(f"{num} is not a prime number.")
