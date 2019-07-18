class Dog(object):

    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 简单玩耍" % self.name)


class XiaoTianDog(Dog):

    def game(self):
        print("%s 在天上玩耍" % self.name)


class Person(object):

    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍" % (self.name, dog.name))
        dog.game()


# 通过调用子类和父类的方法，实现不同的功能
# wangcai = Dog("旺财")
xiaotianquan = XiaoTianDog("啸天犬")
xiaoming = Person("小明")
xiaoming.game_with_dog(xiaotianquan)