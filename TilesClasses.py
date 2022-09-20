import copy
import os
import sys
import pygame
import random
from ErrorClasses import *


def load_image(name, colorkey=None):
    if name == '':
        return ''
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def gen_several_tiles(obj: object, amount: int):
    return [copy.copy(obj) for _ in range(amount)]


gst = gen_several_tiles


class Tile(pygame.sprite.Sprite):
    def __init__(self, img=''):
        pygame.sprite.Sprite.__init__(self)
        if img != '':
            self.image = pygame.transform.scale(load_image(img), (76, 76))
        else:
            self.image = pygame.Surface((76, 76))
            self.image.fill(pygame.color.Color(0, 255, 0))
        self.rect = self.image.get_rect()
        self.people = []
        self.money = 0


class TileWithASign(Tile):
    def __init__(self, sign: str, img=''):
        super().__init__(img)
        self.sign = sign

    def __repr__(self):
        return self.sign


class Sea(TileWithASign):
    def __init__(self):
        super(Sea, self).__init__(sign='Sea')


class UTile(TileWithASign):
    def __init__(self, tile: TileWithASign):
        self.tile = tile
        super().__init__('U(' + self.tile.sign + ')', img='unknown.png')

    def get_tile(self):
        return self.tile


class TileWithSkins(TileWithASign):
    def _check_if_skin(self, skin: int, int1: int, int2: int):
        if skin not in range(int1, int2 + 1):
            raise TileSkinNotExist

    def __init__(self, skin: int, int1: int, int2: int, sign: str, imgs=[]):
        self._check_if_skin(skin, int1, int2)
        self.skin = skin
        super().__init__(sign, imgs[skin - 1])


class Opushka(TileWithSkins):
    def __init__(self, skin: int):
        super().__init__(skin, 1, 4, 'O', imgs=['opushka.png', 'opushka2.png', 'opushka3.png', 'opushka4.png'])


class Arrow(TileWithASign):
    def __init__(self, side: int, int1: int, sign: str, img=''):
        if side not in range(1, int1 + 1):
            raise TileSideNotExist
        self.side = side
        super().__init__('A' + sign)
        if img != '':
            self.image = pygame.transform.scale(load_image(img), (76, 76))
            self.image = pygame.transform.rotate(self.image, (side - 1) * 90)
        else:
            self.image = pygame.Surface((76, 76))
            self.image.fill(pygame.color.Color(0, 255, 0))
        self.rect = self.image.get_rect()

    def get_side(self):
        return self.side


class Arrow1S(Arrow):
    def __init__(self, side):
        super().__init__(side, 4, '1S', 'a1s.png')


class Arrow1D(Arrow):
    def __init__(self, side):
        super().__init__(side, 4, '1D', 'a1d.png')


class Arrow2D(Arrow):
    def __init__(self, side):
        super().__init__(side, 4, '2D', 'a2d.png')


class Arrow2S(Arrow):
    def __init__(self, side):
        super().__init__(side, 4, '2S', 'a2s.png')


class Arrow3(Arrow):
    def __init__(self, side):
        super().__init__(side, 4, '3', 'a3.png')


class Arrow4D(Arrow):
    def __init__(self, side):
        super().__init__(side, 1, '4D', 'a4d.png')


class Arrow4S(Arrow):
    def __init__(self, side):
        super().__init__(side, 1, '4S', 'a4s.png')


class Horse(TileWithASign):
    def __init__(self):
        super().__init__('H', 'horse.png')


class StepTile(TileWithASign):
    def __init__(self, steps: int):
        self.steps = steps
        super().__init__('S' + str(steps))
        '''if steps not in range(1, int1 + 1):
            raise TileStepsNotExist'''

    def get_steps(self):
        return self.steps


class Steps2(StepTile):
    def __init__(self):
        super().__init__(2)


class Steps3(StepTile):
    def __init__(self):
        super().__init__(3)


class Steps4(StepTile):
    def __init__(self):
        super().__init__(4)


class Steps5(StepTile):
    def __init__(self):
        super().__init__(5)


class Ice(TileWithASign):
    def __init__(self):
        super().__init__('I')


class Trap(TileWithASign):
    def __init__(self):
        super().__init__('T')


class Crocodile(TileWithASign):
    def __init__(self):
        super().__init__('C')


class Cannibal(TileWithASign):
    def __init__(self):
        super().__init__('Ca')


class ProtectedTile(TileWithASign):
    def __init__(self, sign):
        super().__init__(sign)


class Fortress(ProtectedTile):
    def __init__(self):
        super(Fortress, self).__init__('F')


class Reviver(ProtectedTile):
    def __init__(self):
        super(Reviver, self).__init__('R')


