class Animal:
    def eat(self):
        print("This animal is eating.")
    def sleep(self):
        print("This animal is sleeping.")
class Dog(Animal):
    def bark(self):
        print("This dog is barking.")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()