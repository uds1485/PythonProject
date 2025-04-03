### Create a class named `Flyer` with a method `fly`. Create a class named `Swimmer` with a method `swim`.
# Create a class named `Superhero` that inherits from both `Flyer` and `Swimmer` and overrides both methods.
# Create an object of the `Superhero` class and call both methods.

class Flyer:
    def fly(self):
        return "I can fly"

class Swimmer:
    def swim(self):
        return "I can swim"

class Superhero(Flyer,Swimmer):
    def fly(self):
        print( "Superhero can fly")
    def swim(self):
        print("Superhero can swim")


superman = Superhero()
superman.fly()
superman.swim()


