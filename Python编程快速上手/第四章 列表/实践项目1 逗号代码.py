'''
假定有下面这样的列表:
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有表项，表项之间以逗号和空格分隔，
并在最后一个表项之前插入 and。例如，将 前面的 spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。
但你的函数应 该能够处理传递给它的任何列表。

'''

'''
insert()方法
列表转字符串

'''
'''
spam = []
def listtostr(list1):
    print('请输入一个列表（列表形式为[xx,xx]）：')
    list1 = input()
    list(list1)
    list1 = list1 + spam
    list(list1).insert(-2,'and')
    print(list1)
    #return ' '.join(list1)

#print(listtostr(['1','2','3']))
listtostr(1)
'''
# 方法一


def listtostr(spam):
    spam[-1] = 'and ' + spam[-1]
    for i in range(len(spam)):
        print(spam[i], end=',')


listtostr(['a', 'b', 'c'])
