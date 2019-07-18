class Animal:

    def eat(self):
        print("吃")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def drink(self):
        print("喝")

#继承的语法 class 类名(父类名)
class Dog(Animal):

    def dark(self):
        print("汪汪叫")

#继承=派生  父类=基类
samoye = Dog()
samoye.run()
samoye.sleep()
samoye.dark()
samoye.eat()
samoye.drink()