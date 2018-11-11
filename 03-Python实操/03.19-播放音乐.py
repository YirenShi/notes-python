import time
import pygame
#pip install pygame


#播放音乐路径
filePath = r"C:\Users\Zhangyadi\Desktop\project\113播放音乐\1.mp3"

#初始化
pygame.mixer.init()


#加载音乐
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()

#
time.sleep(300)
#暂停
pygame.mixer.music.pause()

#停止
pygame.mixer.music.stop()









