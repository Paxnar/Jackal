from ErrorClasses import *


class Tile:
    pass

class TileWithASign(Tile):
    def __init__(self, sign: str):
        self.sign = sign

    def __repr__(self):
        return self.sign


class UTile(TileWithASign):
    def __init__(self, tile: Tile):
        self.tile = tile
        super().__init__('U')

    def get_tile(self):
        return self.tile


class TileWithSkins(TileWithASign):
    def _check_if_skin(self, skin: int, int1: int, int2: int):
        if skin not in range(int1, int2 + 1):
            raise TileSkinNotExist

    def __init__(self, skin: int, int1: int, int2: int, sign: str):
        super().__init__(sign)
        self._check_if_skin(skin, int1, int2)
        self.skin = skin


class Opushka(TileWithSkins):
    def __init__(self, skin: int):
        super().__init__(skin, 1, 4, 'O')


class Arrow(Tile):
    def __init__(self, side: int, int1: int):
        if side not in range(1, int1 + 1):
            raise TileSideNotExist
        self.side = side

    def get_side(self):
        return self.side


class Arrow1S(Arrow, TileWithASign):
    def __init__(self, side):
        Arrow.__init__(self, side, 4)
        super().__init__("A1S")


class Arrow1D(Arrow, TileWithASign):
    def __init__(self, side):
        Arrow.__init__(self, side, 4)
        super().__init__('A1D')


class Arrow2D(Arrow, TileWithASign):
    def __init__(self, side):
        Arrow.__init__(self, side, 4)
        super().__init__('A2D')


class Arrow2S(Arrow, TileWithASign):
    def __init__(self, side):
        Arrow.__init__(self, side, 4)
        super().__init__('A2S')


class Arrow3(Arrow, TileWithASign):
    def __init__(self, side):
        Arrow.__init__(self, side, 1)
        super().__init__('A3')

