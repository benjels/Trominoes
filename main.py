

#KEY FOR UNDERSTANDING BOARD PRINTOUT:
#'o': initial deficient tile
#'X': blank tile
#'1': tile that belongs to tromino that would fit snugly in top left corner
#'2': tile that belongs to tromino that would fit snugly in top right corner
#'3': tile that belongs to tromino that would fit snugly in bottom left corner
#'4': tile that belongs to tromino that would fit snugly in bottom right corner


class Board:

	def __init__(self, x, y, size): #takes an x and y for the OG deficiency and the size which is the width and the height.
		self.size = size
		self.board2d = []

		#fill every index with 'X' which represents a blank space apart from the one index that gets a 'o' which represents the initial deficiency.
		for eachOuter in range(0,size):
			row = []
			for eachInner in range(0,size):
				if(eachOuter == x and eachInner == y):
					print("just put the init deficiency at:" + str(x) + " " + str(y))
					row.append('o')
				else:
					row.append('X')
			self.board2d.append(row)
		self.draw()


	def recursiveSolve(self, x, y, regionSize): #takes the top left (inclusive) coordinate of which region it should solve as well as the size of the region to solve
		#create some variables for keeping track of the 4 sub-regions of this region

		halfSize = int(regionSize/2)
		
		topLeftX = x
		topLeftY = y

		topRightX = x + (halfSize)
		topRightY = y 

		bottomLeftX = x 
		bottomLeftY = y + halfSize

		bottomRightX = x + (halfSize)
		bottomRightY = y + (halfSize)

		#check which of the 4 sub regions the deficiency of this region is contained in. Give a deficiency to the the 3 non-deficient sub regions by placing a tromino that spans all 3 of them, then make a recursive call on each of our (now deficient) 4 sub regions.
		#NOTE: if we are at the base case (size =2), then we don't need to make recursive calls. 

		if self.findDeficiency(topLeftX, topLeftY, halfSize):

			assert self.board2d[x + halfSize][y + (halfSize)-1] == 'X'
			self.board2d[x + halfSize][y + (halfSize)-1] = '4'
			assert self.board2d[x + halfSize][y + halfSize] == 'X'
			self.board2d[x + halfSize][y + halfSize] = '4'
			assert self.board2d[x + halfSize-1][y + halfSize] == 'X'
			self.board2d[x + halfSize-1][y + halfSize] = '4'
			print("deficiency of my region is in top left. my region's info: " + str(x) + " " + str(y) + " size: " + str(halfSize) + ". I'm putting down 4s")
			self.draw();

			if regionSize != 2:
				self.recursiveSolve(topLeftX, topLeftY, halfSize)
				self.recursiveSolve(topRightX, topRightY, halfSize)
				self.recursiveSolve(bottomRightX, bottomRightY, halfSize)
				self.recursiveSolve(bottomLeftX, bottomLeftY, halfSize)

		elif self.findDeficiency(topRightX, topRightY, halfSize):

			assert self.board2d[x + halfSize -1][y + halfSize-1] == 'X'
			self.board2d[x + halfSize -1][y + halfSize-1] = '3'
			assert self.board2d[x + halfSize][y + halfSize] == 'X'
			self.board2d[x + halfSize][y + halfSize] = '3'
			assert self.board2d[x + halfSize - 1][y + halfSize] == 'X'
			self.board2d[x + halfSize - 1][y + halfSize] = '3'
			print("deficiency of my region is in top right. my region's info: " + str(x) + " " + str(y) + " size: " + str(halfSize) + ". I'm putting down 3s")
			self.draw();

			if regionSize != 2:
				self.recursiveSolve(topRightX, topRightY, halfSize)
				self.recursiveSolve(topLeftX, topLeftY, halfSize)
				self.recursiveSolve(bottomRightX, bottomRightY, halfSize)
				self.recursiveSolve(bottomLeftX, bottomLeftY, halfSize)

		elif self.findDeficiency(bottomLeftX, bottomLeftY, halfSize):

			assert self.board2d[x + halfSize][y + halfSize] == 'X'
			self.board2d[x + halfSize][y + halfSize] = '2'
			assert self.board2d[x + halfSize][y + halfSize - 1] == 'X'
			self.board2d[x + halfSize][y + halfSize - 1] = '2'
			assert self.board2d[x + halfSize - 1][y + halfSize - 1] == 'X'
			self.board2d[x + halfSize - 1][y + halfSize - 1] = '2'
			print("deficiency of my region is in bottom left. my region's info: " + str(x) + " " + str(y) + " size: " + str(halfSize) + ". I'm putting down 2s")
			self.draw();

			if regionSize != 2:
				self.recursiveSolve(bottomLeftX, bottomLeftY, halfSize)
				self.recursiveSolve(topRightX, topRightY, halfSize)
				self.recursiveSolve(bottomRightX, bottomRightY, halfSize)
				self.recursiveSolve(topLeftX, topLeftY, halfSize)

		else: # in the case that the deficiency is in the bottom right

			assert self.board2d[x + halfSize][y + halfSize - 1] == 'X'
			self.board2d[x + halfSize][y + halfSize - 1] = '1'
			assert self.board2d[x + halfSize - 1][y + halfSize] == 'X'
			self.board2d[x + halfSize - 1][y + halfSize] = '1'
			assert self.board2d[x + halfSize - 1][y + halfSize - 1] == 'X'
			self.board2d[x + halfSize - 1][y + halfSize - 1] = '1'
			print("deficiency of my region is in bottom right. my region's info: " + str(x) + " " + str(y) + " size: " + str(halfSize) + ". I'm putting down 1s")
			self.draw();

			if regionSize != 2:
				self.recursiveSolve(bottomRightX, bottomRightY, halfSize)
				self.recursiveSolve(topRightX, topRightY, halfSize)
				self.recursiveSolve(bottomLeftX, bottomLeftY, halfSize)
				self.recursiveSolve(topLeftX, topLeftY, halfSize)



	def findDeficiency(self, x, y, size):#takes a region and checks whether there is any deficiency (i.e. a non blank tile) in it
		for eachOuter in range(x, x+size):
			for eachInner in range(y, y+size):
				if self.board2d[eachOuter][eachInner] != 'X':
					#print("we located the deficiency at the following coordinate: " + "x:" + str(eachOuter) + "y:" + str(eachInner))
					return True
		return False


	def draw(self): #print a visual representation of the current state of the board to the console
		for eachOuter in range(0, self.size):
			for eachInner in range(0, self.size):
				print(self.board2d[eachInner][eachOuter] + " ", end = "")
			print("")
		print("\n\n")



	


#runs the algorithm over a size*size boards of the provided size where each of these board has the deficiency initialised in a different location.
def fullTest():
	for i in range(0,BOARD_SIZE):
		for j in range(0,BOARD_SIZE):
			print("now we are going to check with the deficiency at: " + str(i) + " " + str(j))
			board = Board(i, j, BOARD_SIZE)
			board.recursiveSolve(0, 0, BOARD_SIZE)


BOARD_SIZE = 8		

def main():
	#run the test
	fullTest()








if __name__ == "__main__":
	main()