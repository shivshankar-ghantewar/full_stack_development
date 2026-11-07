# Abstraction means hiding internal implementation details and showing only the essential functionality to the user.

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("dog barks")

class cat(Animal):
    def sound(self):
        print("cat meows")

d=Dog()
d.sound()

c=cat()
c.sound()

# a=Animal()  
# a.sound()  # cant call because of abstraction