import random


# list comprehension template
# list = [NEW_ITEM for ITEM in LIST if TEST]


# iterates over the items in the list and increments them
numbers = [1,2,3]
new_numbers = [n+1 for n in numbers]

print(numbers)
print(new_numbers)

# iterates over the string and adds them to a new list
name = "Kerry"
new_name = [letter for letter in name]

print(name)
print(new_name)

# challenge: try to create a range from 1 to 5
new_range = [num * 2 for num in range(1,5)]
print(new_range)

# adding if and test conditions
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

# dictionary comprehension
# new_dict = {NEW_KEY:NEW_VALUE for (KEY, VALUE) in DICT.ITEMS() if TEST}

# randomizing student's scores and filtering for passing grades
names2 = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1,100) for student in names2}
print(students_scores)

# this allows us to 'filter' or affect the values in the key value pairs. the .items() function allows us access to that
passed_students = {student:score for (student,score) in students_scores.items() if score >= 60}
print(passed_students)