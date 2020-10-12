class Island():
    def __init__(self, n, prey_count=0, predator_count=0):
        print(n, prey_count, predator_count)
        self.grid_size = n
        self.grid = []
        for i in range(n):
            row = [0]*n # row is list of n 0's
            self.grid.append(row)
        self.init_animals(prey_count, predator_count)

    def animal(self, x, y):
        if 0<=x <self.grid_size and 0 <= y <self.grid_size:
            return self.grid[x][y]
        else:
            return -1 #outside grid boundary

    def init_animals(self,prey_count, predator_count):
        ''' Put some initial animals on the island
        '''
        count = 0
        # while loop continues until prey_count unoccupied positions are found
        while count < prey_count:
            x = random.randint(0,self.grid_size-1)
            y = random.randint(0,self.grid_size-1)
            if not self.animal(x,y):
                new_prey=Prey(island=self,x=x,y=y)
                count += 1
                self.register(new_prey)
        count = 0
        # same while loop but for predator_count
        while count < predator_count:
            x = random.randint(0,self.grid_size-1)
            y = random.randint(0,self.grid_size-1)
            if not self.animal(x,y):
                new_predator=Predator(island=self,x=x,y=y)
                count += 1
                self.register(new_predator)

    def size(self):
        return self.grid_size

    def register(self, animal):
        x = animal.x
        y = animal.y
        self.grid[x][y] = animal

    def __str__(self):
        s =''
        for j in range(self.grid_size-1, -1, -1): #print row size -1 first
            for i in range(self.grid_size): #each new row starts at 0
                if not self.grid[i][j]: #if empty print a period
                    s+= "{:<2s}".format('.' + " ")
                else:
                    s+= "{:<2s}".format((str(self.grid[i][j])) + " ")
            s+="\n"
        return s

    def remove(self,x,y):
        self.grid[x][y] = 0

class Animal(object): #this should be helpful for associating friends with users, e.g. user is island, friend is name, then see register in island
    def __init__(self, island, x=0, y=0, s="A"):
        self.island = island
        self.name = s
        self.x = x
        self.y = y

    def __str__(self):
        return self.name

    def move(self):
        offset = [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)] 
        for i in range(len(offset)):
            x = self.x + offset[i][0]
            y = self.y + offset[i][1]
            if self.island.animal(x,y) == 0:
                self.island.remove(self) # note that this island method is available to an animal object, and by inheritance prey & predator
                self.x = x
                self.y = y
                self.island.register(self)
                break



class Prey(Animal):
    def __init__(self, island, x=0, y=0,s="O"): 
        Animal.__init__(self, island, x,y,s) 

class Predator(Animal):
    def __init__(self, island, x=0, y=0,s="O"):
        Animal.__init__(self, island, x,y,s) 


"""
>>> royale = Island(10)
10 0 0
>>> animal1 = Animal(island=royale, x=4, y=8,s='a1')
>>> animale = Animal(island=royale, x=6, y=6,s='a2')
>>> royale.register(animal1)
>>> royale.register(animale)
>>> print(royale)
. . . . . . . . . . 
. . . . a1 . . . . . 
. . . . . . . . . . 
. . . . . . a2 . . . 
. . . . . . . . . . [omitted rest]
"""