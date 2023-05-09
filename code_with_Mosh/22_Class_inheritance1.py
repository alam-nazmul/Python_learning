class Memo():
    def walk(self):
        print("Walk")
class Dog(Memo):
    pass

class Cat(Memo):
    pass

dog = Dog()
dog.walk()

cat = Cat()
cat.walk()