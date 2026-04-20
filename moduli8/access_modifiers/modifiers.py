class Myclass():
    def __init__(self):
        self.public_variable = "this is public"
        self.__private_variable = "this is privat"

my_class = Myclass()
print(my_class.public_variable)
#print(my_class.__private_variable)
print(my_class._protected_variable)