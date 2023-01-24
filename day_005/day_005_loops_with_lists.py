# For Loop

# for item in list_of_items:
#     do something to each item

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Exercise:

def average_height():
    # You are going to write a program that calculates the average student
    # height from a List of heights.

    # student_heights = [180, 124, 165, 173, 189, 169, 146]
    # 180 120 165 173 189 169 146

    # The average height can be calculated by adding all the heights together 
    # and diving by the total number of heights.

    # Round number to the nearest whole number

    # total_height = sum(student_heights)
    # number_of_students = len(student_heights)
    # average_height = round(total_height / number_of_students)
    # print(average_height)

    student_heights = input("Input a list of student heights ").split()

    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

    print(student_heights)

    total_height = 0
    number_of_students = 0

    for n in student_heights:
        total_height += n

    for n in student_heights:
        number_of_students += 1

    average_height = round(total_height / number_of_students)
    print(average_height)

average_height()

def heights_score():
    # You are going to write a program that calculates the highest score
    # from a list of scores.

    # student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

    # Important you are not allowed to use the max or min functions. The 
    # output words must match the example.

    # The highest score in the class is: x
    # example input 78 65 89 86 55 91 64 89
    # print(max(student_scores))

    student_scores = input("Input a list of student score").split()

    for n in range(0, len(student_scores)):
        student_scores[n] = int(student_scores[n])
    print(student_scores)

    max_score = 0

    for n in student_scores:
        if n > max_score:
            max_score = n
        else:
            max_score = max_score

    print(f"THe highest score in the class is: {max_score}")

heights_score()