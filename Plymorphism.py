##Base Class

class Animal:
    def speak(self):
        return "Sound of the animal"
    def play(self):
        return "The animal is playing"

## Derived Class 1
class Dog(Animal):
    def speak(self):
        return "woof!"
    def play(self):
        return "The dog is playing in the park"

## Derived Class 2
class Cat(Animal):
    def speak(self):
        return "Meow!"
    def play(self):
        return "The cat is playing in the house"

class Cow(Animal):
## function that demos polymorphism
    def speak(self):
        return "MOO!"
    def play(self):
        return "The Cow is playing in the farm"


def animal_speak(animal):
    print( animal.speak())
    print(animal.play())
## Create Dog and cat object
dog = Dog()
cat = Cat()
cow = Cow()

# print(dog.speak())
# print(cat.speak())
# print(cow.speak())
animal_speak(dog)
animal_speak(cat)
animal_speak(cow)
