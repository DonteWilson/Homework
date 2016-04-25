import pygame as gfx
import math
class Node:
	def __init__(self, x, y):
		self.parent = None		
		self.color = (255,255,255)
		self.width = 20
		self.height = 20
		self.margin = 5
		self.left = (self.margin + self.width) *  x + self.margin
		self.top = (self.margin + self.height) *  y + self.margin
		self.walkable = True
		self.pos = (x, self.height - y)
		self.neighbor = None
		self.data = None
		self.next = None
		self.f = None
		self.g = None
		self.h = None
	
	def Run(self):
		i = 0			
			for adj in current.adjacents:
				if adj.walkable and adj not in closed:
					if adj not in open:
						open.append(adj)
						yield adj
						adj.parent = current						
						adj.g = 10 if i < 4 else 14
						
					else:
						move = 10 if i < 4 else 14
						movecost = move + current.g
						if movecost < adj.g: 
							adj.parent = current						
							adj.g = movecost
						yield adj.parent
				i+=1
		
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
class Algorithm:
	def __init__(self,SearchSpace,Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		self.Start = Start
		self.Goal = Goal
		self.SearchSpace = SearchSpace
		self.currentNode = Start
		print self.currentNode.pos[0],",",self.currentNode.pos[1]
	#sets class definition to find the lowest F	
	def LowestF(self, Nodes):
		lowestF = -1
		LFNode = None
		for node in Nodes:
			if(node.f > lowestF):
				lowestF = node.f
				LFNode = node
		return LFNode
	#sets class defintion to start the program
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
	#sets class definition to the list of nodes
	def Nlist(self, Nodes):
		nList = Nodes.sort(key = lambda n: n.f)
		print(nList)
	
	def AdjList(self, Nodes):
		for n in self. SearchSpace
		
	
	def Mdist(self, Node1, Node2):
		Xpos = abs(Node1.pos[0]-Node2.pos[0])
		Ypos = abs(Node1.pos[1]-Node2.pos[1])
		print Xpos,",",Ypos
		return Xpos, Ypos
	
	
	
	
		
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
		
	
	
	

	
	