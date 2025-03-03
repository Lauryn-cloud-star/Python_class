def account_details():
    word = "welcome dear"
    details = {"account number": int(input("please enter your account number")),
			"visa_card_number": int(input("please enter your visa card number")),
			"password": input("please enter your account password"),
		}
    print(word)
    
    for key, value in details.items():
	    print(f"{key}: {value}")

account_details()


def account_balance():
      num1 = 3000000
      withdraw = int(input("please enter amount you want to withdraw"))

      if withdraw <= num1:
            print(f"withdrwaw of {withdraw} is sucessful ")
      else:
            print("transaction not posible due to incuficient funds")
            
account_balance()


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
      

