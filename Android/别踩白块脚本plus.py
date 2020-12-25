import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import time

'''别踩白块pc 模拟器 -- 成功'''


def screenPhotoUsePositionRGB():
    box = (0, 100, 500, 900)
    im = ImageGrab.grab(box)
    # 参数 保存截图文件的路径
    im.save('/Users/drogencat/Desktop/python/screenPhoto/game.png')
    # 调用识别
    filePath = "/Users/drogencat/Desktop/python/screenPhoto/game.png"
    image = cv2.imread(filePath)

    for i in range(0, 4):  # y 轴
        for j in range(0, 4):  # x轴
            rgb = image[717 - 210 * i, 130 * j + 65, 0]
            if 32 == rgb:
                # print("x = %s , y = %s , rgb :%s " % (100 * j + 65, 717 - 210 * i, rgb))
                # print("点击x: %s , y : %s" %(130 * j + 70, 850 - 200 * i))
                if i == 0 and j == 0:
                    pyautogui.click(130 * j + 70, 850 - 140 * i)
                    continue
                else:
                    pyautogui.click(130 * j + 70, 850 - 140 * i + 120)
                    continue


if __name__ == '__main__':
    while True:
        screenPhotoUsePositionRGB()
