# Exercise 2
num = int(input("Enter a number: "))
largest_num = 0
smallest_num = 999999

while num >= 0:
    num = int(input("Enter a number: "))
    if num > largest_num:
        largest_num = num
    elif num < smallest_num and num > 0:
        smallest_num = num
    else:
        continue

print(f'''The largest number entered was: {largest_num}
The smallest number entered was: {smallest_num}''')
