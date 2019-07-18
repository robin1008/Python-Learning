class MusicPlayer(object):

    # 重写new方法（new方法是默认创建对象，分配内存空间的作用）
    # __new__方法是object基类提供的内置静态方法，作用：
    # 1）在内存中为对象分配空间，2）返回对象的引用
    def __new__(cls, *args, **kwargs):

        print("创建对象，分配内存空间")

        instance = super().__new__(cls)

        return instance

    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
print(player)