#! /usr/bin/env python3
# -*- coding:utf-8 -*-
'''
程序实现：在一段以行为单位分隔的文本前加上一些字符，例如 *
思路：
1、将数据从剪切板粘贴出
2、对数据进行处理
3、将数据拷贝回剪切板
'''

import pyperclip


text = pyperclip.paste()
content = text.split('\n')
for i in range(len(content)):
    content[i] = '* ' + content[i]
text = '\n'.join(content)  # 需要使用join方法，将列表用换行符连接成字符串，这一步很关键
pyperclip.copy(text)