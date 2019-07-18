#  编写代码，如果变量 spam 中存放 1，就打印 Hello，如果变量中存放 2，就 打印 Howdy，如果变量中存放其他值，就打印 Greetings!
spam = int(input('please input number:'))
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
