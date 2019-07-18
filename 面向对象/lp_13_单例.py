class MusicPlayer:

    # 记录第一个被创建对象的引用
    instance = None

    # 重写new方法
    def __new__(cls, *args, **kwargs):

        # 判断类属性是否为空，使用身份运算符is
        if cls.instance is None:
            # 为空的话，返回创建的内存空间赋值给类属性，父类的方法用super().调用，new为静态方法，需要传入cls参数
            cls.instance = super().__new__(cls)
        # 返回类属性保存的对象引用
        return cls.instance


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)