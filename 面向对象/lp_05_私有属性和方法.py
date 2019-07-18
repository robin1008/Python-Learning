class Women:

    def __init__(self, name):

        self.name = name
        #两个下划线表示私有属性
        self.__age = 18

    #两个下划线表示私有方法
    def __secret(self):
        #私有属性可以在方法内部进行调用
        print("%s 年龄是 %d" % (self.name,self.__age))


xiaofang = Women("小芳")

#私有属性不能被外部直接调用，不会出现智能提示
#print(xiaofang.__age)

#私有方法不能被外部直接调用
xiaofang.__secret()
