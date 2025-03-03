# a fuction can not have the same name as a variable
#a variable with in a dunction block can never be accessed outside the function2
num = int(input("enter the number of entries\n"))
dict = {input("enter key: \n"): input("enter value\n")for _index in range(num)}
print(dict)


def students():
    total =  int(input("enter the number of entries\n"))
    capture = {input("enter key: \n"): input("enter value\n")for _index in range(total)}
    #print(capture)
students()

def display_product(name, price):
    print(f"The product {name} costs ${price:.2f}.")

display_product("Laptop", 999.999)
#students()
# a value students and capture are local variables
# local variable are variables limited within a aparticular function and can not be accessed outside a function                                                                                                                                                                                                                                                                                                                                                                                                                                        
print(students)

    
