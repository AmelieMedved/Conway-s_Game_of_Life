# coding: utf-8

import pygame as pg
from random import randint
from copy import deepcopy

c0 = (0,0,0)
c1 = (88, 100, 200)
c2 = (200,233,255)
width, height =  1300, 750
cell = 25
res = width, height
w, h = width//cell, height//cell
fps = 30
next_cell_cond = []
curr_cell_cond = []

pg.init()
surface = pg.display.set_mode(res)
pg.display.set_caption("Conway's Game of Life") 
clock = pg.time.Clock()

for i in range(h):
  tmp = []
  for j in range(w):
    tmp.append(0)
  next_cell_cond.append(tmp)
  
for i in range(h):
  tmp = []
  for j in range(w):
    tmp.append(randint(0, 1))
  curr_cell_cond.append(tmp)

def check_cell_cond(curr_cell_cond, x, y):
  count = 0
  for i in range(y - 1, y + 2):
    for j in range(x - 1, x + 2):
      if curr_cell_cond[i][j]:
        count += 1 
  if curr_cell_cond[y][x]:
    count -= 1
    if count == 2 or count == 3:
      return 1
    return 0
  else:
    if count == 3:
      return 1
    return 0
  
flag = True
while flag:
  surface.fill(c0)
  for event in pg.event.get():
    if event.type == pg.QUIT:
      pg.quit()
      flag = False
      
  for x in range(0, width, cell):
    pg.draw.line(surface, c1, (x, 0), (x, height))
  for y in range(0, height, cell):
    pg.draw.line(surface, c1, (0, y), (width, y))
  
  for x in range(1, w - 1):
    for y in range(1, h - 1):
      if curr_cell_cond[y][x]:
        pg.draw.rect(surface, c2, (x * cell + 2, y * cell + 2, cell - 2, cell - 2))
      next_cell_cond[y][x] = check_cell_cond(curr_cell_cond, x, y)
      
  curr_cell_cond = deepcopy(next_cell_cond)

  pg.display.flip()
  clock.tick(fps)  
