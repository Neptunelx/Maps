# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:02:25 2021

@author: Neptune
"""

import pygame as pg

class Resource:
    #记录所有固定数据
    
    #屏幕尺寸，全屏与否，图片颜色深度
    "地图是20*10个格子，一个格子占60*60个像素"
    SCREEN_WIDTH=1200              
    SCREEN_HEIGHT=600
    SCREEN_FLAG=0
    SCREEN_IMG_BIT=32
    #游戏标题
    GAME_TITLE='坦克大战'
    
    bg=pg.image.load('BG.jpeg')



    #障碍物图片
    OBS_IMAGES=[
        pg.image.load("./images/steels.gif"),
        pg.image.load("./images/walls.gif"),
        pg.image.load("./images/grass.gif"),
        pg.image.load("./images/water.gif")
        ]
    
    #0无 1钢铁 2瓷砖 3草地 4水域                    
    "钢铁无法通过和被子弹击穿 瓷砖被子弹击穿后可通过 草地可以被所有坦克和子弹通过，在草地中敌方看不见 水域坦克永远过不了，子弹可以穿透"
    MAPS=[
          #第一关
        [
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
           [1,0,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,0,1],
           [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1],
           [1,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,1,0,1],
           [1,0,1,0,0,1,0,0,2,2,2,0,0,0,0,0,0,1,0,1],
           [1,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,1],
           [1,0,0,0,0,0,2,0,0,0,0,0,2,0,1,0,2,0,0,1],
           [1,0,0,1,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,1],
           [1,0,0,0,2,0,0,1,0,0,0,0,0,0,2,0,0,0,0,1],
           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        ]
    ]




#%%
pg.init()

screen=pg.display.set_mode((Resource.SCREEN_WIDTH,Resource.SCREEN_HEIGHT),
                           Resource.SCREEN_FLAG,Resource.SCREEN_IMG_BIT)  

#screen.bilt(Resource.OBS_IMAGES[0],0,0)

a=Resource.OBS_IMAGES

screen.fill(pg.Color("blue"))
screen.blit(Resource.bg,(0,0))
screen.blit(a[0],(800,400))
pg.display.update()

while True:
    e=pg.event.poll()
    if e.type==pg.QUIT:
        break

pg.quit()