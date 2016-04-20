import pygame as gfx
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
		

	def draw(self, screen, color):
		margin = self.margin
		
		color = (0, 255, 0) if (self.walkable) else (255,0,0)
		
		
		
		gfx.draw.rect(screen, color, (self.left , self.top, self.width, self.height))
	def setWalk(self, walkable):
		self.walkable = walkable
	
	def getF(self):
		return self.h + self.g
		
	def setH(self, val):
		self.h = val
	
	def setG(self, val):
		self.g = val

class Algorithm:
	def __init__(self,SearchSpace,Start, Goal):
		self.OPEN = []
		self.CLOSED = []
		
	def LowestF(self, Nodes):
		lowestF = -1
		LFNode = None
		for node in Nodes:
			if(node.f > lowestF):
				lowestF = node.f
				LFNode = node
		return LFNode
	
	def Run(self):
		self.OPEN.append(Start)
		while not self.OPEN:
			current = self.LowestF(self.OPEN)
	
	def Nlist(self, Nodes):
		nList = Nodes.sort(key = lambda n: n.f)
		print(nList)
	
	def AdjList(self, Nodes):
		print "Stuff"
		
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
		
	
	
	

	
	