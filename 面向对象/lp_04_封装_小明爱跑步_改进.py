'''

1、小明 体重 75。0公斤
2、小明每天跑步 会减肥 0.5公斤
3、小明每次吃东西体重增加1公斤

'''


class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return '我是%s， 我的体重是 %.2f' % (self.name, self.weight)

    def run(self):
        self.weight -= 0.5
        print('%s爱跑步' % self.name)

    def eat(self):
        self.weight += 1
        print('%s是吃货' % self.name)


xiaoming = Person('小明', 75)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)

