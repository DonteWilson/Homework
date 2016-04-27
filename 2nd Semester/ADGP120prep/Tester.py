import pygame
from Image import *




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
			
			
			
			
			
			
			
	MD = Algorithm(searchSpace, searchSpace[0],searchSpace[10])
	Node1 = Node (3,5, 35)
	Node2 = Node (5,8, 58)
	Node3 = Node (x-1,y-1,id-1)
	MD.Mdist (Node1, Node2)
	MD.Adj (Node3)

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