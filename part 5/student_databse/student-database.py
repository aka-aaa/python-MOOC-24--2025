def add_student(students:dict, name:str):
    students[name] = []
   
def print_student(students:dict, name:str):
        if name in students:
            total = 0
            courses = students[name]
            print(f"{name}:")
            if not courses:
                print(" no completed courses")
                return
            print(f" {len(courses)} completed courses:")
            for course_name, grade in courses:
                print(f"  {course_name} {grade}")
                total += grade
            average = total / len(courses)
            print(f" average grade {average}")
        else:
            print(f"{name}: no such person in the database")

def add_course(students:dict, name:str, course:tuple):
    course_name, grade = course
    if grade == 0:
        return
    courses = students[name]
    for i in range(len(courses)):
        old_name, old_grade = courses[i]
        if old_name == course_name:
            if grade>old_grade:
                courses[i] = (course_name, grade)
            return
        
    courses.append((course_name,grade))

def summary(students:dict):
    most_courses = 0
    most_courses_name = ""
    best_average_grade = 0
    best_average_grade_name = ""
    for name in students:
        total = 0
        courses = students[name]
        length = len(courses)
        if length > most_courses:
            most_courses = length
            most_courses_name = name
        for course_name, grade in courses:
            total += grade
        average = total / len(courses)
        if average > best_average_grade:
            best_average_grade = average
            best_average_grade_name = name      
    print(f"students {len(students)}")
    print(f"most courses completed {most_courses} {most_courses_name}")
    print(f"best average grade {best_average_grade} {best_average_grade_name}")



