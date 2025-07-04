#The program asks the user for results from different students on the course. 
# These include exam points and numbers of exercises completed.
# The program then prints out statistics based on the results.
# The program keeps asking for input until the user types in an empty line.
# You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.
# The program keeps asking for input until the user types in an empty line. 
# You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.

def subjects():
    exam_points = []
    exe_completed = []
    while True:
        ep_ec = input("Exam points and exercises completed: ")
        if ep_ec != "":
            list_subjects = ep_ec.split()
            e_p = int(list_subjects[0])
            e_c = int(list_subjects[1])
            exam_points.append(e_p)
            exe_completed.append(e_c)
        else:
            break
        
    return exam_points, exe_completed 

exam, exercises = subjects()

#print("Exam points:", exam)
#print("Exercises points:", exercises)

#The exercises completed are converted into exercise points, so that completing at least 10% of the exercises grants one point,
# 20% grants two points, and so forth. Completing all 100 exercises grants 10 exercise points. 
# The number of exercise points granted is an integer value, rounded down

def exercise_points(exercises):
    exercise_points_list = []
    for exe in exercises:
        points = exe//10
        exercise_points_list.append(points)
    return exercise_points_list

exercise_points_list = exercise_points(exercises)

#print("points for completed exercises:", exercise_points_list)

# The grade for the course is determined based on the following table:
# exam points + exercise points	grade
# 0–14	0 (i.e. fail)
# 15–17	1
# 18–20	2
# 21–23	3
# 24–27	4
# 28–30	5
# There is also an exam cutoff threshold. If a student received less than 10 points from the exam,
# they automatically fail the course, regardless of their total number of points.

def sum_of_points(exam, exercise_points_list):
    raw_points_list = []
    all_points_list = []
    i = 0
    for points in exam:
        raw_total = points + exercise_points_list[i]
        raw_points_list.append(raw_total)
        if points >= 10:
            all_points = raw_total
        else:
            all_points = 0
        all_points_list.append(all_points)
        i+=1
    return raw_points_list, all_points_list

raw_points_list, all_points_list = sum_of_points(exam, exercise_points_list)

#print("summary of points:", all_points_list)

def grades(all_points_list):
    i = 0
    grades = []
    for i in range(len(all_points_list)):
        final_points = all_points_list[i]
        if final_points >= 28:
            grade = 5
            grades.append(grade)
        elif final_points >= 24:
            grade = 4
            grades.append(grade)
        elif final_points >= 21:
            grade = 3
            grades.append(grade)
        elif final_points >= 18:
            grade = 2
            grades.append(grade)
        elif final_points >= 15:
            grade = 1
            grades.append(grade)
        elif final_points >= 0:
            grade = 0
            grades.append(grade)
        i+=1
    return grades

grades = grades(all_points_list)

#print("grades:", grades)

# print out the following statistics:
# Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
# 5:
# 4:
# 3: *
# 2:
# 1: **
# 0: *
# Floating point numbers should be printed out with one decimal precision.
def main(grades, raw_points_list):
    print("Statistics:")
    print(f"Points average: {sum(raw_points_list)/len(raw_points_list):.1f}")
    pass_percentage = 0
    total_subjects = len(grades)
    for grade in grades:
        if grade > 0:
            pass_percentage +=1
    return pass_percentage, total_subjects

percentage, subjects = main(grades,raw_points_list) 
print(f"Pass percentage: {(percentage/subjects)*100:.1f}")
list_for_five = 0
list_for_four = 0
list_for_three = 0
list_for_two = 0
list_for_one = 0
list_for_fail = 0

for grade in grades:
    if grade == 5:
        list_for_five += 1
    elif grade == 4:
        list_for_four += 1
    elif grade == 3:
        list_for_three += 1
    elif grade == 2:
        list_for_two += 1
    elif grade == 1:
        list_for_one += 1
    elif grade == 0:
        list_for_fail += 1
print("Grade distribution:")
print(f"5: {'*' * list_for_five}")
print(f"4: {'*' * list_for_four}")
print(f"3: {'*' * list_for_three}")
print(f"2: {'*' * list_for_two}")
print(f"1: {'*' * list_for_one}")
print(f"0: {'*' * list_for_fail}")
