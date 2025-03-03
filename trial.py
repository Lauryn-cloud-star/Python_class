def account_details():
    word = "welcome dear"
    details = {"account_number": int(input("please enter your account number")),
              "visa_card_number": int(input("please enter your visa card number")),
              "password": input("please enter your account password"),
             }
    print(word)
    for key, value in details.items():
        print(f"{key}: {value}")

account_details()

def account_balance():
    num1 = 3000000
    withdraw = int(input("please enter amount"))
    if withdraw <= num1:
        print("withdrawing amount")
    else:
        print("insufficient funds available")