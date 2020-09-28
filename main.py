class Game():

  def __init__(self):
    self.array = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
          ]

  def printBoard(self):
    for i in self.array:
      print(i)
    print("\n")

  def isEmpety(self,x,y):
      if self.array[x][y] == 0:
          return True
      else:
          return False

  def getEmptySpots(self):
    self.spots = []
    for y in range(0, len(self.array)):
      self.lines = []
      for x in range(0,len(self.array)):
        if self.isEmpety(x,y):
          self.spots.append([x,y])
    return self.spots

  def generateRandom(self):
      from random import choices
      population = [2, 4]
      weights = [0.9, 0.1]
      result = choices(population, weights)
      return result[0]

  def addRandom(self):
    from random import randrange
    freeSpots = self.getEmptySpots();
    randomSpot = randrange(0,len(freeSpots))
    randomSpot = freeSpots[randomSpot]
    x,y = randomSpot[0],randomSpot[1]
    self.array[x][y] = self.generateRandom()

  def stack(self):
    newMatrix = [[0]*4 for _ in range(4)]
    for y in range(4):
      fillPositions = 0
      for x in range(4):
        if self.array[y][x] != 0:
          newMatrix[y][fillPositions] = self.array[y][x]
          fillPositions += 1
    self.array = newMatrix

  def combine(self):
    for y in range(4):
      for x in range(3):
        if self.array[y][x] != 0 and self.array[y][x] == self.array[y][x+1]:
          self.array[y][x] *= 2
          self.array[y][x+1] = 0
  

if __name__ == "__main__":
  teste = Game()
  count = 0
  if (count <= 1):
    teste.addRandom()
    count += 1
  teste.addRandom()
  teste.addRandom()
  teste.printBoard()

  teste.stack()
  teste.printBoard()

  teste.combine()
  teste.printBoard()

  teste.stack()
  teste.printBoard()
  