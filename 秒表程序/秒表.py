'''
需求：
1、以毫秒为单位显示当前时间
2、可以通过输入开始、结束控制秒表
3、将逻辑打包成windows应用

'''

import datetime
import sys


class Clock:

    def __init__(self, control):
        self.control = control

    def run(self):
        if self.control == 'start':
            print('【开始计时】')
            while self.control:
                time_now = datetime.datetime.now().strftime('%H:%M:%S.%f')
                print(time_now)

    def stop(self):
        if self.control == 'stop':
            print('===退出程序===')
            sys.exit()


sec = Clock('start')
sec.run()

sec = Clock('stop')
sec.stop()