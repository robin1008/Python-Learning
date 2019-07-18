#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import pyperclip

# 口令保管箱，实现功能：存储账号及密码，且能够拷贝至剪切板中

PASSWORDS = {'12306_pwd': 'aaa', 'sina_pwd': '123456'}


if len(sys.argv) < 2:
    print('usage: python pw.py [account] - copy accout password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('password for ' + account + ' copied to clipboard')
else:
    print('There is no accout named: ' + account)