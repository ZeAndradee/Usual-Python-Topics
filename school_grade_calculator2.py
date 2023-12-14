# Exercise 3

failed = False

while not failed:
    final = False
    print("Enter the first grade: ")
    grade1 = int(input())
    remaining1 = 14 - grade1
    remaining1f = 10 - grade1

    if grade1 < 4:
        print("Failed outright.")
        failed = True
        break
    elif 4 <= grade1 < 7:
        print("Need ", remaining1f, " more points to pass the final.")
        final = True
    elif grade1 >= 7:
        print("Need ", remaining1, " more points to pass outright.")

    print("Enter the second grade: ")
    grade2 = int(input())
    remaining2 = 14 - (grade1 + grade2)

    if final and grade2 < remaining1f:
        print("Failed outright.")
        failed = True
    elif final and remaining1f <= grade2 < remaining1:
        print("Need ", remaining1f, " more points to pass the final.")
    elif not final and grade2 >= remaining1f:
        print("Passed outright.")
        break
    
    print("Enter the final grade: ")
    final_grade = int(input())
    final_average = (grade1 + grade2 + final_grade) / 3

    if final_average < 10:
        print("Failed the final.")
        failed = True
    else:
        print("Passed the final. 🙌")
        break
