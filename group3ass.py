def students_performance():
    # Welcoming remarks
    print("Welcome to the Student Performance System!")
    print("Kindly, you will be required to input data where necessary. Thank you.")
    
    students_list = []
    num = int(input("Please enter the number of entries: "))  # Input for number of students

    # Loop to collect information for each student
    for _ in range(num):
        students = {}  # Initialize an empty dictionary for each student
        
        # Collect student information
        students["name"] = input("Please enter student name: ")
        students["age"] = int(input("Please enter student age: "))
        students["gender"] = input("Please enter student gender (male or female): ")
        students["program"] = input("Please enter student's program: ")
        students["year_of_study"] = int(input("Please enter student's year of study: "))
        students["test1"] = int(input("Please enter marks scored in test1: "))
        students["test2"] = int(input("Please enter marks scored in test2: "))
        students["course_work"] = int(input("Please enter marks scored in course work: "))
        students["exam"] = int(input("Please enter marks scored in exam: "))

        # Calculate best_done and final_exam marks
        students["best_done"] = best_done(students["test2"], students["course_work"])
        students["final_exam"] = final_exam(students["best_done"], students["exam"])

        # Append the student's data to the students_list
        students_list.append(students)

    return students_list

# Function to calculate the best done score (average of test2 and course work)
def best_done(test2, course_work):
    return ((test2 + course_work) // 2) * 0.4

# Function to calculate the final exam score based on the best done and exam marks
def final_exam(best_done, exam):
    return best_done + (exam * 0.6)

# Collect data for all students
all_students = students_performance()

# Print out the collected information for each student
for student in all_students:
    print(student)
