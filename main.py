#Опис  класу
class Dog():

    def __init__(self, name, age):
       self.name=name
       self.age=age

    def sit(self):
        print(self.name+ " is now sitting!")

# створення екземпляру класу Dog
myDog=Dog("Jerry",2)



print(f"Dog name: {myDog.name}. Age: {myDog.age}")
myDog.sit()

myDog1=Dog("Tom",5)
print(f"Dog name: {myDog1.name}. Age: {myDog1.age}")
myDog1.sit()


