def student_details():
    details = {"name": input("Student_name"), 
               "gender": input("enter gender"),
               "date of birth":input("date of birth"), 
               "age": int(input("Enter age")),
               "program": input("Enter program"),
               "year of study": int(input("Enter year of study")),
               "faculty": input("Enter the faculty"),
               "test1_marks": int(input("Enter test1 marks")),
               "test2_marks": int(input("Enter test2 marks")),
               "final_marks": int(input("Enter final marks")), }
    
    sum = (((details["test1_marks"]) + (details["test2_marks"]))/2)*0.4
    print(type(sum))
    final_mark = details["final_marks"]*0.6
    total = sum + final_mark
    print(f"average out of 40 is {sum}")
    print(f"final_marks is {final_mark}")
    print(f"total is {total}")
student_details()


