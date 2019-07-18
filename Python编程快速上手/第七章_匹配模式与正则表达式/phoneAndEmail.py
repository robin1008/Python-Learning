#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
如果拷贝的字符串中有中文，运行程序时会有如下错误信息：
    return stdout.decode(ENCODING)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xba in position 1: invalid start byte
'''

import pyperclip, re
'''
从剪切板中查找出指定格式的电话号码、email
'''

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.a-zA-Z{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard 已拷贝至剪切板')
    print('\n'.join(matches))
else:
    print('没有找到匹配的内容')