# Main driver code for the game.
import pogpack as pp


def main():
    print("Welcome to POGOBAN!!")
    map = pp.Map()
    map.loadMapFromFile("map1")
    print(map)
    map.loadMapFromFile("map2")
    print(map)

if __name__ == "__main__":
    main()
    