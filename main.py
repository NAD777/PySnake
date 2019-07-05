import pygame

class Part_tail:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = 30
        self.height = 30
    
    def set_x(self, x): 
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_pos(self, pos):
        self.pos = pos

    def get_pos(self):
        return self.pos

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def __str__(self):
        return f'x: {self.x}, y:{self.y}'
    

class Snake:
    def __init__(self, x, y):
        self.poses = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.len = 0
        self.cur_pos = 0
        self.x_head = x
        self.y_head = y
        self.width = 30
        self.height = 30
        self.speed = 10
        self.tail = []
    
    def add_piece(self):
        if self.len == 0:
            pos_x, pos_y = self.poses[self.cur_pos]
            self.tail.append(Part_tail(self.x_head + self.width * (-pos_x), self.y_head + self.width * (-pos_y), self.cur_pos))
        else:
            last_p = self.tail[-1]
            x, y = last_p.get_x(), last_p.get_y()
            pos_x, pos_y = self.poses[last_p.get_pos()]
            self.tail.append(Part_tail(x + self.width * (-pos_x), y + self.width * (-pos_y), last_p.get_pos()))
            
        self.len += 1
    
    def get_snake(self):
        return [Part_tail(self.x_head, self.y_head, self.cur_pos)] + self.tail

    def rot_left(self):
        self.cur_pos = self.cur_pos - 1 if self.cur_pos - 1 != -1 else 3

    def rot_right(self):
        self.cur_pos = self.cur_pos + 1 if self.cur_pos + 1 != 4 else 0

    def next(self):
        last_x, last_y, last_pos = self.x_head, self.y_head, self.cur_pos
        # print(self.x_head, self.y_head)
        self.x_head = self.x_head + self.poses[self.cur_pos][0] * self.width
        self.y_head = self.y_head + self.poses[self.cur_pos][1] * self.height
        # print(self.x_head, self.y_head)
    
        if self.len != 0:
            
            for i in range(self.len): 
                last_x1 = self.tail[i].get_x()
                last_y1 = self.tail[i].get_y()
                last_pos1 = self.tail[i].get_pos()
                self.tail[i].set_x(last_x)
                self.tail[i].set_y(last_y)
                self.tail[i].set_pos(last_pos)
                last_x, last_y, last_pos = last_x1, last_y1, last_pos1
            
    
    def print_tail(self):
        # print(self.get_snake())
        for el in self.get_snake():
            print(el)

class Board:
    def __init__(self, snake):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        self.fill_brd()
        self.snake = snake
    
    def main_action(self):
        while True:
            self._keys()
            self.fill_brd()
            self.draw_snake()
            pygame.display.update()
    
    def fill_brd(self):
        self.screen.fill((255,255,255))

    def is_alive(self):
        pass

    def draw_snake(self):
        arr = self.snake.get_snake()
        pygame.draw.rect(self.screen, (255, 165, 0), (arr[0].get_x(), arr[0].get_y(), arr[0].get_width(), arr[0].get_height()))
        for el in arr[1:]:
            pygame.draw.rect(self.screen, (0, 0, 255), (el.get_x(), el.get_y(), el.get_width(), el.get_height()))


    def _keys(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.snake.rot_left()
                if event.key == pygame.K_d:
                    self.snake.rot_right()
                if event.key == pygame.K_f:
                    self.snake.add_piece()
                if event.key == pygame.K_m:
                    self.snake.next()
                if event.key == pygame.K_l:
                    print(self.snake.len)
                if event.key == pygame.K_p:
                    self.snake.print_tail()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        # if keys[pygame.K_f]:
        #     self.snake.add_piece()
        # if keys[pygame.K_m]:
        
    

snk = Snake(100, 100)
brd = Board(snk)
brd.main_action()

