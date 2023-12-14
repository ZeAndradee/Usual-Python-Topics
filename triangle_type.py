# Exercise 2
print("Enter the measurement segment A: ")
a = int(input())
print("Enter the measurement segment B: ")
b = int(input())
print("Enter the measurement segment C: ")
c = int(input())

exists = False
if a + b > c and a + c > b and b + c > a:
    exists = True
else:
    print("This triangle cannot exist.")

if exists and a != b and a != c and c != b:
    print("This triangle is Scalene.")
    
elif exists and (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print("This triangle is Isosceles.")
    
elif exists and a == b == c:
    print("This triangle is Equilateral.")
