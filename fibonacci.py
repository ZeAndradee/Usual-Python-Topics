# Exercise 1 A
parameter = int(input("Enter a parameter: "))

def fibonacci(parameter):
    print(f"Fibonacci ({parameter}) = ")    
    previous_num = 0
    current_num = 1
    print(previous_num)  
    print(current_num)

    for i in range(2, parameter):
        next_num = previous_num + current_num   
        print(next_num)                       
        previous_num = current_num             
        current_num = next_num                 

fibonacci(parameter)
