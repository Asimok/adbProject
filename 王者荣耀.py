# -*- coding: utf-8 -*-

import logging
import os
import time

# 屏幕分辨率
base_x = 1080
base_y = 2340

# 刷金币次数
repeat_times = 60

# 游戏时长
playLen = 110
# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(tap_x, tap_y, sleepTime):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=tap_x / 1080 * base_x,
        y1=tap_y / 2340 * base_y,
    )
    os.system(cmd)
    if sleepTime > 0:
        print('等待' + str(sleepTime) + '秒')
        time.sleep(sleepTime)


def do_money_work():
    print('#1 下一步')
    tap_screen(1725, 895, 2)

    print('#2 闯关')
    tap_screen(1676, 863, 8)

    # print('#3 确定')
    # tap_screen(2077, 1004, 8)

    # 游戏时间
    print("#4 等待110")
    for innerTime in range(playLen):
        tap_screen(1000, 600, 0)
        # print(i)
        time.sleep(1)

    print('#7 再次挑战')
    tap_screen(1970, 984, 1)


if __name__ == '__main__':
    for i in range(repeat_times):
        try:
            logging.info('round {}'.format(i + 1))
            do_money_work()
        except KeyboardInterrupt:
            os.system('kill-server')
            print('进程停止')
            exit(0)
