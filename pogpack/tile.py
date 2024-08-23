""" This file contains details for the implementation of the Tile class. """


class Tile:
    def __init__(self, tileType : int, x : int, y : int) -> None:
        self.type = tileType
        self.x = x
        self.y = y

    def setType(self, newType : int):
        self.type = newType
    
    def __repr__(self) -> str:
        if (self.type == 1): # Wall
            return "[=]"
        elif (self.type == 2): # Box
            return "[#]"
        elif (self.type == 3): # Storage
            return "[ ]"
        else: # Blank space
            return " . "
        
if __name__ == "__name__":
    tile1 = Tile(1, 4, 5)
    print(repr(tile1))
