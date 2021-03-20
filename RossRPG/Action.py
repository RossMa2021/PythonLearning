import pygame
from pygame.locals import*

class CharWalk:
    """
    人物行走类 char是character的缩写
    """
    DIR_DOWN = 0
    DIR_LEFT = 1
    DIR_RIGHT = 2
    DIR_UP = 3

    def __init__(self, hero_surf, char_id, dir, mx, my):
        """
        :param hero_surf: 精灵图的surface
        :param char_id: 角色id
        :param dir: 角色方向
        :param mx: 角色所在的小格子坐标
        :param my: 角色所在的小格子坐标
        """
        self.hero_surf = hero_surf
        self.char_id = char_id
        self.dir = dir
        self.mx = mx
        self.my = my

        self.is_walking = False  # 角色是否正在移动
        self.frame = 1  # 角色当前帧
        self.x = mx * 32  # 角色相对于地图的坐标
        self.y = my * 32
        # 角色下一步需要去的格子
        self.next_mx = 0
        self.next_my = 0
        # 步长
        self.step = 2  # 每帧移动的像素

    def draw(self, screen_surf, map_x, map_y):
        cell_x = self.char_id % 12 + int(self.frame)
        cell_y = self.char_id // 12 + self.dir
        # Sprite.draw(screen_surf, self.hero_surf, map_x + self.x, map_y + self.y, cell_x, cell_y)

    def drawSplit(self, screen_surf, map_x, map_y):
        cell_x = self.char_id % 12 + int(self.frame)
        cell_y = self.char_id // 12 + self.dir
        # Sprite.draw(screen_surf, self.hero_surf, map_x + self.x, map_y + self.y, cell_x, cell_y)

    def goto(self, x, y):
        """
        :param x: 目标点
        :param y: 目标点
        """
        self.next_mx = x
        self.next_my = y

        # 设置人物面向
        if self.next_mx > self.mx:
            self.dir = CharWalk.DIR_RIGHT
        elif self.next_mx < self.mx:
            self.dir = CharWalk.DIR_LEFT

        if self.next_my > self.my:
            self.dir = CharWalk.DIR_DOWN
        elif self.next_my < self.my:
            self.dir = CharWalk.DIR_UP

        self.is_walking = True

    def move(self):
        if not self.is_walking:
            return
        dest_x = self.next_mx * 32
        dest_y = self.next_my * 32

        # 向目标位置靠近
        if self.x < dest_x:
            self.x += self.step
            if self.x >= dest_x:
                self.x = dest_x
        elif self.x > dest_x:
            self.x -= self.step
            if self.x <= dest_x:
                self.x = dest_x

        if self.y < dest_y:
            self.y += self.step
            if self.y >= dest_y:
                self.y = dest_y
        elif self.y > dest_y:
            self.y -= self.step
            if self.y <= dest_y:
                self.y = dest_y

        # 改变当前帧
        self.frame = (self.frame + 0.1) % 3

        # 角色当前位置
        self.mx = int(self.x / 32)
        self.my = int(self.y / 32)

        # 到达了目标点
        if self.x == dest_x and self.y == dest_y:
            self.frame = 1
            self.is_walking = False

