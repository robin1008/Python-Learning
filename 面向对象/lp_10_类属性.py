class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        print("工具名称是 %s" % self.name)

        Tool.count += 1

# 创建工具对象
tool1 = Tool("计算器")
tool2 = Tool("键盘")

# 输出工具对象的总数
print(Tool.count)