# Design Patterns are well-understood ways of writing code
# We do what we know from experience is going to work

# We use a fctory to provide a single pont of entry to create many types of object
from abc import ABCMeta, abstractmethod
# we may declare an Abstract Base Class as the basis for any concrete class we may need
class Animal(metaclass=ABCMeta): # we NEVER implement an abstract class
    '''Every Abstract Base Class contains NO implementation'''
    @abstractmethod
    def make_noise(self):
        pass

class Dog(Animal): # the ABC means we MUST implement as directed
    def make_noise(self):
        return 'Woof' 

class Cat(Animal):
    def make_noise(self):
        return 'Miaow' 

class Bat(Animal):
    def make_noise(self):
        return '_____' 

# We can make life easy by writing a factory
class CreatureFactory():
    '''This is a single point of access to manufacture any type of creature'''
    def make_sound(self, obj):
        return eval(obj)().make_noise() 

if __name__ == '__main__':
    cf = CreatureFactory()
    n1 = cf.make_sound('Cat')
    print(n1)
    cre = ('Cat', 'Dog', 'Cat', 'Bat', 'Dog', 'Cat')
    for _ in cre:
        print(f'{_} says {cf.make_sound(_)}')

    # grommet = Dog()
    # felix = Cat()
    # oenid = Bat()
    # print(grommet.make_noise())
    # print(felix.make_noise())
    # print(oenid.make_noise())