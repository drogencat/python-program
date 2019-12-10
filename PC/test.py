import pygame

import sys

pygame.init()  # 初始化pygame
size = width, height = 500, 800  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

while True:  # 死循环确保窗口一直显示
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()

pygame.quit()  # 退出pygame
