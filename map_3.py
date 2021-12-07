# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:44:13 2021

@author: Neptune
"""

import pygame as pg

           
class DATA:
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
        pg.image.load("./images/grass.gif"),
        pg.image.load("./images/water.gif")
        ]
    
    #obs_1=OBS_IMAGES[0]
    #obs_2=OBS_IMAGES[1]
    #obs_3=OBS_IMAGES[2]
    #obs_4=OBS_IMAGES[3]
    
    #0无 1钢铁 2瓷砖 3草地 4水域                    
    "钢铁无法通过和被子弹击穿 瓷砖被子弹击穿后可通过 草地可以被所有坦克和子弹通过，在草地中敌方看不见 水域坦克永远过不了，子弹可以穿透"
    MAPS=[

        [
           [0,0,1,0,0,0,0,3,0,0,0,3,0,0,0,0,0,1,0,0],
           [0,0,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,0,0],
           [0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,1,0,0],
           [0,1,1,0,0,0,0,0,0,2,0,0,3,3,0,0,0,1,0,0],
           [0,0,1,0,0,1,0,0,2,2,2,0,0,0,3,0,0,1,0,0],
           [4,0,0,0,0,0,0,2,2,2,2,2,0,4,4,4,0,0,3,3],
           [0,0,0,0,0,0,2,0,3,0,0,0,2,0,1,0,2,0,3,3],
           [3,3,0,1,0,2,0,0,0,2,0,0,0,2,0,0,0,0,0,0],
           [0,0,0,0,2,0,0,1,0,0,0,0,0,0,2,0,0,0,0,0],
           [0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0]
        ]
    ]
    
    MAP_1=MAPS[0]             #第一关


    def draw_map():
        global screen
        for y in range(len(DATA.MAP_1)):
           for x in range(len(DATA.MAP_1[y])):
               index_y = y
               index_x = x
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

#DATA.draw_map()
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

#渲染障碍物
#DATA.draw_map()

BG=pg.image.load("BG.jpeg")
tranBG=pg.transform.scale(BG, (60,60))
screen.blit(tranBG,(600,300))
pg.display.flip()

while True:
    e=pg.event.poll()
    if e.type==pg.QUIT:
        break
    pg.display.flip()
  
pg.quit() 
