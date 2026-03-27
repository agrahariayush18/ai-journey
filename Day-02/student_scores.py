# Create a list of dictionaries (each representing a student)
students = [
    {'name': 'Ayush', 'score': 85},
    {'name': 'Priya', 'score': 92},
    {'name': 'Rahul', 'score': 78},
    {'name': 'Sneha', 'score': 95},
    {'name': 'Amit', 'score': 88}
]

print("Original List:")
for student in students:
    print(student)

# Sort by 'score' in descending order
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)

print("\nSorted by Score (Descending):")
for student in sorted_students:
    print(student)
