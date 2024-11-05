
class Animal:
    def eat(self):
        print("The animal is eating.")
    def sleep(self):
        print("The animal is sleeping.")
class Dog(Animal):
    # New method specific to Dog
    def bark(self):
        print("The dog is barking.")
my_dog = Dog()
my_dog.eat()
my_dog.sleep()
my_dog.bark()
