class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move here")


    def draw(self):
        print("Game draw")

'''
point = Point()
point.x = 10
point.y = 20

print(point.x)
print(point.y)

'''


point = Point(10, 20)
print(point.x)