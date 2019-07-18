'''

1、小明 体重 75。0公斤
2、小明每天跑步 会减肥 0.5公斤
3、小明每次吃东西体重增加1公斤

'''


class Person:

    def __init__(self, name, new_weight):
        self.name = name
        self.weight = new_weight

    def run(self):
        self.weight = self.weight - 0.5
        print('每天跑步会减肥0.5公斤，现在是 %s 公斤' % self.weight)
        self.

    def eat(self):
        self.weight = self.weight + 1
        print('每次吃东西体重增加1公斤，现在是 %s 公斤' % self.weight)


student = Person('小明', 75)
student.run()
student.run()
student.eat()
