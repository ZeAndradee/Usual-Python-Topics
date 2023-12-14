# Exercise 5

def power_calculation(number):
    for i in range(2, number + 1):
        print(f"{number}^{i} =", number**i)
        
number_input = int(input("Enter a number: "))
power_calculation(number_input)
