# object_oriented programming
#class, object, properties(attributes, characteristics, features)
#methods, constructors
# principles of oop(abstruction, encapsolation, inheritence and polymorphism)
# overloading and overriding 
# oop is a programming concept(paradigm or arrangement,belief) that advocates writing software based on real world objects
# objects are gotten from classes or they are classified.
# classes are identified in singular hence the number of individuals are the ones that will make it plural.
# a class is a blue print of an object.
# an object is an instance of a class.
# classes define the features, attributes, characteristics of object
# date, time, venue, name of the  guest, contacts, D and D etc
# "is a" is a phrase used to identify a class of a particular object
# an object should fulfill all the properties of a clss
# if the class is an integer you out 0
# the name of the class should start with a capital letter
# the dop operator is used to access the name of the property of an object
students = [ "ajaohn", "Hope", "Glen", "Lianca"]
student1 = {"name" : "Lauryn", "Gender": "Female", "School": "refactory"}

class laptop():
    pass

class Food():
    name = ""
    price = ""
    taste = ""
    calories = 0
    food_value = ""
# creating objects out of the class  food
matooke = Food()
matooke.name = "matooke"
matooke.price = "5000"
matooke.taste = "delicious"
matooke.calories = "5"
matooke.food_value = "starch"

sparg = Food()
sparg.name = "sparg"
sparg.price = "7000"
sparg.taste = "delicious"
sparg.calories = "5"
sparg.food_value = "carbohydrates"

print(sparg.name)



