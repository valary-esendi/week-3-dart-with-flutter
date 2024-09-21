
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
    
class Cow(Animal):
    def sound(self):
        return "Mooo!"

def animal_sound(animal):
    print(animal.sound())

# Example Usage
dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)