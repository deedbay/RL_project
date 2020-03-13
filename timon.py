import pygame
import sys
import math
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os


screen = pygame.display.set_mode((960, 960))

class spot:
    def __init__(self, x, y):
        self.i = x
        self.j = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.obs = False
        self.value = 1

    def show(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

NOMBRE_COL = 12
NOMBRE_ROW = 12
cols = NOMBRE_COL
grid = [0 for i in range(cols)]
row = NOMBRE_ROW
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
w = 960 / cols
h = 960 / row

# create 2d array
for i in range(cols):
    grid[i] = [0 for i in range(row)]

# Create Spots
for i in range(cols):
    for j in range(row):
        grid[i][j] = spot(i, j)


for i in range(cols):
    for j in range(row):
        grid[i][j].show((0,0,0), 0)

#def onsubmit():
#    global start
#    global end
#    st = startBox.get().split(',')
#    ed = endBox.get().split(',')
#    start = grid[int(st[0])-1][int(st[1])-1]
#    end = grid[int(ed[0])-1][int(ed[1])-1]
#    window.quit()
#    window.destroy()
#
#window = Tk()
#label = Label(window, text='Départ(x,y): ')
#startBox = Entry(window)
#label1 = Label(window, text='fin mgl(x,y): ')
#endBox = Entry(window)
#var = IntVar()
#
#
#submit = Button(window, text='Submit', command=onsubmit)
#
#submit.grid(columnspan=2, row=3)
#label1.grid(row=1, pady=3)
#endBox.grid(row=1, column=1, pady=3)
#startBox.grid(row=0, column=1, pady=3)
#label.grid(row=0, pady=3)
#
#window.update()
#mainloop()
start = grid[0][0]
end = grid[NOMBRE_COL-1][NOMBRE_ROW-1]
pygame.init()

def mousePress(x):
    t = x[0]
    w = x[1]
    g1 = t // (960 // cols)
    g2 = w // (960 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)
def mousePress2(x):
    t = x[0]
    w = x[1]
    g1 = t // (960 // cols)
    g2 = w // (960 // row)
    acess = grid[g1][g2]
    if acess != start and acess != end:
        if acess.obs == True:
            acess.obs = False
            acess.show((0,0,0), 0)
           
        

end.show((255, 8, 127), 0)
start.show((127, 8, 255), 0)
#stud = pygame.image.load("student.png")
#screen.blit(stud, (start.i, start.j))

loop = True
while loop:
    ev = pygame.event.get()
    for event in ev:
        #screen.blit(stud, (start.i, start.j))
        if event.type == pygame.QUIT:
            pygame.quit()
        if pygame.mouse.get_pressed()[0]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress(pos)
            except AttributeError:
                pass
        elif pygame.mouse.get_pressed()[2]:
            try:
                pos = pygame.mouse.get_pos()
                mousePress2(pos)
            except AttributeError:
                pass
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                loop = False
                break
            elif event.key == pygame.K_a:
                x, y = pygame.mouse.get_pos()
                g1 = x // (960 // cols)
                g2 = y // (960 // row)
                acess = grid[g1][g2]
                if acess != start and acess != end and acess.obs == False:
                    end.show((0,0,0), 0)
                    end = acess
                    end.show((255, 8, 127), 0)
            
            elif event.key == pygame.K_d:
                x, y = pygame.mouse.get_pos()
                g1 = x // (960 // cols)
                g2 = y // (960 // row)
                acess = grid[g1][g2]
                if acess != start and acess != end and acess.obs == False:
                    start.show((0,0,0), 0)
                    start = acess
                    start.show((127, 8, 255), 0)
                    #screen.blit(stud, ((x // w), (y // w)))
            

                    

def main():
    end.show((255, 8, 127), 0)
    start.show((255, 8, 127), 0)
    pygame.quit()
