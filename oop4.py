class Animal:
    # this a constructor is used to initialise /giving values for objects
    # name is the urgument and animal_name is the property. then self.animal_name is the parameter
    # white is the parameter for color and the value for the property animal.color 
    # there has to be a representatio f the object in the constructor thats why we put there a keyword self
    #SELF IS AN IDENTIFIER OF THE PROPERTY. 
    # kitty, small and white are urguments on line 18  but also  values to the pro
    def __init__(self, name, size, color):
        self.animal_name = name
        self.animal_size = size
        self.animal_color = color

    def sound(self):
        my_sound = "mwaaauuuu" 
        cry = print(my_sound)
        return my_sound

cat = Animal("kitty", "small", "white")
print(cat.animal_color)
cat.sound()
print(cat.animal_size)
print(cat.color)
    
