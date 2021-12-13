# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:44:13 2021

@author: Neptune
"""

import pygame as pg
import numpy as np
from numpy import random
      
class DATA:
    global lst2
    #记录所有固定数据
    
    #屏幕尺寸，全屏与否，图片颜色深度
    "地图是20*10个格子，一个格子占60*60个像素"
    SCREEN_WIDTH=1200              
    SCREEN_HEIGHT=600
    SCREEN_FLAG=0    #flags=0是窗口化  flags=pg.FULLSCREEN全屏
    SCREEN_IMG_BIT=32 #颜色显示深度，一般不设置，会自动设置最佳
    #游戏标题
    GAME_TITLE='坦克大战'
    #游戏屏幕刷新率
    fps=24
    #障碍物图片
    OBS_IMAGES=[
        pg.image.load("./images/steels.gif"),
        pg.image.load("./images/walls.gif"),
        pg.image.load("./images/water.gif"),
        pg.image.load("./images/grass.gif")
        ]
    
   
    arr1 = random.randint(0,4,size=(12,22))
    lst2=arr1.tolist()
    lst2[0]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    lst2[11]=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    for i in range(1,12):
        lst2[i][0]=1
        lst2[i][21]=1
       # MAPS.append(arr1)
        #return MAPS
    
        
    #MAPS = []
    
    #MAPS.append(arr1)
    
    #0无 1钢铁 2瓷砖 3草地 4水域                    
    "钢铁无法通过和被子弹击穿 瓷砖被子弹击穿后可通过 草地可以被所有坦克和子弹通过，在草地中敌方看不见 水域坦克永远过不了，子弹可以穿透"
    MAPS=[
        
        lst2
        #第一关

    ]
    
    MAP_1=MAPS[0]



    def draw_map():
        global screen
        MAP=DATA.MAP_1
        for y in range(1,len(MAP)-1):
           for x in range(1,len(MAP[y])-1):
               index_y = y-1
               index_x = x-1
               pos_x=index_x*60
               pos_y=index_y*60
               if DATA.MAP_1[y][x]!=0:
                   if DATA.MAP_1[y][x]==1:
                       obs_x=DATA.OBS_IMAGES[0]
                   elif DATA.MAP_1[y][x]==2:
                       obs_x=DATA.OBS_IMAGES[1]
                   elif DATA.MAP_1[y][x]==3:
                       obs_x=DATA.OBS_IMAGES[2]
                   elif DATA.MAP_1[y][x]==4:
                       obs_x=DATA.OBS_IMAGES[3]
                   screen.blit(obs_x,(pos_x,pos_y))
                   #print(pos_x,pos_y),测试坐标
                   #创建障碍物

#%%
pg.init()

#游戏舞台
screen=pg.display.set_mode((DATA.SCREEN_WIDTH,DATA.SCREEN_HEIGHT))   
screen.fill(pg.Color("blue"))
#screen.blit(DATA.obs_1,(1140,540))
#游戏标题
pg.display.set_caption(DATA.GAME_TITLE)
#游戏时钟
clock=pg.time.Clock()
clock.tick(DATA.fps)

#渲染背景
BG=pg.image.load("BG.png")
tranBG=pg.transform.scale(BG, (1200,600))
#把缩放后的BG图片放到左上角(0,0)上去
screen.blit(tranBG,(0,0))

#渲染障碍物
DATA.draw_map()

pg.display.update()

while True:
    e=pg.event.poll()
    if e.type==pg.QUIT:
        break
    pg.display.update()

pg.quit() 

'''
建议先确定游戏屏幕大小，再确定格子大小，数组中每一个元素代表一个格子，确定后调整数组大小

BG图片1536*1060，背景和screen大小不一致，先进行压扁平铺到screen上作为底层，之后加的障碍物会覆盖背景

障碍物像素都是60*60可以在属性中查看
'''
