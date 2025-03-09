# inheritence is two individual classes sharing the same properties
# inheritence is the ability of a sub/child/derived-class to take on one or more attributs of a super/parent/base class

class Animal():
    name = ""
    color = ""
    weight = 50
    owner = ""

# a function with in aclass is cslled a method
# the statements you write in a method are called behaviours
    def sound(self): # means each individual object that will take on the attribute sound
        my_sound = print("I bark")

dog = Animal()
dog.sound()