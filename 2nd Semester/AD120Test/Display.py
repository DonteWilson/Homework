import pygame 
import Astar

class Display(object):
    def __init__(self):
        self.animate = False
        self.options = ("F","G","H")
        self.piece_type = "F"
        self.cell_size = (20,20)
        self.image = self.make_background()
        self.reset()
        self.font = pygame.font.SysFont("arial",13)
        self.rendered = {}

    def make_background(self):
        #Creates a Grid 
        image = pygame.Surface((500,500)).convert()
        image.set_colorkey((0,0,255))
        image.fill((0,0,255),(20,20,400,240))
        for i in range(21):
            image.fill((224,102,255),(20+20*i,20,2,242))
        for i in range(13):
            image.fill((224,102,255),(20,20+20*i,400,2))
        return image

    def reset(self,full=True):
        """Allows both completely resetting the grid or resetting to an
        unsolved state."""
        if full:
            self.mode = "START"
            self.start_cell   = None
            self.goal_cell    = None
            self.barriers  = self.setup_barriers()
            self.Solver = None
            self.time_end = self.time_start = 0.0
            self.solution = []
        else:
            self.Solver = None
            self.mode = "BARRIER"

    def setup_barriers(self):
        """Initialize the boundary borders. Borders must be two cells thick to
        prevent knight pieces from leaving the grid."""
        self.add_barrier = False
        self.del_barrier = False
        barriers = set()
        for i in range(-1,23):
            for j in (-1,0,13,14):
                barriers.add((i,j))
        for j in range(-1,15):
            for i in (-1,0,21,22):
                barriers.add((i,j))
        return barriers

    def get_target(self):
        #Gets Mouse position on grid.
        self.mouse  = pygame.mouse.get_pos()
        self.target = (self.mouse[0]//self.cell_size[0],self.mouse[1]//self.cell_size[1])

    def get_event(self,event):
        """Receives events from the control class and passes them along as appropriate."""
        self.get_target()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hit = pygame.mouse.get_pressed()
            if hit[0]:
                self.left_button_clicked()
            elif hit[2]:
                self.right_button_clicked()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.add_barrier = False
            self.del_barrier = False
        elif event.type == pygame.KEYDOWN:
            self.hotkeys(event)

    def left_button_clicked(self):
        """Left mouse button functionality for get_event method."""
        if pygame.Rect(20,20,400,240).collidepoint(self.mouse):
            if self.mode == "START":
                if self.target != self.goal_cell and self.target not in self.barriers:
                    self.start_cell = self.target
                    self.mode = ("BARRIER" if self.goal_cell else "GOAL")
            elif self.mode == "GOAL":
                if self.target != self.start_cell and self.target not in self.barriers:
                    self.goal_cell = self.target
                    self.mode = "BARRIER"
            elif self.mode == "BARRIER":
                self.add_barrier = True
        elif self.rendered["MOVE"][1].collidepoint(self.mouse):
            self.toggle_piece()
        elif self.rendered["ANIM"][1].collidepoint(self.mouse):
            self.toggle_animate()
        elif self.mode == "BARRIER" and self.rendered["BARRIER"][1].collidepoint(self.mouse):
            self.mode = "RUN"
        elif self.mode in ("SOLVED","FAILED"):
            if self.rendered["ENTER"][1].collidepoint(self.mouse):
                self.reset()
            elif self.rendered["RESET"][1].collidepoint(self.mouse):
                self.reset(False)

    def right_button_clicked(self):
        #Runs this if the right mouse button is clicked.
        if self.mode != "RUN":
            if self.target == self.start_cell:
                self.start_cell = None
                self.mode = "START"
            elif self.target == self.goal_cell:
                self.goal_cell = None
                self.mode = ("GOAL" if self.start_cell else "START")
            elif self.mode == "BARRIER":
                self.del_barrier = True

    def hotkeys(self,event):
        #defines keyboard functionality
        if event.key in (pygame.K_1,pygame.K_2,pygame.K_3):
            self.toggle_piece(int(event.unicode)-1)
        elif event.key == pygame.K_d:
            self.toggle_animate()
        elif self.mode == "BARRIER" and event.key == pygame.K_SPACE:
            self.mode = "RUN"
        elif self.mode in ("SOLVED","FAILED"):
             if event.key == pygame.K_RETURN:
                self.reset()
             elif event.key == pygame.K_i:
                self.reset(False)

    def toggle_animate(self):
        """Turns animation mode on and off."""
        if self.mode != "RUN":
            self.animate = not self.animate
            self.render_text("ANIM")
    def toggle_piece(self,ind=None):
        """Change to next piece or to a specific piece if ind is supplied."""
        if self.mode != "RUN":
            if not ind:
                ind = (self.options.index(self.piece_type)+1)%len(self.options)
            self.piece_type = self.options[ind]
            self.render_text("MOVE")

    def add_barriers(self):
       #Creates barriers based on user decision
        if self.mode == "BARRIER":
            self.get_target()
            if pygame.Rect(20,20,400,240).collidepoint(self.mouse):
                if self.target not in (self.start_cell,self.goal_cell):
                    if self.add_barrier:
                        self.barriers.add(self.target)
                    elif self.del_barrier:
                        self.barriers.discard(self.target)

    def update(self,Surf):
        #Updates GUI as the soultion is being solved.
        self.add_barriers()
        if self.mode == "RUN":
            if not self.Solver:
                self.time_start = pygame.time.get_ticks()
                self.Solver = Astar.Star(self.start_cell,self.goal_cell,self.piece_type,self.barriers)
            if self.animate:
                self.Solver.evaluate()
            else:
                while not self.Solver.solution:
                    self.Solver.evaluate()
            if self.Solver.solution:
                self.found_solution()
        if self.mode != "RUN" or self.animate:
            self.draw(Surf)

    def found_solution(self):
        """Sets appropriate mode when solution is found (or failed)."""
        self.time_end = pygame.time.get_ticks()
        if self.Solver.solution == "NO SOLUTION":
            self.mode = "FAILED"
        else:
            self.solution = self.Solver.solution
            self.mode = "SOLVED"

    def fill_cell(self,cell,color,Surf):
        """Fills a single cell given coordinates, color, and a target Surface."""
        loc = cell[0]*self.cell_size[0],cell[1]*self.cell_size[1]
        Surf.fill(color,(loc,self.cell_size))
        return pygame.Rect(loc,self.cell_size)
    def center_number(self,cent,string,color,Surf):
        """Used for centering numbers on cells."""
        rend = self.font.render(string,1,color)
        rect = pygame.Rect(rend.get_rect(center=cent))
        rect.move_ip(1,1)
        Surf.blit(rend,rect)

    def draw(self,Surf):
        """Calls draw functions in the appropraite order."""
        Surf.fill(0)
        self.draw_solve(Surf)
        self.draw_start_end_walls(Surf)
        Surf.blit(self.image,(0,0))
		
    def draw_solve(self,Surf):
        """Draws while solving (if animate is on) and once solved."""
        if self.mode in ("RUN","SOLVED","FAILED"):
            for cell in self.Solver.closed_set:
                self.fill_cell(cell,(255,0,255),Surf)
            if self.mode == "SOLVED":
                for i,cell in enumerate(self.solution):
                    cent = self.fill_cell(cell,(0,255,0),Surf).center
                    self.center_number(cent,str(len(self.solution)-i),(0,0,0),Surf)
    def draw_start_end_walls(self,Surf):
        """Draw endpoints and barriers."""
        if self.start_cell:
            self.fill_cell(self.start_cell,(255,255,0),Surf)
        if self.goal_cell:
            cent = self.fill_cell(self.goal_cell,(0,0,255),Surf).center
            if self.mode == "SOLVED":
                self.center_number(cent,str(len(self.solution)),(255,255,255),Surf)
        for cell in self.barriers:
            self.fill_cell(cell,(255,255,255),Surf)
 