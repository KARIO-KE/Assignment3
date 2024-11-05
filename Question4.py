class Cat:
    def make_sound(self):
        print("Meow!")
class Dog:
    def make_sound(self):
        print("Woof!")
def make_animal_sound(animal):
    animal.make_sound()
cat = Cat()
dog = Dog()
make_animal_sound(cat)
make_animal_sound(dog)
