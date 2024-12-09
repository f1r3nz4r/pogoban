""" This contains details for the implementation of the map class """
from .tile import Tile

class Map:
    def __init__(self) -> None:
        pass
    
    def loadMapFromFile(self, mapName : str):
        with open(f"Maps/{mapName}.pogM") as file:
            data = file.readlines()
        row = int(data[0].rstrip().split(" ")[1])
        col = int(data[0].rstrip().split(" ")[2])
        types = [line.rstrip().split(" ") for line in data[1::]]
        self.initMap(row, col, types)
        
    def initMap(self, rows : int, cols : int, types : list[list[str]]) -> None:
        self.map = [[Tile(0, x, y) for x in range(cols)] for y in range(rows)]
        for y, line in enumerate(types):
            for x, type in enumerate(line):
                self.map[y][x].setType(int(type))
        self.ROWS = rows
        self.COLS = cols

    def __repr__(self) -> str:
        returnStr = "\n+" + "-" * (3 * self.COLS) + "+\n"
        for row in self.map:
            returnStr += "|"
            for tile in row:
                returnStr += f"{tile}"
            returnStr += "|\n"
        returnStr += "+" + "-" * (3 * self.COLS) + "+\n"
        return returnStr
