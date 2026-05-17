class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "...\n"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("小花")
print(cat.speak())
