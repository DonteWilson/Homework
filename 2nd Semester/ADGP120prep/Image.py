import pygame as gfx
from pygame.locals import *
import time
class Node(object):
	def __init__(self, x, y, id):
		self.parent = None	
		self.id = id
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.x = x
		self.y = y
		self.margin = 5
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2))
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x,y)
		self.f = None
		self.g = None
		self.h = 0
		
		
	#defines draw
	def draw(self, screen, color):
		margin = self.margin
		
		#sets the color to red and else if green
		color = (255, 250, 250) if (self.walkable) else (255,0,0)
		
		
		#draws to the screen
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
	def setWalk(self, walkable):
		self.walkable = walkable
	#gets the f value
	def getF(self):
		if self.g == None:
			self.g = 0
		return self.h + self.g
	#sets the h value
	def setH(self, val):
		self.h = val
	#sets the g value
	def setG(self, val):
		self.g = val
#class that stores all algorithm data
class Algorithm(object):
	def __init__(self,Start,SearchSpace, Goal, id):
		self.OPEN = []
		self.CLOSED = []
		self.PATH = []
		self.Start = Start
		self.Goal = Goal
		self.SearchSpace = SearchSpace
		self.currentNode = self.Start
		#print self.currentNode.pos[0],",",self.currentNode.pos[1]
	
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
	
	def Draw(self, screen):
		pygame.draw.rect(screen,[0,150,198,220],[(self.Start.x, self.Start.y),(self.Start.width, self.Start.height)])
		pygame.draw.rect(screen,[0,255,255,255],[(self.Goal.x, self.Goal.y),(self.Goal.width, self.Goal.height)])
		
	#sets class definition to the list of nodes
	def Nlist(self, Nodes):
		nList = Nodes.sort(key = lambda n: n.f)
		print(nList)
		
	#Finds Lowest F node
	def LowestF(self, nodes):
		lowestF = None
		for n in nodes:
			if lowestF == None:
				lowestF = nList
			
			elif(n.getF() < lowestF.getF()):
				lowestF = n 
		
		return lowestF
	
		
	#Finds the manhattan distance
	def Mdist(self, Node1, Node2):
		Xpos = abs(Node1.pos[0]-Node2.pos[0])
		Ypos = abs(Node1.pos[1]-Node2.pos[1])
		print Xpos,",",Ypos
		return Xpos, Ypos
	
	def Start(self):
		self.currentNode = self.start
		
		self.OPEN.append(self.currentNode)
		aj = self.Adj()
		for n in aj:
			if(n.walkable == True):
				n.parent = self.currentNode
				n.setH(self.H(n, self.Goal))
				n.setG(self.G(n, self.currentNode))
				self.OPEN.append(n)
		
		self.OPEN.remove(self.currentNode)
		self.CLOSED.append(self.currentNode)
		
	#Finds the Adjacent nodes surroundings
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
	
	def H(self, node1, node2):
		cost = 0
		for x, nodes in  enumerate(self.SearchSpace):
			for y, node in enumerate(nodes):
				if self.SearchSpace[x][y] == node1:
					n1xy = [x,y]
				
				if self.SearchSpace[x][y] == node2:
					n2xy = [x,y]
		
		dist = [abs(n1xy[0] - n2xy[0]), abs(n1xy[1] - n2xy[1])]
		
		while (dist != [0,0]):
			if dist[0] > 0:
				cost += 10
				dist[0] -= 1
				
			if dist[1] >0:
				cost += 10
				dist[1] -= 1
		
		return cost
	
	def G(self, node1, node2):
		cost = 0
		for x, nodes in enumerate(self.SearchSpace):
			for y, node in enumerate(nodes):
				if self.SearchSpace[x][y] == node1:
					n1xy = [x,y]
				
				if self.SearchSpace[x][y] == node2:
					n2xy = [x,y]
					
		dist = [abs(n1xy[0] - n2xy[0]), abs(n1xy[1] - n2xy[1])]
		
		if(dist[0] > 0) and (dist[1] > 0):
			cost = 14
		
		else:
			cost = 10
		
		return cost
	
	
	def Star(self):
		self.Start()
		while(len(self.OPEN) > 0):
			self.currentNode = self.LowestF(self.OPEN)
			self.OPEN.remove(self.currentNode)
			self.CLOSED.append(self.currentNode)
			adj = self.Adj()
			
			if(self.currentNode == self.Goal) or (self.Goal in self.CLOSED):
				return True
			
			for n in adj:
				if(n not in self.CLOSED):
					if(n not in self.OPEN):
						n.parent = self.currentNode
						n.setH(self.H(n, self.Goal))
						n.setG(self.G(n, self.currentNode))
						self.OPEN.append(n)
					else:
						movecost = self.currentNode.g + self.G(self.currentNode, n)
						if(movecost < n.g):
							n.parent = self.currentNode
							n.setG(self.G(self.currentNode,n))
							self.OPEN.sort(key = lambda x : x.f)
			
			return False
	
	def DrawP(self, screen, node1, node2):
		pygame.draw.circle(screen,[255, 0, 0, 255], node1.center, 10)
		pygame.draw.line(screen,[255, 0, 0, 255], node1.center, node2.center, 5)
	
	def Path(self, screen):
		cur = self.Goal
		while(cur.parent != None):
			pygame.draw.line(screen, [100, 100, 100, 255], cur.center, cur.parent.center, 5)
			cur = cur.parent
			