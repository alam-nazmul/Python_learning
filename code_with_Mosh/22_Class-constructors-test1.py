class Person():
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("Talk Anything")


jhon = Person("Nazmul")
print("Hi" + " " + jhon.name)
jhon.talk()

bob = Person("Bob")
print(bob.name)
bob.talk()