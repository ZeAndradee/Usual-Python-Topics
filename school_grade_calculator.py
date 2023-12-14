# Exercise 1
print("Enter the grade in Portuguese")
portuguese = int(input())
print("Enter the grade in Mathematics")
math = int(input())
print("Enter the grade in Physics")
physics = int(input())
print("Enter the grade in Chemistry")
chemistry = int(input())
print("Enter the grade in History")
history = int(input())
print("Enter the grade in Geography")
geography = int(input())
print("Enter the grade in Biology")
biology = int(input())
print("Enter the grade in Philosophy")
philosophy = int(input())
print("Enter the grade in Foreign Language")
foreign_language = int(input())
print("Enter the grade in Sociology")
sociology = int(input())

average = (portuguese * 2 + math * 2 + physics * 2 + chemistry * 1 + history * 0.5 + geography * 0.5 + biology * 0.5 + philosophy * 0.5 + foreign_language * 0.5 + sociology * 0.5) / 10
average *= 10

if portuguese == 0 or math == 0 or physics == 0 or chemistry == 0 or history == 0 or geography == 0 or biology == 0 or philosophy == 0 or foreign_language == 0 or sociology == 0:
    print("You have failed.")    
elif average >= 65:
    print("You have passed.")
else:
    print("You are in the relocation process.")
