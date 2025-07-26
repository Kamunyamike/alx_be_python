class Dog:
    def make_sound(self):
        return "Dogs bark"
class Cat:
    def make_sound(self):
        return "Cats meaw"
class Bird:
    def make_sound(self):
        return "Birds chirp"


def let_them_speak(obj):
    return obj.make_sound()

dog_obj = Dog()
cat_obj = Cat()
bird_obj = Bird()

print(let_them_speak(dog_obj))
print(let_them_speak(cat_obj))
print(let_them_speak(bird_obj))