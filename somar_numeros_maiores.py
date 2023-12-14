# Create a program that reads 3 numbers and sums the 2 largest ones.

# Declaring variables
largest_num = 0
second_largest_num = 0
smallest_num = 0

# Receive input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Conditions for number 1
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num1 >= num2 and num1 <= num3:
    second_largest_num = num1
elif num1 >= num3 and num1 <= num2:
    second_largest_num = num1
else:
    smallest_num = num1

# Conditions for number 2
if num2 >= num1 and num2 >= num3:
    largest_num = num2
elif num2 >= num1 and num2 <= num3:
    second_largest_num = num2
elif num2 >= num3 and num2 <= num1:
    second_largest_num = num2
else:
    smallest_num = num2

# Conditions for number 3
if num3 >= num1 and num3 >= num2:
    largest_num = num3
elif num3 >= num1 and num3 <= num2:
    second_largest_num = num3
elif num3 >= num2 and num3 <= num1:
    second_largest_num = num3
else:
    smallest_num = num3 

# Print the result of the sum
sum_result = largest_num + second_largest_num
print(f"The sum of the largest and second-largest numbers is: {sum_result} | The sum of {largest_num} + {second_largest_num} is: {sum_result}")
