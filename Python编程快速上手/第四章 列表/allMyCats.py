cats = []
while True:
    print('请输入第'+str(len(cats)+1)+'猫的名字:(或者直接敲回车退出)')
    name = input()
    if name == '':
        break
    cats = cats + [name]
for name in cats:
    print('猫的名字是：'+ name)