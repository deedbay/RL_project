import numpy as np
import matplotlib.pyplot as plt
from random import *


SIZE = 4
NB_EPISODES = 25000
MOVE_PENALTY = 1
WALL_PENALTY = 5
GOAL_REWARD = 50

epsilon = 0.9
EPS_DECAY = 0.9998  # Every episode will be epsilon*EPS_DECAY
SHOW_EVERY = 3000

LEARNING_RATE = 0.1
DISCOUNT = 0.95


grid=[]
for j in range(SIZE) :
    l = [0 for i in range(SIZE)]
    grid.append(l)
grid[0][0] = 1 #Agent
grid[2][1] = 2
grid[2][2] = 2 #walls
grid[3][3] = 3 #goal

print(grid)
plt.imshow(grid)


class Agent:
    def __init__(self):
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 :  #On prend les positions x et y de l'agent
                    self.x = i
                    self.y = j
        
    def move(self,x,y) :   
        x1 = self.x
        y1 = self.y
        self.x += x
        self.y += y
        
        if self.x < 0:
            self.x = 0
        elif self.x > SIZE-1:   #Si les positions x ou y de l'agent sont inférieures à 0
            self.x = SIZE-1     #ou supérieures à la taille de la grille on ramène l'agent dans la grille
        if self.y < 0:
            self.y = 0
        elif self.y > SIZE-1:
            self.y = SIZE-1
        if grid[self.x][self.y] == 2 :  #Si l'agent rencontre un mur il reste à sa place
            self.x = x1
            self.y = y1

    def action(self,choice):
        if choice == 0 :
            self.move(1,0) #bouger vers la droite
        if choice == 1 :
            self.move(0,1) #bouger vers le bas
        if choice == 2 :
            self.move(-1,0) #bouger vers la gauche
        if choice == 3 :
            self.move(0,-1) #bouger vers le haut
       
       
       
q_table = []
l1=[]
l2=[]
for i in range(SIZE):   #Création de la q_table : Liste de liste de listes qui
    l1.append(0)        #pour chaque x et chaque y, contient les 4 q_value
    l2.append(l1)
    q_table.append(l2)
    
q_table = np.array(q_table)
    
episode_rewards = []

for episode in range(NB_EPISODES) :
    agent = Agent()
    
    episode_reward = 0
    
    if episode%SHOW_EVERY == 0 :
        print("On episode : ",episode)
        print("Epsilon is : ", epsilon)
        print("mean on last 3000 episodes : ", np.mean(episode_rewards[-SHOW_EVERY:]))
    
    for i in range(200):
        pos_x = agent.x
        pos_y = agent.y
        if np.random.random() <= epsilon :
            choice = np.random.randint(4)
        else :
            choice = np.argmax(q_table[pos_x][pos_y])
        agent.action(choice)
        
        reward=0
        if grid[agent.x][agent.y] == 0:
            reward = - MOVE_PENALTY
        if grid[agent.x][agent.y] == 2 :
            reward = - WALL_PENALTY
        if grid[agent.x][agent.y] == 3 :
            reward = GOAL_REWARD
        
        current_q = q_table[pos_x][pos_y][choice] #On prend la q_value du choix qui vient d'être pris par l'agent
        new_pos_x = agent.x
        new_pos_y = agent.y
        max_next_q = np.max(q_table[new_pos_x][new_pos_y]) #On prend la max q_value du nouvel état
        
        #Update de la q_value du choix qui vient d'être pris
        new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_next_q)
        q_table[pos_x][pos_y][choice] = new_q
        
        
        episode_reward += reward
        if reward == GOAL_REWARD :
            break
    
    episode_rewards.append(episode_reward)
    epsilon*=EPS_DECAY
    
