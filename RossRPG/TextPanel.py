import sys
from pygame.locals import *
import pygame
from pygame.locals import*

white = (255,255,255)
black = (0,0,0)

# 所有的对话 用二维数组的形式存储
textArry = [['这是第一张地图第一个人的第一句话','这是第一张地图第一个人的第二句话','这是第一张地图第一个人的第三句话'],
            ['这是第一张地图第2个人的第一句话','这是第一张地图第2个人的第二句话','这是第一张地图第2个人的第三句话']]

class TextPanel(object):
    def __init__(self, textBottom,arrayNPC):
        self.textBottom = textBottom
        self.font = pygame.font.SysFont('SimHei', 17)
        self.textLoopSeq = 0  # 长对话标识
        self.isShowTextPanel = False # 是否显示的标识
        self.mapSeq = 0 #地图编号
        self.npcSeq = 0 #npc编号
        self.arrayNPC = arrayNPC #npc数组

    def draw_text(self, screen_surf):
        screen_surf.blit(pygame.transform.smoothscale(self.textBottom, (640, 100)), (0, 380))
        screen_surf.blit(self.font.render('故事开始!', True, (0, 0, 0)), (20, 390))

    def draw_textLoop(self,screen_surf):
        screen_surf.blit(pygame.transform.smoothscale(self.textBottom, (640, 100)), (0, 380))
        str = textArry[self.npcSeq][self.textLoopSeq]
        screen_surf.blit(self.font.render(str, True, (0, 0, 0)), (20, 390))

    def draw_NextText(self):
        if self.textLoopSeq + 1 == len(textArry[self.npcSeq]) :
            self.isShowTextPanel = False
            self.textLoopSeq = 0
        else:
            self.textLoopSeq = self.textLoopSeq + 1

    def set_Map_NPC_Seq(self,MapSeq,playerPosX,playerPosY):
        self.mapSeq = MapSeq # 地图编号

        #print(playerPosX,playerPosY)
        for i in range(len(self.arrayNPC)):
            # print("iii",i)
            if abs(playerPosX - self.arrayNPC[i][0]) < 20 and abs(playerPosY - self.arrayNPC[i][1]) < 20:
                self.isShowTextPanel = True
                self.npcSeq = i
                break;
            else:
                self.isShowTextPanel = False