import pygame
from pygame.locals import *
import time
#Node class Object 
class Node(object):
	def __init__(self, x, y):
		self.parent = None	
		self.color = (255,187,31)
		self.width = 20
		self.height = 20
		self.space = 10 
		self.x = x
		self.y = y
		self.margin = 5
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2))
		self.walkable = True
		self.pos = (x,y)
		self.f = None
		self.g = None
		self.h = 0
		
		
	#defines draw
	def Draw(self, screen):
	#sets walkable squares to yellow and unwalkable squares to a brownish color.
		clr = self.color if (self.walkable) else (141,103,18)
		
		
		#draws to the screen
		pygame.draw.rect(screen, clr, [(self.x , self.y), (self.width, self.height)])
	def setWalk(self, walkable):
		self.walkable = walkable
	#gets the f value
	def getF(self):
		if self.g == None:
			self.g = 0
		return self.h + self.g
	#sets the h value
	def setH(self, value):
		self.h = value
		self.f = self.getF()
		return self.h
	#sets the g value
	def setG(self, value):
		self.g = value
		self.f = self.getF()
		return self.g
#class that stores all algorithm data
class Algorithm(object):
	def __init__(self,Start,SearchSpace, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.PATH = []
		self.start = Start
		self.goal = Goal
		self.ss = SearchSpace
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
		#Sets starting node to a light purple color
		pygame.draw.rect(screen,[0,142,7,255],[(self.start.x, self.start.y),(self.start.width, self.start.height)])
		#Sets goal node to a light blue color
		pygame.draw.rect(screen,[150, 100, 255, 255],[(self.goal.x, self.goal.y),(self.goal.width, self.goal.height)])
		
	#sets class definition to the list of nodes
	def Nlist(self, Nodes):
		nList = Nodes.sort(key = lambda n: n.f)
		print(nList)
		
	#Finds Lowest F node
	def LowestF(self, nodes):
		lowestF = None
		for n in nodes:
			if lowestF == None:
				lowestF = n
			
			elif(n.getF() < lowestF.getF()):
				lowestF = n 
		
		#returns the lowest F value
		return lowestF
	
		
	#Finds the manhattan distance
	def Mdist(self, Node1, Node2):
		Xpos = abs(Node1.pos[0]-Node2.pos[0])
		Ypos = abs(Node1.pos[1]-Node2.pos[1])
		print Xpos,",",Ypos
		return Xpos, Ypos
	
	
	#Finds the Adjacent nodes surroundings
	def Adj(self):
		#list of all adjacent nodes
		adjacents = [] 
		#search for the current node.
		for i, nodes in enumerate(self.ss):
			for j, node in enumerate(nodes):
				if node == self.currentNode:
					pos = (j, i)
					
		#gets all adjacent nodes 
		for i, nodes in enumerate(self.ss):
			if(pos[1] - 1 <= i <= pos[1] + 1):
				for j, node in enumerate(nodes):
				#if adjacent is walkable and not current node
					if (pos[0] - 1 <= j <= pos[0] + 1) and (self.ss[i][j].walkable == True) and (self.ss[i][j] != self.currentNode):
					#adds onto the adjacent list
						adjacents.append(self.ss[i][j])
		#returns the adjacent values.
		return adjacents
		#rows = 10
		#cols = 10
		#Left = currentNode.id - rows
		#Right = currentNode.id + rows
		#Bot = currentNode.id + 1
		#Top = currentNode.id -1
		#Down = currentNode.id + rows + 1
		#Tright = Right - 1
		#Tleft = Left - 1
		#Bright = Right + 1
		#Bleft = Left + 1
		#adjs = [Left, Right, Bot, Top, Down, Tright, Tleft, Bright, Bleft]
		
		#if currentNode.id % rows == 0:
		#	Left = 0
		#	Tleft = 0
		#	Bleft = 0
		#if currentNode.id % rows == 9: 
		#	Right = 0
		#	Tright = 0
		#	Bright = 0
		#print "Top: ", Top,"| Bot: ", Bot,"| Left: ", Left,"| Right", Right
		#print "TLeft: ", Tleft,"| Bleft ", Bleft,"| Tright: ", Tright, "| Bright", Bright
	
	#Calculates the H value
	def H(self, node1, node2):
		cost = 0
		for x, nodes in  enumerate(self.ss):
			for y, node in enumerate(nodes):
				if self.ss[x][y] == node1:
					n1xy = [x,y]
				
				if self.ss[x][y] == node2:
					n2xy = [x,y]
		
		dist = [abs(n1xy[0] - n2xy[0]), abs(n1xy[1] - n2xy[1])]
		
		while (dist != [0,0]):
			if dist[0] > 0:
				cost += 10
				dist[0] -= 1
				
			if dist[1] >0:
				cost += 10
				dist[1] -= 1
		
		#returns the cost
		return cost
		
	#Calculates the G Value
	def G(self, node1, node2):
		cost = 0
		for x, nodes in enumerate(self.ss):
			for y, node in enumerate(nodes):
				if self.ss[x][y] == node1:
					n1xy = [x,y]
				
				if self.ss[x][y] == node2:
					n2xy = [x,y]
					
		dist = [abs(n1xy[0] - n2xy[0]), abs(n1xy[1] - n2xy[1])]
		
		if(dist[0] > 0) and (dist[1] > 0):
			cost = 14
		
		else:
			cost = 10
		
		return cost
		
	def Start(self):
		#sets the current node to the starting node.
		self.currentNode = self.start
		#Add to the Open List
		self.OPEN.append(self.currentNode)
		aj = self.Adj()
		for n in aj:
			#If node walkable is true do this and looks at adjacent nodes
			if(n.walkable == True):
				#Set parent to current node
				n.parent = self.currentNode
				#Sets the H 
				n.setH(self.H(n, self.goal))
				#Sets the G
				n.setG(self.G(n, self.currentNode))
				self.OPEN.append(n)
		
		self.OPEN.remove(self.currentNode)
		self.CLOSED.append(self.currentNode)
		
	
	#definition for the A star algorithm 
	def Star(self):
		self.Start()
		while(len(self.OPEN) > 0):
			self.currentNode = self.LowestF(self.OPEN)
			self.OPEN.remove(self.currentNode)
			self.CLOSED.append(self.currentNode)
			adj = self.Adj()
			
			if(self.currentNode == self.goal) or (self.goal in self.CLOSED):
				return True
			
			for n in adj:
				if(n not in self.CLOSED):
					if(n not in self.OPEN):
						#sets the parent node
						n.parent = self.currentNode
						n.setH(self.H(n, self.goal))
						n.setG(self.G(n, self.currentNode))
						self.OPEN.append(n)
					else:
						movecost = self.currentNode.g + self.G(self.currentNode, n)
						if(movecost < n.g):
						#sets the parent node
							n.parent = self.currentNode
						#Sets the G value
							n.setG(self.G(self.currentNode,n))
							#sorts the list
							self.OPEN.sort(key = lambda x : x.f)
			#If OPEN is empty return False
			return False
	
	def DrawP(self, screen, node1, node2):
		pygame.draw.circle(screen,[255, 252, 195, 157], node1.center, 10)
		pygame.draw.line(screen,[255, 255, 177, 125], node1.center, node2.center, 5)
	
	def Path(self, screen):
		cur = self.goal
		while(cur.parent != None):
			#draws line to the parent node.
			pygame.draw.line(screen, [100, 255, 137, 0], cur.center, cur.parent.center, 5)
			cur = cur.parent
			