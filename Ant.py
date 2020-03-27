import os
import time

# 屏幕分辨率
base_x = 1080
base_y = 2340

x_start = 105
x_end = 880
y_start = 480
y_end = 840

# 输入自己排名
myRank = 2
# 输入好友总数
friendsNum = 49


def tap_screen(tap_x, tap_y):
    cmd = 'adb shell input tap {x1} {y1}'.format(
        x1=tap_x / 1080 * base_x,
        y1=tap_y / 2340 * base_y,
    )
    os.system(cmd)


def swipe_screen(tap_sx, tap_sy, tap_ex, tap_ey, timeLen):
    cmd = 'adb shell input swipe {x1} {y1} {x2} {y2} {times}'.format(
        x1=tap_sx / 1080 * base_x,
        y1=tap_sy / 2340 * base_y,
        x2=tap_ex / 1080 * base_x,
        y2=tap_ey / 2340 * base_y,
        times=timeLen
    )
    os.system(cmd)
    # print(tap_sx, tap_sy, tap_ex, tap_ey, timeLen)


def init():
    tap_screen(548, 339)
    tap_screen(548, 339)
    # 收自己的蚂蚁能量
    print("正在收取自己的蚂蚁能量")
    getGreenEnergy()
    print("收取自己的蚂蚁能量结束")


def getGreenEnergy():
    for x in range(x_start, x_end, 100):
        for y in range(y_start, y_end, 100):
            tap_screen(x, y)


def changeUser():
    # 滑动到排行榜第一位
    swipe_screen(550, 1615, 250, 918, 1000)
    # 第十次展开更多好友列表
    for i in range(10):
        if i != myRank:
            print("第{}位朋友".format(1 + i))
            # 点击进入朋友蚂蚁森林界面
            tap_screen(650, 2230)
            # 偷蚂蚁能量
            getGreenEnergy()
            # 退出该朋友界面
            swipe_screen(0, 900, 370, 900, 500)
            print("收取第{}位朋友的蚂蚁能量结束".format(1 + i))
        # 再次滑动固定距离
        swipe_screen(550, 1155, 550, 1155 - 205, 1000)

    # 点开查看更多好友
    tap_screen(650, 2180)
    time.sleep(2)
    swipe_screen(550, 1155, 550, 1155 - 209, 1000)

    for i in range(friendsNum - 10):
        if i != myRank:
            print("第{}位朋友".format(11 + i))
            # 点击进入朋友蚂蚁森林界面
            tap_screen(650, 2230)
            # 偷蚂蚁能量
            getGreenEnergy()
            # 退出该朋友界面

            swipe_screen(0, 900, 370, 900, 500)
            print("收取第{}位朋友的蚂蚁能量结束".format(11 + i))
        # 再次滑动固定距离
        swipe_screen(550, 1155, 550, 1155 - 209, 1000)


if __name__ == '__main__':
    init()
    changeUser()
