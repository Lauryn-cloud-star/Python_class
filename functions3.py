#return expporses a avalue to be accessed out of the function
def add():
    num1 = 56
    num2 = 65
    return num1 + num2
print(add())
my_var = add()
print(my_var)

def sub():
    var = 34
    var2 = 65
    return var2 - var
print(sub())

def both():
    return sub() + add()
print(both())

def add1():
    var1 = int(input("enter the first value"))
    var3 = int(input("enter the second value"))
    return var1 + var3
print(add1())

def sub2():
    var1 = int(input("enter the first value"))
    var3 = int(input("enter the second value"))
    return var1 - var3
def both2():
    return add1() + sub2()