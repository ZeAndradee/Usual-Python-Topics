# Exercise 3
num_patinhos = int(input("Enter the number of ducklings: "))
original_count = num_patinhos

while num_patinhos > 0:
    count_down = (num_patinhos - 1)
    print(f'''{num_patinhos} little ducks went out to play,
      beyond the mountains
      to have some fun
      momma duck quacked: Quack, quack, quack, quack
      But only {count_down} little ducks came back from there.''')
    num_patinhos = count_down

if num_patinhos == 0:
    print(f'''Momma duck went searching
    Beyond the mountains
    by the seaside.
    Momma duck quacked: Quack, quack, quack, quack
    and the {original_count} little ducks came back from there.''')
