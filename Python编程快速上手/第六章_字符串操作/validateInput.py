#!/usr/bin/env python
#-*- coding:utf-8 -*-


while True:
    print('input your age')
    age = input()
    if age.isdecimal():
        print('your age is: '+ str(age))
    break

