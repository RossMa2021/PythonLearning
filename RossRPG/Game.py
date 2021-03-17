import sys
import pygame
from pygame.locals import*
from PicSplit import Sprite     # 图片分割
from GameMap import GameMap     # 地图控制
from Action import Player       # 角色动态

# 具体的游戏业务类
class Game:
    def __init__(self, title, width, height, fps=60):
        """
        初始化,构造函数，为类里的成员变量们附值
        :param title: 游戏窗口的标题
        :param width: 游戏窗口的宽度
        :param height: 游戏窗口的高度
        :param fps: 游戏每秒刷新次数
        """
        self.title = title
        self.width = width
        self.height = height
        self.screen_surf = None
        self.fps = fps
        self.__init_pygame()
        self.__init_game()
        self.update()

    # 较为通用,有别于 init game的比较具体的用法
    def __init_pygame(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen_surf = pygame.display.set_mode([self.width, self.height])       # 初始化屏幕窗体
        self.clock = pygame.time.Clock()

    # 更偏向业务
    def __init_game(self):
        self.hero = pygame.image.load('./img/character/Jieni.png').convert_alpha()
        self.map_bottom = pygame.image.load('./img/map/0.png').convert_alpha()   #背景
        self.map_top = pygame.image.load('./img/map/0_top.png').convert_alpha()  #前景
        # 一般来说，前景图和背景图大小一样。所以map w h 可以分别取
        self.game_map = GameMap(self.map_bottom, self.map_top, 0, 0)
        self.game_map.load_walk_file('./img/map/0.map')
        self.role = Player(self.game_map)  # 初始化角色

    def update(self):
        while True:
            self.clock.tick(self.fps)
            # TODO:逻辑更新
            self.event_handler()
            # TODO:画面更新
            # 绘制背景
            self.game_map.draw_bottom(self.screen_surf)
            # 绘制人物固定位置
            # Sprite.drawAbs(self.screen_surf, self.hero, 100, 100, 3, 4, 42, 42)
            # Sprite.drawAbs(self.screen_surf, self.hero, 210, 120, 3, 4, 42, 42)
            # Sprite.drawAbs(self.screen_surf, self.hero, 300, 100, 3, 4, 42, 42)
            # 绘制人物动态位置
            self.game_map.draw_grid(self.screen_surf)
            role_rect = self.role.pic.get_rect()
            self.game_map.roll(self.role.pos[0], self.role.pos[1])
            self.screen_surf.blit(pygame.transform.smoothscale(self.role.pic, (int(role_rect[2]) * 1, int(role_rect[3]) * 1)),
                        (self.role.pos[0], self.role.pos[1]))
            # 绘制前景
            self.game_map.draw_top(self.screen_surf)

            self.role.move()  # 任务角色移动 通过键盘

            pygame.display.update()


    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
