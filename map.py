# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 17:44:13 2021

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
        
    #障碍物图片
    OBS_IMAGES=[
        pg.image.load("./images/steels.gif"),
        pg.image.load("./images/walls.gif"),
        pg.image.load("./images/grass.gif"),
        pg.image.load("./images/water.gif")
        ]
    
    obs_1=OBS_IMAGES[0]
    obs_2=OBS_IMAGES[1]
    obs_3=OBS_IMAGES[2]
    obs_4=OBS_IMAGES[3]
    
    #0无 1钢铁 2瓷砖 3草地 4水域                    
    "钢铁无法通过和被子弹击穿 瓷砖被子弹击穿后可通过 草地可以被所有坦克和子弹通过，在草地中敌方看不见 水域坦克永远过不了，子弹可以穿透"
    MAPS=[
          #第一关
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
    
    MAP_1=MAPS[0]

#screen=pg.display.set_mode((Resource.SCREEN_WIDTH,Resource.SCREEN_HEIGHT),
                           #Resource.SCREEN_FLAG,Resource.SCREEN_IMG_BIT) 


    def draw_map(self):
        
#screen.flit((x,y))

       for y in Resource.MAP_1:
           for x in y:
               print(MAP_1.index(y),y.index(x))
               index_y = MAP_1.index(y)
               index_x = y.index(x)
               pos_x=index_x*60
               pos_y=index_y*60
               #创建障碍物
               """
               if x==1:  #钢铁
                   screen.blit(image,())
               elif x==2:   #瓷砖
                   obs_x=Resource.OBS_IMAGES[1],
                                       position={'x':pos_x,'y':pos_y})
               elif x==3:   #草地
                   obs_x=Obstacle_Type(Resource.OBS_IMAGES[2],
                                       position={'x':pos_x,'y':pos_y})               
               elif x==4:   #水域
                   obs_x=Obstacle_Type(Resource.OBS_IMAGES[3],
                                       position={'x':pos_x,'y':pos_y})  
                   
       
              

#%% 垃圾测试代码
#img_1 = pg.image.load("BG.jpeg")
#img_2 = pg.image.load("TANK.png")

#screen.blit(img_2, [0, 0])
#screen.blit(img_2, [0, 300])


#%%


        
    pg.display.set_caption(Resource.GAME_TITLE)
    #游戏时钟
    clock=pg.time.Clock()
    


#%%老师源码可用,主程序

pg.init()

#游戏舞台
screen=pg.display.set_mode((Resource.SCREEN_WIDTH,Resource.SCREEN_HEIGHT))   

screen.fill(pg.Color("blue"))
#游戏标题
pg.display.set_caption(Resource.GAME_TITLE)
#游戏时钟
pg.time.Clock.tick(24)

pg.display.flip()

while True:
    e=pg.event.poll()
    if e.type==pg.QUIT:
        break
    
    #调用障碍物工厂时候出BUG还未解决
    #Obstacle_Factory.build_maps()
    pg.display.flip()
    
pg.quit()
"""
