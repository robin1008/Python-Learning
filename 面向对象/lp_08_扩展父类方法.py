class Animal:

    def eat(self):
        print("吃")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def drink(self):
        print("喝")


# 继承的语法 class 类名(父类名)
class Dog(Animal):

    def dark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")

    # 重写父类中dark方法
    def dark(self):

        # 直接重写方法
        print("啸天犬叫的不一样")

        # 使用 super(). 调用父类中原有的方法
        super().dark()

        # 重写方法中其他功能
        print("需要实现的代码")



xtq = XiaoTianQuan()
xtq.dark()