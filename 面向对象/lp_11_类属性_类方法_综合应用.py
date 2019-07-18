class Game(object):

    # 定义类属性
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 定义静态方法（方法内部不需要访问实例属性和类属性）
    @staticmethod
    def show_help():
        print("这是游戏帮助")

    # 定义类方法（方法内部只要访问类属性）
    @classmethod
    def show_top_score(cls):
        print("历史最高分是 %d" % cls.top_score)

    # 定义实例方法（方法内部需要访问实例属性）
    def start_game(self):
        print("%s 游戏开始啦..." % self.player_name)


# 查看游戏帮助（类名.静态方法）
Game.show_help()

# 查看历史最高分（类名.类方法）
Game.show_top_score()

# 实例方法的调用，需要先创建对象
game = Game("小明")
game.start_game()