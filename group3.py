def capture():
    student_details = {"name:" : input("enter student's name"), 
                       "Age:" : int(input("enter student's age")),
                       "Program:" : input("enter the student's program"),
                       "Gender:" : input("enter the student's gender"),
                       "Date of birth:" : input("enter the student's date of birth(dd/mm/yyyy)"),
                       "Faculty:" : input("enter the student's Faculty"),
                       "Year of study:" : int(input("enter student's year of study")),
    }
    test1 = int(input("enter the marks scored in test1"))
    test2 = int(input(" enter the marks scored in test2"))
    average = (test1 + test2)/2
    summation = (average * 40/100)
    final_exams = int(input("enter the marks scored in the final exam "))
    final_mark = (final_exams * 60/100)
    actual_course_unit = (summation + final_mark)
    student_details["actual_course_unit"] = actual_course_unit

    for key, value in student_details.items():
        print(f"{key}: {value}")

capture()


def students_perfomance():
    students_list =[]
    num = int(input("Enter Number of student entrie: "))

    for _ in range(num):
     students = {}
    students["name"] = input("please enter student name: ")
    students["Age"] = int(input("please enter student age: "))
    students["gender"] = input("please enter student gender(male or female): ")
    students["program"] = input("please enter student's program: ")
    students["year_of_study"] = int(input("please enter student's year of study: "))
    students["test1"] = int(input("please enter marks scored in test1: "))
    students["test2"] = int(input("please enter marks scored in test2: "))
    students["course_work"] = int(input("please enter marks scored in course_work: "))
    students["exam"] = int(input("please enter marks scored in exam: "))
    students["best_done"] = best_done(students["test2"],students["course_work"])
    students["final_exam"] = final_exam (students["best_done"], students["exam"])

    students_list.append(students)
    return students_list




def best_done(test2, course_work):
    return ((test2 + course_work)/2) * 0.4


def final_exam(best_done, exam):
    return best_done + (exam * 0.6)


all_students = students_perfomance()

for student in all_students:
     print(student)
