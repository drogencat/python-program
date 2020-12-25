import os
import cv2
import numpy as np
import time
'''别踩白块 -- 失败（截图速度限制）'''

def screenPhoto():
    os.system("adb shell screencap -p /sdcard/game.png")  # cmd运行
    os.system("adb pull /sdcard/game.png /Users/drogencat/Desktop/python/screenPhoto/game.png")  # 存入电脑里面
    image = cv2.imread('/Users/drogencat/Desktop/python/screenPhoto/game.png')
    height = len(image)
    width = len(image[0])
    # 裁剪顶部白色装修
    image = image[int(height - (height - 150)):height, 0:width]
    im = cv2.resize(image, (1080, 2160))
    lower_red = np.array([0, 0, 0])
    upper_red = np.array([180, 255, 46])
    # 找到黑色区域
    mask = cv2.inRange(im, lower_red, upper_red)
    # 绘制轮廓
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        # x，y是矩阵左上点的坐标  w，h是矩阵的宽和高
        x, y, w, h = cv2.boundingRect(contours[i])
        # 计算中心点x坐标 x = x + w/2,y坐标 y = y + h/2
        pushX = x + w / 2
        if i >= 2:
            pushY = y + h / 2 + 540 + 150
        else:
            pushY = y + h / 2 + 150

        # 点击屏幕
        os.system('adb shell input tap  %s %s  ' % (pushX, pushY))

'''
计算偏移量
'''


def speedFactor():
    # 速度因子
    speed = 0

    return speed


if __name__ == '__main__':
    while True:
        screenPhoto()
