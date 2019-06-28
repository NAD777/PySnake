import pygame

class Part_tail:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = 30
        self.height = 30
    
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
            print(x + self.width * (-pos_x), x)
        self.len += 1

    
    def get_snake(self):
        return [Part_tail(self.x_head, self.y_head, self.cur_pos)] + self.tail


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
        for el in arr:
            pygame.draw.rect(self.screen, (0, 0, 255), (el.get_x(), el.get_y(), el.get_width(), el.get_height()))

    def _keys(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_f]:
            self.snake.add_piece()
    
snk = Snake(100, 100)
brd = Board(snk)
brd.main_action()

