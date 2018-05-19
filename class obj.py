class second:
    color = 'red'
    form = 'circle'
    square = 'big'
    def changecolor(self, newcolor):
        self.color = newcolor
    def changeform(self, newform):
        self.form = newform
    def changesquare(self, newsquare):
        self.square = newsquare

obj1 = second()
obj2 = second()

print(obj1.color, obj1.form, obj1.square)
print(obj2.color, obj2.form, obj2.square)

obj1.changecolor(input('Введите цвет обьекта 1 - '))
obj1.changeform(input('Введите форму обьекта 1 - '))
obj1.changesquare(input('Введите размер обьекта 1 - '))
obj2.changecolor(input('Введите цвет обьекта 2 - '))
obj2.changeform(input('Введите форму обьекта 2 - '))
obj2.changesquare(input('Введите размер обьекта 2 - '))

print(obj1.color, obj1.form, obj1.square)
print(obj2.color, obj2.form, obj2.square)
