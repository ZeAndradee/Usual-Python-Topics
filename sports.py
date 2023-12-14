# Write a program with the following input:

# A) Registration number (0 ends the reading), age, the sport (swimming,
# basketball, or volleyball) they are enrolled in, and gender.

# At the end of reading, display on the screen:

# A) The average age of participants, the oldest, and the youngest.

# B) The descending order of the number of people enrolled in each
# sport and the name of the sport.

# C) What percentage, in relation to the total, of males are enrolled.

# Note: Validate all inputs and only use topics covered so far.

registration = 999
total_registrations = 0
average_age = 0
oldest = 0
youngest = 999
swimming = 0
basketball = 0
volleyball = 0
males = 0

while True:
    registration = int(input("Enter your registration number: "))
    if registration == 0:
        break
    total_registrations += 1
    age = int(input("Enter your age: "))
    if age > oldest:
        oldest = age
    elif age < youngest:
        youngest = age
    average_age += age
    sport = input('''Enter the chosen sport:
     [S] Swimming
     [B] Basketball
     [V] Volleyball ''')
    
    if sport.lower() == "s":
        swimming += 1
    elif sport.lower() == "b":
        basketball += 1
    elif sport.lower() == "v":
        volleyball += 1
    
    gender = input("Enter your gender: [M] Male or [F] Female")
    if gender.lower() == "m":
        males += 1
    
average_age /= total_registrations
male_percentage = (males / total_registrations) * 100

print(f'''Average Age: {average_age:.1f}
Oldest: {oldest}
Youngest: {youngest}''')

# Sorting sports in descending order
sports_list = [("Swimming", swimming), ("Basketball", basketball), ("Volleyball", volleyball)]
sorted_sports = sorted(sports_list, key=lambda x: x[1], reverse=True)

print(f'''
1- {sorted_sports[0][0]}: {sorted_sports[0][1]}
2- {sorted_sports[1][0]}: {sorted_sports[1][1]}
3- {sorted_sports[2][0]}: {sorted_sports[2][1]}
''')

print(f'''Percentage of Males: {male_percentage:.1f}%''')
