# Exercise 1 B
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


value_n = int(input("Enter a positive integer value for n: "))

print(f"Fibonacci({value_n}) =")
for i in range(value_n):
    print(fibonacci_recursive(i))
