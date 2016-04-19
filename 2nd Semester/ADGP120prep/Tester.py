import pygame
from Image import *



def main():


	# Create a 2 dimensional array. A two dimensional
	# array is simply a list of lists.
	EmptyRoom = []
	for x in range(10):
		for y in range(10):
			n = Node(x, y)
			
			
			
			cantreach = True if (x >= 4 and x <= 6 and y >= 4 and y >= 3) else False
			print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
		
			n.setWalk(cantreach)
			
			
			EmptyRoom.append(n)
			
			
			
			
			
			
			
		

	# Initialize pygame
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	WINDOW_SIZE = [500, 500]
	screen = pygame.display.set_mode(WINDOW_SIZE)

	# Set title of screen
	pygame.display.set_caption("Example of Astar")

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

		for i in EmptyRoom:
			i.draw(screen, (255,255,255))

		# Limit to 60 frames per second
		clock.tick(60)

		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()

	# Be IDLE friendly. If you forget this line, the program will 'hang'
	# on exit.
	pygame.quit()

main()