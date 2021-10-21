class point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = point()
point1.move()
point1.draw()
point1.x = 20
point1.y = 10
print(point1.x)
print(point1.y)
