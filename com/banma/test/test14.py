class Animal(object):
    def run(self):
        print("Animal is runnnig ...")

class Dog(Animal):
    def run(self):
        self.zzz = 123
        print("Dog is runnign...")
    def eat(self):
        print("Eating meat...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")

dog=Dog()
dog.run()
cat = Cat()
cat.run()
a=list(range(10))
print(a)
a=isinstance(dog ,Animal)
print(a)
b=isinstance(cat ,Cat)
print(b)

def run_twice(animal):
    animal.run()
    animal.run()

a= Animal()
b=Dog()
c = Cat()
run_twice(a)
run_twice(b)
run_twice(c)
print(dir(Dog))
print(dir(b))