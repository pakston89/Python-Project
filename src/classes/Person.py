
class Person:

    def __init__(self, name, lastName, age, gender):
        
        self.name = name
        self.lastName = lastName
        self.age = age
        self.gender = gender
    
    def run(self):
        print(self.name, " is running...")

    def birthday(self):
        self.age = self.age + 1
        print(self.age)


