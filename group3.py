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