class Fruits:
  #what we have on the left are the properties and on the write are the values   
    def __init__(fruit,name,color,size,taste,price):
        fruit.name = name
        fruit.color = color
        fruit.size = size
        fruit.taste = taste
        fruit.price =  price
# here we are creating a variable that will store an object hence we write it in small letters
mango = Fruits("mango", "yellow", "small", "sweet", "Ugx2000")
apple = Fruits("apple", "green", "small", "sweet", "Ugx4000")
grapes = Fruits("grapes", "purple", "small", "bitter sweet", "Ugx7000")
print(f"{mango.name:}, {mango.color:}, {mango.size}" )
print(mango.name)

class Animal:
    def __init__(animal, name,color,size,home,food):
        animal.name = name
        animal.color = color
        animal.size = size
        animal.home = home
        animal.food = food
    
    #a method is something a class can do or does to its self
    
    def details(animal):
        print(f"animal_name: {animal.name}, animal_size:{animal.size}")

# means dog class is inheriting from the animal class
class Dog(Animal):
    def sound(self):
        print("dog  barks")

class Germansheperd(Dog):       
     def greet(selff):
         print("it wegs")
germansheperd = Germansheperd("Bixby", "brown", "domestic", "german_food")
germansheperd

dog = Dog("ruby","brown","medium","domestic","dog_food" )





