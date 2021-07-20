import pygame

class Array2D:
    """
        说明：
            1.构造方法需要两个参数，即二维数组的宽和高
            2.成员变量w和h是二维数组的宽和高
            3.使用：‘对象[x][y]’可以直接取到相应的值
            4.数组的默认值都是0
    """

    def __init__(self, w, h, default=0):
        self.w = w
        self.h = h
        self.data = []
        self.data = [[default for y in range(h)] for x in range(w)]

    def show_array2d(self):
        for y in range(self.h):
            for x in range(self.w):
                print(self.data[x][y], end=' ')
            print("")

    def __getitem__(self, item):
        return self.data[item]

class GameMap(Array2D):
    """
    游戏地图类
    """

    def __init__(self, bottom, top, x, y):
        """
        将地图划分成w*h个小格子，每个格子32*32像素
        :param bottom: 背景图
        :param top: 前景图
        :param x: 起始位置x
        :param y: 起始位置y
        """
        w = int(bottom.get_width() / 32 ) + 1 #格子数
        h = int(top.get_height() / 32) + 1

        super().__init__(w, h)
        self.bottom = bottom
        self.top = top
        self.x = x
        self.y = y
        # 绝对宽高
        self.width = bottom.get_width()
        self.height= bottom.get_height()
        # NPC坐标数组 后续增加文件导入功能
        self.posNPC = [[380, 310], [600, 120]]

    def draw_bottom(self, screen_surf):
        screen_surf.blit(self.bottom, (self.x, self.y))

    def draw_top(self, screen_surf):
        screen_surf.blit(self.top, (self.x, self.y))

    def draw_grid(self, screen_surf):
        # 画网格
        for x in range(self.w):
            for y in range(self.h):
                if self[x][y] == 0:
                    pygame.draw.rect(screen_surf, (255, 255, 255), (self.x + x * 32, self.y + y * 32, 32, 32), 1)
                else:
                    pygame.draw.rect(screen_surf, (0, 0, 0, 100), (self.x + x * 32 + 1, self.y + y * 32 + 1, 30, 30), 0)

    # 图片滚动
    def roll(self, role_x, role_y, WIN_WIDTH=640, WIN_HEIGHT=480):
        """
        地图滚动
        :param role_x: 角色相对于地图的坐标
        :param role_y:
        """
        # print(role_x, role_y)
        if role_x < WIN_WIDTH / 2:
            self.x = 0
        elif role_x > self.bottom.get_width() - WIN_WIDTH / 2:
            self.x = -(self.bottom.get_width() - WIN_WIDTH)
        else:
            self.x = -(role_x - WIN_WIDTH / 2)

        if role_y < WIN_HEIGHT / 2:
            self.y = 0
        elif role_y > self.bottom.get_height() - WIN_HEIGHT / 2:
            self.y = -(self.bottom.get_height() - WIN_HEIGHT)
        else:
            self.y = -(role_y - WIN_HEIGHT / 2)

    def load_walk_file(self, path):
        # 读取可行走区域文件
        with open(path, 'r') as file:
            for x in range(self.w):
                for y in range(self.h):
                    v = int(file.readline())
                    self[x][y] = v
        #self.show_array2d()