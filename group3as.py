def students_perfomance():
    students  = {}
    students["name"] = input("please enter student name: ")
    students["Age"] = int(input("please enter student age: "))
    students["gender"] = input("please enter student gender(male or female): ")
    students["program"] = input("please enter student's program: ")
    students["year_of_study"] = int(input("please enter student's year of study: "))
    students["test1"] = int(input("please enter marks scored in test1: "))
    students["test2"] = int(input("please enter marks scored in test2: "))
    students["course_work"] = int(input("please enter marks scored in course_work: "))
    students["exam_mark"] = int(input("please enter marks scored in exam: "))
    return students
students_data = students_perfomance
print(students_data())

def calculate_best_2(test2, course_work):
    return ((test2 + course_work) / 2) * 0.4
print(calculate_best_2(75, 80))
calculate_best_2 (45, 75)
calculate_best_2 (76, 78)                
print(calculate_best_2())

def final_mark(best_2, exam_mark):
    return best_2 + ((exam_mark) * 0.6)




  


