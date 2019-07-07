#birth commit :)
import pygame
from random import randint
class Part_tail:
    def __init__(self, x, y, pos):
        self.x = x
        self.y = y
        self.pos = pos
        self.width = 10
        self.height = 10
        self.speed = 10
    
    def set_x(self, x): 
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def get_speed(self):
        return self.speed

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
    
class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
    
    def check(self, x, y):
        if self.x == x and self.y == y:
            return True
        else:
            return False
    
    def __call__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width
        self.y =  y

class Snake:
    def __init__(self, x, y):
        self.poses = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        self.cur_pos = 1
        self.x_head = x
        self.y_head = y
        self.width = 10
        self.height = 10
        self.speed = 10
        self.tail = [Part_tail(self.x_head, self.y_head, self.cur_pos)]
    
    def add_piece(self):
        pos_x, pos_y = self.poses[self.cur_pos]
        self.x_head = self.x_head + self.speed * pos_x
        self.y_head = self.y_head + self.speed * pos_y
        self.tail.insert(0, Part_tail(self.x_head, self.y_head, self.cur_pos))
    
    def move(self):
        self.add_piece()
        self.tail.pop()

    def get_snake(self):
        return self.tail

    def rot_left(self):
        self.cur_pos = self.cur_pos - 1 if self.cur_pos - 1 != -1 else 3

    def rot_right(self):
        self.cur_pos = self.cur_pos + 1 if self.cur_pos + 1 != 4 else 0  
    
    def print_tail(self):
        # print(self.get_snake())
        for el in self.get_snake():
            print(el)
WIDTH = 720
HEIGHT = 460
class Board:
    def __init__(self, snake):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.fill_brd()
        self.clock = pygame.time.Clock()
        self.snake = snake
        self.score = 0
        self.fruit = Fruit(randint(0, WIDTH - 1) // 10 * 10, randint(0, HEIGHT - 1) // 10 * 10)
        self.fps_controller = pygame.time.Clock()

    def main_action(self):
        while True:
            self._keys()
            self.fill_brd()
            self.draw_fruit()
            self.draw_snake()
            self.pudge()
            # self.snake.next()
            
            # pygame.display.update()
            pygame.display.flip()
            self.fps_controller.tick(40)

    def pudge(self):
        head = self.snake.get_snake()[0]
        if self.fruit.check(head.get_x(), head.get_y()):
            self.fruit(randint(0, WIDTH - 1) // 10 * 10, randint(0, HEIGHT - 1) // 10 * 10)
            self.score += 1
            self.snake.add_piece()
        else:
            self.snake.move()

    def draw_fruit(self):
        pygame.draw.rect(self.screen, (255, 0, 0), (self.fruit.get_x(), self.fruit.get_y(), self.fruit.get_width(), self.fruit.get_height()))
    
    def fill_brd(self):
        self.screen.fill((255,255,255))

    def is_alive(self):
        pass

    def draw_snake(self):
        arr = self.snake.get_snake()
        # pygame.draw.rect(self.screen, (255, 165, 0), (arr[0].get_x(), arr[0].get_y(), arr[0].get_width(), arr[0].get_height()))
        for el in arr:
            pygame.draw.rect(self.screen, (0, 165, 0), (el.get_x(), el.get_y(), el.get_width(), el.get_height()))

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
                if event.key == pygame.K_l:
                    print(self.snake.len)
                if event.key == pygame.K_p:
                    self.snake.print_tail()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_f]:
            self.snake.add_piece()
        # if keys[pygame.K_f]:
        #     self.snake.add_piece()
        # if keys[pygame.K_m]:
        
    

snk = Snake(0, 0)
brd = Board(snk)
brd.main_action()

