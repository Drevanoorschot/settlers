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


class DockTypes(Enum):
    UNIVERSAL = 0
    GRAIN = 1
    WOOD = 2
    WOOL = 3
    ORE = 4
    BRICK = 5

board_representation = """
          oxo          
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