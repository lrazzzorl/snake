game_over, max_x, max_y = False, 28, 28

import time
import keyboard
from random import randint as rnd


class Snake:
    def __init__(self):
        self.body= [(15,15), (15,14), (15,13)]
        self.direct='right'
        self.score=0
        self.time=0.0

    def turn(self, dir):
        #назад повернуть нельзя
        reverse={'up':'down', 'down':'up', 'left':'right', 'right':'left'}
        if reverse[self.direct] != dir:
            self.direct = dir
  
    def growth(self):
        #рост и +1 к счету
        self.body.append(self.tail)
        self.score+=1
        #apple = Food()
            

    def go(self):
        self.tail=self.body[0]
        #двигаем голову
        if  self.direct=='up':
            self.body[0]= self.body[0][0]-1, self.body[0][1]
        elif  self.direct=='down':
            self.body[0]= self.body[0][0]+1, self.body[0][1]
        elif  self.direct=='left':
            self.body[0]= self.body[0][0], self.body[0][1]-1
        elif  self.direct=='right':
            self.body[0]= self.body[0][0], self.body[0][1]+1
        #двигаем тело
        for i in range(1, len(self.body)):
            pos = self.body[i]
            self.body[i] = self.tail
            self.tail = pos


class Food:
    #еда появляется в случайных координатах
    def __init__(self):
        while True:
            coord = rnd(1, max_x-1),  rnd(1, max_y-1)
            if coord not in python.body:
                self.loc = coord
                break

def NewGame():
    global python, apple
    python = Snake()
    apple = Food()

def paint(snake, food):
    #рисуем змею и поле
    for i in range(max_x):
        for j in range(max_y):
            if i == 0 or i == max_x - 1:
                print('=', end=' ')
            elif j == 0 or j == max_y - 1:
                    print('|', end=' ')
            elif (i,j) in snake.body:
                    print('#', end=' ')
            elif (i,j) == food.loc:
                    print('@', end=' ')
            else:
                print(' ', end=' ')
        print('')
    print('time = {}; score = {}; use "wasd" to move.'.format(round(python.time, 1), python.score))


#новая игра
NewGame()

while game_over==False:
    #змея ползет
    python.go()
    paint(python, apple)
    keyboard.add_hotkey('w', lambda: python.turn('up'))
    keyboard.add_hotkey('s', lambda: python.turn('down'))
    keyboard.add_hotkey('a', lambda: python.turn('left'))
    keyboard.add_hotkey('d', lambda: python.turn('right'))


    chech_body = python.body.copy()
    chech_body.pop(0)
    #проверка на яблоко - растем и делаем новое
    if apple.loc in python.body:
        python.growth() 
        apple = Food()
    #проверка на столкновение
    elif python.body[0][0] <= 0 or python.body[0][0] >= max_x or python.body[0][1] <= 0 or python.body[0][1] >= max_y or python.body.count(python.body[0]) > 1: 
        if input('Gameover! Type any key to continue or "exit" to end game!')=='exit': 
            game_over=True
        else:
            NewGame()
        
    #время
    python.time+=0.4
    time.sleep(0.4)