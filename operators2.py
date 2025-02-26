#comparison operators 
#these compare two values and rerurn a boolean value
# in mathematics we have operators like <, >, <=, >=, ==, !=
# ! means not equal to
comp1 = 20
comp2 = 40
print(comp1 < comp2)
print(comp1 >comp2)
print(comp1 >= comp2)
print(comp1 <= comp2)
print(comp1 != comp2)
print(comp1 == comp2)

#logical operators
# lojical operator include and, or and not(for and it is the & and some programming languages use(1)  and or is(||) and not is (!)
log1 = 5
log2 = 6
print(log1 > log2) and (log2 < log1)
#not is used to negate a boolean value
#not comes before the variable
print (not (log2 < log1))

#for or it valuates to true if everything written is true and false if one of things is false
print(log1 > log2) or (log2 < log1)

#
print(True and True)

#prints false if one of the values is false
print(True and False)

#prints false if one of the values is true
print(not True)

#prints true if one of the values is true
print( True or True)

#prints true if one of the values is true
print(True or False)







#membership operators
#we use "in" and "not in"
members = (10, 20, 30, 40, 50)  
print(20 in members)
print(20 not in members)

name="Lauryn"
print("a" in name)
print("a" not in name)

#identify operators
#identity we use "is" or "isnot"
print(10 is 10)
print(10 is not 10)
print((10, 20, 30, 40, 50) is members)

