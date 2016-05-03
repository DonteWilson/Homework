import pygame
import Image
import random
from random import*
from Image import *
import time




def main():


	# Create a 2 dimensional array. A two dimensional
	# array is simply a list of lists.
	rows = 10
	cols = 10
	id = 0
	searchSpace = []
	for x in range(cols):
		for y in range(rows):
			print x,",",y, "Index", id
			n = Node(x, y, id)
			id+=1
			
			
			
			cantreach = True if (x >= 5 and x <= 8 and y >= 3 and y >= 8) else False
			#print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
		
			n.setWalk(cantreach)
			
			
			searchSpace.append(n)
			
			
			
			
			
			
			
	MD = Algorithm(searchSpace[0],searchSpace,searchSpace[10], id)
	Node1 = Node (3,5, 35)
	Node2 = Node (5,8, 58)
	Node3 = Node (x-1,y-1,id-1)
	MD.Mdist (Node1, Node2)
	MD.Adj (Node3)
	
	Control = Algorithm(searchSpace[1][1], searchSpace, searchSpace[8][8], id)
	
	for r in searchSpace:
		for n in r:
			rand = randrange(0,5)
			if(rand % 3 == 0) and (Control.currentNode != n) and (Control.Goal != n):
				n.walkable = False
			n.Draw(screen)
			
	Control.Draw(screen)
	
	if(Control.Algorithm()):
		for n in Control.OPEN:
			if n != Control.Goal:
				pygame.draw.rect(screen, [0,255,0,255],[(n.x,n.y),(n.width, n.height)])
		for n in Control.CLOSED:
			if(n != Control.Start) and (n != Control.Goal):
				pygame.draw.rect(screen,[0,0, 255, 255],[(n.x, n.y), (n.width, n.height)])
		for l in Control.SearchSpace:
			for n in l:
				if n.parent != None:
					pygame.Draw.line(screen,[255,0,0,255],n.center,n.parent.center, 5)
					pygame.Draw.circle(screen,[255,0,0,255], n.center, 10, 0)
					
		Control.Path(screen)
	
	else:
		for n in Control.OPEN:
			if n != Control.OPEN:
				if n != Control.Goal:
					pygame.Draw.rect(screen,[0, 255, 0, 255],[(n.x,n.y),(n.width, n.height)])
		
		for n in Control.CLOSED:
			if(n != Control.Start) and (n != Control.Goal):
				pygame.draw.rect(screen, [0,0,255,255],[(n.x, n.y), (n.width, n.height)])
		
		for l in Control.SearchSpace:
			for n in l:
				if n.parent != None:
					pygame.draw.line(screen, [255, 0, 0, 255], n.center, n.parent.center, 5)
					pygame.draw.circle(screen,[255,0,0,255], n.center, 10, 0)
			pygame.draw.line(screen,[100,100,100,255],[0, 0], size, 10)

	# Initialize pygame
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [500, 500]
	screen = pygame.display.set_mode(WINDOW_SIZE)

	# Set title of screen
	pygame.display.set_caption("ADGP120 A*")

	# Loop until the user clicks the close button.
	done = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()



	# -------- Main Program Loop -----------
	while not done:
		for event in pygame.event.get():  # User did something
			if event.type == pygame.QUIT:  # If user clicked close
				done = True	 # Flag that we are done so we exit this loop




		# Set the screen background
		screen.fill((0,0,0))

		for i in searchSpace:
			i.draw(screen, (255,255,255))

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()