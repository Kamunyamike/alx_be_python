class Bird:
    def fly(self):
        return "flying"
class Mammal:
    def run(self):
        return "running"
class Bat(Bird, Mammal):
    pass


bat = Bat()
print(f"A bat is has unique characteristics of {bat.fly()} and {bat.run()}. What a unique feature!")