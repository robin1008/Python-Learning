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


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")


class Cat(Animal):

    def catch(self):
        print("我会抓老鼠")

#XiaoTianQuan类的对象xtq，不能调用Cat类的方法
#儿子可以继承父类以及爷爷的属性和方法
xtq = XiaoTianQuan()
