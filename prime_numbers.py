num = int(input("Enter a positive integer: "))  # Request input for a positive integer
is_prime_number = True  # Assume the number is prime initially

for i in range(2, num):
    if (num % i) == 0:
        is_prime_number = False  # If the number is divisible, it's not prime
        break

if num == 1:
    print("1 is not a prime number.")  # 1 is not considered a prime number

if num > 1:
    if is_prime_number:
        print(f"{num} is a prime number.")  # Display if the input is a prime number
    else:
        print(f"{num} is not a prime number.")  # Display if the input is not a prime number
