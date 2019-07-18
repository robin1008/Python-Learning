class MusicPlayer(object):

    # 记录第一个被创建对象的引用
    instance = None

    init_flag = False

    # 重写new方法
    def __new__(cls, *args, **kwargs):

        # 判断类属性是否为空，使用身份运算符is
        if cls.instance is None:

            # 为空的话，返回创建的内存空间赋值给类属性，父类的方法用super().调用，new为静态方法，需要传入cls参数
            cls.instance = super().__new__(cls)

        # 返回类属性保存的对象引用
        return cls.instance

    def __init__(self):

        # 1、判断初始化动作，为真直接返回
        if MusicPlayer.init_flag:
            return

        # 2、没有调用的话，调用一次初始化方法
        print("调用初始化方法")

        # 3、调用完成后，改变类属性的值，让初始化动作不再执行
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)