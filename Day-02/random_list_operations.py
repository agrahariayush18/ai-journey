import random

# Create a list of 15 random numbers (between 1 and 20, so duplicates are likely)
random_list = [random.randint(1, 20) for _ in range(15)]
print("Original List:", random_list)

# Sort in ascending order
ascending = sorted(random_list)
print("Ascending Order:", ascending)

# Sort in descending order
descending = sorted(random_list, reverse=True)
print("Descending Order:", descending)

# Remove duplicates (preserving original order) and print the modified list
no_duplicates = list(dict.fromkeys(random_list))
print("After Removing Duplicates:", no_duplicates)