class Player():
    def __init__(self, map2d):
        """
            :param map2d: Array2D类型的寻路数组
        """
        self.map2d = map2d
        # 向下
        self.rd0 = pygame.image.load(r"img\character\0.png").convert_alpha()
        self.rd1 = pygame.image.load(r"img\character\1.png").convert_alpha()
        self.rd2 = pygame.image.load(r"img\character\2.png").convert_alpha()
        self.rd3 = pygame.image.load(r"img\character\3.png").convert_alpha()
        # 向左
        self.rl0 = pygame.image.load(r"img\character\4.png").convert_alpha()
        self.rl1 = pygame.image.load(r"img\character\5.png").convert_alpha()
        self.rl2 = pygame.image.load(r"img\character\6.png").convert_alpha()
        self.rl3 = pygame.image.load(r"img\character\7.png").convert_alpha()
        # 向右
        self.rr0 = pygame.image.load(r"img\character\8.png").convert_alpha()
        self.rr1 = pygame.image.load(r"img\character\9.png").convert_alpha()
        self.rr2 = pygame.image.load(r"img\character\10.png").convert_alpha()
        self.rr3 = pygame.image.load(r"img\character\11.png").convert_alpha()
        # 向上
        self.ru0 = pygame.image.load(r"img\character\12.png").convert_alpha()
        self.ru1 = pygame.image.load(r"img\character\13.png").convert_alpha()
        self.ru2 = pygame.image.load(r"img\character\14.png").convert_alpha()
        self.ru3 = pygame.image.load(r"img\character\15.png").convert_alpha()
        # 站立
        self.sd = pygame.image.load(r"img\character\0.png").convert_alpha()
        self.sr = pygame.image.load(r"img\character\4.png").convert_alpha()
        self.sl = pygame.image.load(r"img\character\8.png").convert_alpha()
        self.su = pygame.image.load(r"img\character\12.png").convert_alpha()
        self.rd=[self.rd0,self.rd1,self.rd2,self.rd3]
        self.ru=[self.ru0,self.ru1,self.ru2,self.ru3]
        self.rr=[self.rr0,self.rr1,self.rr2,self.rr3]
        self.rl=[self.rl0,self.rl1,self.rl2,self.rl3]
        self.pos=[0,300] #初始化人物位置
        self.speed=4 #初始化人物移动速度
        self.pic=self.sd #初始化人物图像
        self.picnum = 0

    def moveControl(self):
        kp=pygame.key.get_pressed()
        # kp 是定时轮询监视全键盘操作的结果，如有按下则会置为1
        # print(kp)
        if kp[K_a] or kp[K_LEFT]: # a 左
            self.picnum+=1
            self.picnum=self.picnum%4
            if self.checkMoveRange(self.pos[0] - self.speed, self.pos[1]) == True:
                self.pos[0]=self.pos[0]-self.speed
            self.pic=self.rl[self.picnum]
        elif kp[K_d] or kp[K_RIGHT]: # d 右
            self.picnum+=1
            self.picnum=self.picnum%4
            if self.checkMoveRange(self.pos[0] + self.speed, self.pos[1]) == True:
                self.pos[0]=self.pos[0]+self.speed
            self.pic=self.rr[self.picnum]
        elif kp[K_s] or kp[K_DOWN]: # s 下
            self.picnum+=1
            self.picnum=self.picnum%4
            if self.checkMoveRange(self.pos[0], self.pos[1]+self.speed) == True:
                self.pos[1]=self.pos[1]+self.speed
            self.pic=self.rd[self.picnum]
        elif kp[K_w] or kp[K_UP]: # w 上
            self.picnum+=1
            self.picnum=self.picnum%4
            if self.checkMoveRange(self.pos[0], self.pos[1]-self.speed) == True:
                self.pos[1]=self.pos[1]-self.speed
            self.pic=self.ru[self.picnum]
        # 如果抬起了键盘，显示站立状态
        keyup =  ""
        for event in pygame.event.get():
            if event.type == KEYUP:
                keyup = event.key
            else:
                keyup = None
        if keyup:
            if keyup==K_a:
                self.picnum=0
                self.pic=self.sl
            if keyup==K_d:
                self.picnum=0
                self.pic=self.sr
            if keyup==K_w:
                self.picnum=0
                self.pic=self.su
            if keyup==K_s:
                self.picnum=0
                self.pic=self.sd


    def checkMoveRange(self, x, y):
        # 需要注意的是, x,y人物图片的左上角, 所以在最后右侧检测时要减去人物图的尺寸
        # 边缘检测
        if x < 0 or y < 0 or x > self.map2d.width - 32 or (y > self.map2d.height - 32):
            return False
        # 转换为格子坐标, 根据角色实际调整
        pX = int(x / 32 + 0.5)
        pY = int(y / 32) + 1
        # 障碍检测
        if self.map2d[pX][pY] == 1:
           return False
        return True
