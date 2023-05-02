from algorithm import algorithm
from maze_reader import maze_reader #do testów

## @brief Class containing right hand algorithm 
#

class right_hand(algorithm):

    ## @brief Constructor to initialize maze
    #
    # @param maze is a 2d list representing the layout of the walls in the maze from maze_reader
    def __init__(self, maze):
        self.maze = maze #przekazanie labiryntu z maze_reader
        self.path = [[0 for _ in range(16)] for _ in range(16)] # zainicjalizowanie listy dwuwymiarowej path zerami


    def right_hand_algorithm(self, position, end_position):
        front = self.NORTH
        right = self.EAST
        left = self.WEST
        back = self.SOUTH
        direction = right
        column = position[0]    # obecne położenie
        row = position[1]
        self.path[column][row] = 1     # wpisanie 1 do listy tam, gdzie znalazł się robot
        while position != end_position:   # dopóki robot nie dotrze do końca ścieżki
            if not self.maze[column][row] & right: #jeśli nie ma prawej ściany
                direction = right
            elif not self.maze[column][row] & front:  #jest prawa ściana, ale nie ma przedniej
                direction = front
            elif not self.maze[column][row] & left:  #są prawa i przednia, ale nie ma lewej ściany
                direction = left     
            elif not self.maze[column][row] & back: #są ściany prawa, przednia, lewa, ale nie ma tylnej
                direction = back
            
            if direction == self.NORTH:
                row += 1
                front = self.NORTH
                right = self.EAST
                left = self.WEST
                back = self.SOUTH
            if direction == self.EAST:
                column += 1
                right = self.SOUTH
                front = self.EAST
                left = self.NORTH
                back = self.WEST
            if direction == self.SOUTH:
                row -= 1
                front = self.SOUTH
                right = self.WEST
                left = self.EAST
                back = self.NORTH
            if direction == self.WEST:
                column -= 1
                front = self.WEST
                right = self.NORTH
                left = self.SOUTH
                back = self.EAST
            position = [column, row]
            self.path[column][row] = 1
            print("position: ", position)
        return self.path
    


    def solve(self) -> list:
        column = 0
        row = 0
        position = [column, row]    # pole startowe [0,0]
        end_position = self.find_finish()   #pole końcowe
        self.right_hand_algorithm(position, end_position)   # wywołanie algorytmu prawej ręki
        for i in range(15,-1,-1):     # wypisanie wyznaczonej sciezki
            for j in range(16):
                print(self.path[j][i], end=" ")
            print("\n")

        return self.path
        




maze = maze_reader()
rh = right_hand(maze.read_maze("mazes/maze_cut"))   #maze_cut da sie rozwiazac prawa reka
rh.solve()