class Gold(TileWithASign):
    def __init__(self, sign, amount: int):
        super().__init__(sign)
        self.amount = amount


class Chest(Gold):
    def __init__(self, amount: int):
        if amount not in range(1, 6):
            raise TileMoneyNotExist
        super().__init__('GC' + str(amount), amount)


class Ingot(Gold):
    def __init__(self):
        super().__init__('GI', 3)


class Plane(TileWithASign):
    def __init__(self):
        super(Plane, self).__init__('P')


class Karamba(TileWithASign):
    def __init__(self):
        super(Karamba, self).__init__('K')


class AirBalloon(TileWithASign):
    def __init__(self):
        super(AirBalloon, self).__init__('AB')


class Cannon(TileWithASign):
    def __init__(self, side: int):
        super(Cannon, self).__init__('Cn')
        if side not in range(1, 5):
            raise TileSideNotExist
        self.side = side


class Beacon(TileWithASign):
    def __init__(self):
        super(Beacon, self).__init__('B')


class TileWithRecruit(TileWithASign):
    def __init__(self, sign):
        super(TileWithRecruit, self).__init__(sign)
        self.empty = False

    def recruit(self):
        self.empty = True


class BenGannTile(TileWithRecruit):
    def __init__(self):
        super(BenGannTile, self).__init__('BG')


class MissionerTile(TileWithRecruit):
    def __init__(self):
        super(MissionerTile, self).__init__('M')


class FridayTile(TileWithRecruit):
    def __init__(self):
        super(FridayTile, self).__init__('Fr')


class Bottle(TileWithASign):
    def __init__(self, amount: int):
        super(Bottle, self).__init__('Bo' + str(amount))
        if amount not in range(1, 4):
            raise TileBottleNotExist
        self.amount = amount


class Bottle1(Bottle):
    def __init__(self):
        super().__init__(1)


class Bottle2(Bottle):
    def __init__(self):
        super().__init__(2)


class Bottle3(Bottle):
    def __init__(self):
        super().__init__(3)


class Cave(TileWithASign):
    def __init__(self):
        super().__init__('Cv')
        self.works = False


class Skip(TileWithASign):
    def __init__(self):
        super().__init__('Sk')


class Earthquake(TileWithASign):
    def __init__(self):
        super().__init__('E')


class Jungle(ProtectedTile):
    def __init__(self):
        super().__init__('J')


class Hihihi(TileWithASign):
    def __init__(self):
        super().__init__('Hi')


def make_possible_tiles(mode=0):
    if mode == 0:
        possible_tiles = gst(Opushka(1), 5) + gst(Opushka(2), 4) + gst(Opushka(3), 5) + gst(Opushka(4), 4) + [
            Arrow1S(random.randrange(1, 5)), Arrow1S(random.randrange(1, 5)), Arrow1S(random.randrange(1, 5))] + \
                         [Arrow1D(random.randrange(1, 5)), Arrow1D(random.randrange(1, 5)),
                          Arrow1D(random.randrange(1, 5))] + [
                             Arrow2S(random.randrange(1, 3)), Arrow2S(random.randrange(1, 3)),
                             Arrow2S(random.randrange(1, 3))] + [
                             Arrow2D(random.randrange(1, 3)), Arrow2D(random.randrange(1, 3)),
                             Arrow2D(random.randrange(1, 3))] + [
                             Arrow3(random.randrange(1, 5)), Arrow3(random.randrange(1, 5)),
                             Arrow3(random.randrange(1, 5))] + gst(Arrow4D(1), 3) + gst(Arrow4S(1), 3) + gst(Horse(),
                                                                                                             2) + \
                         gst(Steps2(), 5) + gst(Steps3(), 4) + gst(Steps4(), 2) + [Steps5()] + gst(Ice(), 6) + \
                         gst(Trap(), 3) + gst(Crocodile(), 4) + [Cannibal()] + gst(Fortress(), 2) + [Reviver()] + \
                         gst(Chest(1), 5) + gst(Chest(2), 5) + gst(Chest(3), 3) + gst(Chest(4), 2) + [Chest(5)] + [
                             Ingot()] + \
                         [Plane()] + [Karamba()] + gst(AirBalloon(), 2) + \
                         [Cannon(random.randrange(1, 5)), Cannon(random.randrange(1, 5))] + [Beacon()] + [
                             BenGannTile()] + [
                             MissionerTile()] + [FridayTile()] + gst(Bottle1(), 3) + gst(Bottle2(), 2) + [Bottle3()] + \
                         gst(Cave(), 4) + gst(Skip(), 4) + [Earthquake()] + gst(Jungle(), 3) + gst(Hihihi(), 2)
        random.shuffle(possible_tiles)
        return possible_tiles

