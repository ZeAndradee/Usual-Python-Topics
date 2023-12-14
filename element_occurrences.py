# Creating a tuple
tuple1 = (1, 1, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 8, 8, 8, 8, 8)
# Creating an empty list
list2 = []

# Initializing variables
aux = 0
counter = 0

# Looping through the tuple
for i in tuple1:
    # Checking if the current element is equal to the previous one
    if i == aux:
        counter += 1
    else:
        # Creating a string representation of the previous element and its count
        representation = f"{aux} - {counter}"
        aux = i
        counter = 1
        # Appending the representation to the list
        list2.append(representation)

# Creating a string representation for the last element and its count
representation = f"{aux} - {counter}"
# Appending the representation to the list
list2.append(representation)

# Printing the result as a tuple (excluding the first element, which is empty)
print(tuple(list2)[1:])
