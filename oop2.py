Animal =  {}
# from line 4 to 9 are the properties, attributes or features for yhe class
class Animal():
    name = ""
    family = ""
    size = ""
    color = ""
    habitat = 0
    food = ""

#creating objects of the class animal
dog = Animal()
dog.name = "dog"
dog.family = "mammalia"
dog.size = "mediam"
dog.color = "brown"
dog.habitat = "domestic"
dog.food= "meat"


cow = Animal()
cow.name = "cow"
cow.family = "mammalia"
cow.size = "large"
cow.color = "whitee"
cow.habitat = "domestic"
cow.food= "grass"

print(f"cow :{cow.name:},{cow.family:},{cow.size:}")
print(Animal)
print(cow)