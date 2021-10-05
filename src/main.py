from classes.Person import Person

person1 = Person("Pau", "Serratosa", 32, "Male")

person1.run()

for i in range(500):
    while person1.age < 69:
        person1.birthday()
