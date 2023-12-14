# Exercise 6
# Defining variables
highest_avg = 0
first_registration = 0
oldest_age = 0
female_count = 0
renewing_count = 0
total_registered = 0
registration = 0
finish_registration = False

# Start registration loop
while not finish_registration:
    print(" - Starting registration -")
    registration = int(input("Enter your registration number: "))
    
    if registration == 0:
        print("Registration has been completed.")
        finish_registration = True
        break

    # Input Age
    age = int(input("Enter your age: "))

    # Input Average
    university_avg = int(input("Enter your overall university average: "))
    
    if university_avg > highest_avg:
        highest_avg = university_avg
        first_registration = registration

    if university_avg == highest_avg and age > oldest_age:
        oldest_age = age
        highest_avg = university_avg
        first_registration = registration

    # Input Gender
    gender = input("Enter your gender: Female [F] or Male [M].")
    
    if gender.lower() == "f":
        female_count += 1
        total_registered += 1
    elif gender.lower() == "m":
        total_registered += 1
    else:
        print("Invalid gender chosen.")
        continue

    # Input Renewing Contract
    renewing_contract = input("Are you renewing the contract? [Y/N] ")
    
    if renewing_contract.lower() == "y" or renewing_contract.lower() == "yes":
        renewing_count += 1

# Print results
print(''' 
- Results -
''')
female_percentage = (female_count / total_registered) * 100
print(f'''The total number of registered candidates is: {total_registered}.
First place: Registration ({first_registration}) | Average ({highest_avg})
Percentage of registered women: {female_percentage:.1f}%
Total candidates renewing: {renewing_count}''')
