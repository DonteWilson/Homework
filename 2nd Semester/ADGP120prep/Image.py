import pygame as gfx
import math
class Node:
	def __init__(self, x, y, id):
		self.parent = None	
		self.id = id
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x,y)
		self.neighbor = None
		self.data = None
		self.next = None
		self.f = None
		self.g = None
		self.h = None
		
		
	#defines draw
	def draw(self, screen, color):
		margin = self.margin
		
		#sets the color to red and else if green
		color = (0, 255, 0) if (self.walkable) else (255,0,0)
		
		
		#draws to the screen
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
	def setWalk(self, walkable):
		self.walkable = walkable
	#gets the f value
	def getF(self):
		return self.h + self.g
	#sets the h value
	def setH(self, val):
		self.h = val
	#sets the g value
	def setG(self, val):
		self.g = val
#class that stores all algorithm data
class Algorithm(object):
	def __init__(self,SearchSpace,Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.PATH = []
		self.Start = Start
		self.Goal = Goal
		self.SearchSpace = SearchSpace
		self.currentNode = self.Start
		print self.currentNode.pos[0],",",self.currentNode.pos[1]
	
	#def Reset(self):
		#for n in self.searchSpace:
			#node = self.searchSpace[n]
			#node.parent = None
			#node.g = 0
			#node.f = 0
			#node.h = 0
		
		#for n in self.searchSpace:
			#node = self.searchSpace[n]
			#self.Adj(node)
			#distx = int(math.fabs(self.Goal.index[0] - node.index[0]))
			#distx *= 10
			#disty = int(math.fabs(self.Goal.index[1] - node.index[1]))
			#disty *= 10
			#node.h = distx + disty

	#sets class defintion to start the program
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
	#sets class definition to the list of nodes
	def Nlist(self, Nodes):
		nList = Nodes.sort(key = lambda n: n.f)
		print(nList)
	
		
	
	def Mdist(self, Node1, Node2):
		Xpos = abs(Node1.pos[0]-Node2.pos[0])
		Ypos = abs(Node1.pos[1]-Node2.pos[1])
		print Xpos,",",Ypos
		return Xpos, Ypos
		
	
	def Adj(self, currentNode):
		rows = 10
		cols = 10
		Left = currentNode.id - rows
		Right = currentNode.id + rows
		Bot = currentNode.id + 1
		Top = currentNode.id -1
		Down = currentNode.id + rows + 1
		Tright = Right - 1
		Tleft = Left - 1
		Bright = Right + 1
		Bleft = Left + 1
		adjs = [Left, Right, Bot, Top, Down, Tright, Tleft, Bright, Bleft]
		
		if currentNode.id % rows == 0:
			Left = 0
			Tleft = 0
			Bleft = 0
		if currentNode.id % rows == 9:
			Right = 0
			Tright = 0
			Bright = 0
		print "Top: ", Top,"| Bot: ", Bot,"| Left: ", Left,"| Right", Right
		print "TLeft: ", Tleft,"| Bleft ", Bleft,"| Tright: ", Tright, "| Bright", Bright
			
		
	
	
	
	
		
class List:
	def __init__(self):
		self.head = None
	
	def addNode(self, data):
		curr = self.head
		if curr is None:
			n = Node()
			n.data = data
			self.head = next
			return
			
		if curr.data > data:
			n = Node()
			n.data = data
			n.next = curr
			self.head = n
			return
		
		while curr.next is not None:
			if curr.next.data > data:
				break
			curr = curr.next
		n = Node()
		n.data = data
		n.next = curr.next
		curr.next = n
		return
		
	def __str__(self):
		data = []
		curr = self.head
		while curr is not None:
			data.append(curr.data)
			curr = curr.next
		return "[%s]" %(','.join(str(i) for i in data))
		
	def __repr__(self):
		return self.__str__()
		
	
	
	

	
	