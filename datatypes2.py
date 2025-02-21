#sequence
#in python where you find a variable that has more that one value enclosed in brackets is called a list(a collection of values in one single variable)
#a bol
num1, num2, num3 = 100, 200, 300
numbers = [100, 200, 300]
numders1 = [num1, num2, num3]
numbers2 =[]
things=[100, "hello", 200.0, True, [1, 2, 3]]
print(type(numbers2))
print(type(True))
print(things[4][2])
trouble = [20, [30, [100, 20, [500]]]]
print(trouble[1][1][2][0])
trouble.append(1000)
print(trouble)
trouble.pop()
print(trouble)

#tuple
#tuple is a read only sequence(its content is put inside carl brackets also knlown as paranthesis)
mytuple = (100, 200, 300)
print(type(mytuple))