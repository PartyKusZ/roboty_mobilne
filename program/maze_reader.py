from data import data

class maze_reader(data):

    def read_maze(self, maze_name: str) -> list:
        with open(maze_name,"r") as maze_file:  #otwarcie pliku 
           for line in maze_file:               #pętla for, która w tej lini jednocześnie iteruje i pobiera całą linie z pliku aż do napotkania EOF
               line = line.replace("\n","")     # usunięcie znaku nowej lini 
               line = line.split()              # podzielenie lini tekstu na poszczególne stringi względem spacji
               line = [int(x,16) for x in line] # zamiana poszczególnych stringów na liczby hex 
               self.maze.append(line)           # dodanie do listy labirynu liczb hex

        return self.maze                        # zwraca 2 wymiarową liste hex
    

