'''
    Base template for Animals
    What it is?
    What it does?
    Class name: Capital letter
    Function name: small letter and every other word in the name starts with capital letter


'''
class Animal:

    is_animal = True

    def __init__(self, name='', height=0, is_predator= False):
        self.__name = name
        self.height = height
        self.is_predator = is_predator
        self.sound_type = None  # line 1: added so that it can be accessed later

    def sound(self, sound_type, db):
        self.sound_type = sound_type # before adding this line along with line 1, it was a local variable to this method only, now it's public and can be accessed by other methods
        if db > 10:
            print(f'I am loud, don\'t play me on Sundays')
        else:
            print(f'I {sound_type}')
   
    def introduce_yourself(self):
        print(f'I am {self.__name}. My height is {self.height}. Am I a predator? {self.is_predator}')
        print(f'I make {self.sound_type} sound')
        print(f'is animal? {Animal.is_animal}')

    def __repr__(self):

    #def __str__ (self):


dog= Animal('dog', 2, True)
dog.sound('bark', 5)
dog.introduce_yourself()

cat= Animal()