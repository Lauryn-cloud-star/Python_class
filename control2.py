num = int(input("what is your numder"))
if num >= 0:
    print("you have entered a positive number")
else:
    print("you have enytered a negative numder")

if num % 2 == 0:
    print("you have enterd an even number")
else:
    print("you have entered an odd number")
if num  ** 2 > 50:
        print("the square is greater than 50")
else:
        print("the square is less than 50")


marks = int(input("the scored marks"))
if marks >= 90:
     print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
mark = int(input("the scored mark"))
if mark >= 90:
    print("A")
    
else:
    print("B")
    if mark >= 40:
         print("Tried")
    if mark >= 30:
         print("work harder")
    else:
         print("failed")
         

fruits = ["apple", "banana", "cherry", "mango"]
for p in fruits:
     if p == "cherry":
         pass
     print(p)
