#Global Sequence Alignment - Dynamic Programming

sequenceX = '-CTCGATCGATCGA' 
sequenceY = '-TCGATTTAGACTA'

#append a gap character to the front

class element:
	def __init__(self, X, Y):
		self.score = None
		self.x = X
		self.y = Y
		self.calc_score()
		self.traceback = [None, None]

	def calc_score(self):
		score = None
		scoreL = None
		scoreU = None
		scoreD = None
		#if Matrix[self.x-1, self.y-1] != None:

Matrix2 = [[range(len(sequenceY))] for x in range(len(sequenceX))]
for x in range(len(sequenceX)-1):
	for y in range(len(sequenceY)-1):
		Matrix2[x][y] = 0





#Matrix[0][0] = []
#Matrix = {}
#Matrix[0,0] = element(0,0)


print ("self.x equals", Matrix[0,0].x)
print ("self.y equals", Matrix[0,0].y)
print ("traceback equals", Matrix[0,0].traceback)
print ("empty element", Matrix[1,1])
print ("string -1 index", sequenceX[-1])







