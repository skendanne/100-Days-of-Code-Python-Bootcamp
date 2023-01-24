# Dictionaries

# key - Value
# bug - An error in program that prevents the program from running as expected.
# function - A piece of code that you can easily call over and over again.
# loop - The action of doing something over and over again.

# dictionary = {Key: Value}
# dictionary = {Key1: Value1, Key2: Value2, Key3: Value3}

programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for i in programming_dictionary:
    print(i)

# Exercise:

# Grading Program
# You have acess to a database of student_scores in the format of a dicitionary.
# The keys in student_scores are the names of the students and the values
# are their exam scores

# Write a program that converts their scores to grades. By the end of your
# program, you should have a new dictionary called student_grades that
# should contain student names for keys and their grades for values.
# The final version of the student_grades dictionary will be checked.

# DO NOT modify the existing student_scores dicitionary.
# DO NOT write any print statements

# Scores 91 - 100 = "Outstanding"
# Scores 81 - 90 = "Exceeds Expectations"
# Scores 71 - 80 = "Acceptable"
# Scores 70 or lower = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

grade_1 = "Outstanding"
grade_2 = "Exceeds Expectations"
grade_3 = "Acceptable"
grade_4 = "Fail"

student_grades = {}

for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = grade_1
    elif student_scores[i] > 80:
        student_grades[i] = grade_2
    elif student_scores[i] > 70:
        student_grades[i] = grade_3
    else:
        student_grades[i] = grade_4

print(student_grades)