import sys,os
import pygame
import Display
from Display import Node


class Control(object):
    def __init__(self):
        self.Screen = pygame.display.get_surface()
        self.done = False
        self.Clock = pygame.time.Clock()
        self.fps = 60
        self.State = Display.Display()
    def event_loop(self):
        for event in pygame.event.get():
            self.keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
                self.done = True
            if self.State.mode != "RUN":
                self.State.get_event(event)
    def game_loop(self):
        while not self.done:
            self.event_loop()
            self.State.update(self.Screen)
            self.Clock.tick_busy_loop(self.fps)
            pygame.display.flip()

###
def main():

	EmptyRoom = []
	for x in range(21):
		for y in range(13):
			n = Node(x, y)
			
			
			
			cantreach = True if (x >= 4 and x <= 6 and y >= 4 and y >= 3) else False
			print("x =:{mx} y=: {my} | pos =: {position}".format(mx = x, my = y, position = n.pos))
			
		
			n.setWalk(cantreach)
			
			
			EmptyRoom.append(n)
			
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	pygame.init()
	pygame.display.set_caption("ADGP120")
	pygame.display.set_mode((500,500))
	RunIt = Control()
	RunIt.game_loop()
	pygame.quit();sys.exit()

####
if __name__ == "__main__":
    main()