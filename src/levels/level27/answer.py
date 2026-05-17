class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "...\n"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("灏忚姳")
print(cat.speak())
