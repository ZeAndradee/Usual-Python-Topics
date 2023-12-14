# Exercise 4
a = int(input("Enter value A: "))
b = int(input("Enter value B: "))
c = int(input("Enter value C: "))

delta = (b * b) - 4 * a * c
root1 = (-b + (delta ** 0.5)) / (2 * a)
root2 = (-b - (delta ** 0.5)) / (2 * a)

if delta < 0:
    print("The equation has no real roots.")
elif delta == 0:
    print(f"The equation has one real root: {root1}")
elif delta > 0:
    print(f"The roots of this equation are: Root1 = {root1:.4f} and Root2 = {root2:.4f}")
