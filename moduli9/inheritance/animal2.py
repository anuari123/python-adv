class Animal:
    def __init__(self,name):
        self.name = name

    class Animal:
        def sound(self):
            print("Some generic animal sound.")

        def description(self):
            print(f"This is an animal sound named {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
    print("woof! woof!")




     def description(self):
         super().description():
         print(f"breed:{self.breed}")

animal = Animal
animal.sound()
animal.description{}

dog = Dog("Rax","Gold retrever")
dog.sound()
dog.description()





