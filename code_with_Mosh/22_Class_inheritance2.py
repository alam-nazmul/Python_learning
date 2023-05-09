class Memo():
    def walk(self):
        print("Walk")


class Dog(Memo):
    def bark(self):
        print("BARK DOG")

class Cat(Memo):
    pass


dog1 = Dog()
dog1.walk()
dog1.bark()