import pygame
import random



# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, count=5):
        color = (50, 100, 50)
        color1 = (240,240,240)
        height = 400
        width = 600
        posy = -100
        super().__init__()
        self.polygons = []
        self.SURFACE_COLOR = (20,20,20)
        self.image = pygame.Surface([width, height])
        self.image.fill(self.SURFACE_COLOR)
        self.image.set_colorkey(self.SURFACE_COLOR)
        hh = 40
        mw = 150
        mh = 300
        strColor = 100
        for i in range(count):
            par = self.randomize()
            xx = par[0]
            yy = par[1]
            color = (50, strColor + i*10, 50)
            # self.polyg = pygame.draw.polygon(self.image, color,[(par[0]+i*30,0),(0+i*30,par[1]),(200+i*30,150)], 3)
            obj = self.triangleMountain(100 + xx * i, 75 + yy * i)
            self.polyg = pygame.draw.polygon(self.image, color, ((obj[0][0][0]+ yy, obj[0][0][1] - posy+ yy), (obj[0][1][0]+ yy, obj[0][1][1] - posy+ yy), (obj[0][2][0]+ yy, obj[0][2][1] - posy+ yy)))
            self.polyg1 = pygame.draw.polygon(self.image, color1, ((obj[1][0][0]+ yy, obj[1][0][1] - posy+ yy), (obj[1][1][0]+ yy, obj[1][1][1] - posy+ yy), (obj[1][2][0]+ yy, obj[1][2][1] - posy+ yy)))
            self.polygons.append(self.polyg)
            self.polygons.append(self.polyg1)

        self.rect = self.image.get_rect()

    def randomize(self):
        widd = random.uniform(0,100)
        heii = random.uniform(0,40)
        return [widd, heii]

    def triangleMountain(self, w, h, perc=15):
        points = [[], []]
        proc = perc / 100
        lb = [0, h]
        ct = [w / 2, 0]
        rb = [w, h]
        points[0].append(lb)
        points[0].append(ct)
        points[0].append(rb)
        slb = [w / 2 - (w / 2 * h * proc) / h, 0 + h * proc]
        sct = [w / 2, 0]
        srb = [w / 2 + (w / 2 * h * proc) / h, 0 + h * proc]
        points[1].append(slb)
        points[1].append(sct)
        points[1].append(srb)
        return points