from enum import Enum

numbers = {
    0: 5,
    1: 2,
    2: 6,
    3: 3,
    4: 8,
    5: 10,
    6: 9,
    7: 12,
    8: 11,
    9: 4,
    10: 8,
    11: 10,
    12: 9,
    13: 4,
    14: 5,
    15: 6,
    16: 3,
    17: 11
}
mapping_sequence = [0, 1, 3, 8, 13, 16, 18, 17, 15, 10, 5, 2, 4, 6, 11, 14, 12, 7, 9]


class TileType(Enum):
    DESERT = 0
    GRAIN = 1
    WOOD = 2
    WOOL = 3
    ORE = 4
    BRICK = 5


tile_set = {
    TileType.DESERT: 1,
    TileType.GRAIN: 4,
    TileType.WOOD: 4,
    TileType.WOOL: 4,
    TileType.ORE: 3,
    TileType.BRICK: 3
}


class DockType(Enum):
    UNIVERSAL = 0
    GRAIN = 1
    WOOD = 2
    WOOL = 3
    ORE = 4
    BRICK = 5

    def __str__(self):
        if self == DockType.UNIVERSAL:
            return "universal"
        if self == DockType.GRAIN:
            return "grain"
        if self == DockType.BRICK:
            return "brick"
        if self == DockType.WOOD:
            return "wood"
        if self == DockType.WOOL:
            return "wool"
        if self == DockType.ORE:
            return "ore"



dock_set = {
    DockType.UNIVERSAL: 4,
    DockType.GRAIN: 1,
    DockType.WOOD: 1,
    DockType.WOOL: 1,
    DockType.ORE: 1,
    DockType.BRICK: 1

}

dock_locations = [[[(0, 10), (0, 12)], 0],
                  [[(2, 6), (4, 4)], 60],
                  [[(2, 16), (4, 18)], 300],
                  [[(8, 2), (10, 0)], 60],
                  [[(8, 20), (10, 22)], 300],
                  [[(14, 0), (16, 2)], 120],
                  [[(14, 22), (16, 20)], 240],
                  [[(18, 6), (18, 8)], 180],
                  [[(18, 14), (18, 16)], 180]
                  ]

board_representation = """          oxo          
         x   x         
      oxo  0  oxo      
     x   x   x   x     
  oxo  0  oxo  0  oxo  
 x   x   x   x   x   x 
o  0  oxo  0  oxo  0  o
 x   x   x   x   x   x 
  oxo  0  oxo  0  oxo  
 x   x   x   x   x   x 
o  0  oxo  0  oxo  0  o
 x   x   x   x   x   x 
  oxo  0  oxo  0  oxo  
 x   x   x   x   x   x 
o  0  oxo  0  oxo  0  o
 x   x   x   x   x   x 
  oxo  0  oxo  0  oxo  
     x   x   x   x     
      oxo  0  oxo       
         x   x          
          oxo           
"""
