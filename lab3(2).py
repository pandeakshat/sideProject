#!/usr/bin/env python
# coding: utf-8

# <h1>8 Puzzle Single Player Game (A* Algorithm)</h1>

# <h2>Introduction</h2>
# An instance of the n-puzzle game consists of a board holding $n^{2}-1$ distinct movable tiles, plus an empty space. The tiles are numbers from the set $1,..,n^{2}-1$. For any such board, the empty space may be legally swapped with any tile horizontally or vertically adjacent to it. In this assignment, the blank space is going to be represented with the number 0. Given an initial state of the board, the combinatorial search problem is to find a sequence of moves that transitions this state to the goal state; that is, the configuration with all tiles arranged in ascending order  $0,1,..,n^{2}-1$ . 
# 
# The search space is the set of all possible states reachable from the initial state. The blank space may be swapped with a component in one of the four directions {‘Up’, ‘Down’, ‘Left’, ‘Right’}, one move at a time. 
# 
# 

# In this 8 puzzle problem is discussed. 
# 
# Given a 3×3 board with 8 tiles (every tile has one number from 1 to 8) and one empty space. The objective is to place the numbers on tiles to match final configuration using the empty space. We can slide four adjacent (left, right, above and below) tiles into the empty space. 
# For example:
# 
# ![alt text](https://media.geeksforgeeks.org/wp-content/uploads/puzzle8init.jpg)

# **A* Algorithm:** It is a searching algorithm that searches for the shortest path between the initial and the final state. It is used in various applications, such as maps. In maps the A* algorithm is used to calculate the shortest distance between the source (initial state) and the destination (final state).

# <h2>Explanation</h2>
# A* algorithm has 3 parameters:
# 
# 1.   g : the cost of moving from the initial cell to the current cell.
# 2.   h : also known as the heuristic value, it is the estimated cost of moving from the current cell to the final cell. The actual cost cannot be calculated until the final cell is reached. Hence, h is the estimated cost. We must make sure that there is never an over estimation of the cost.
# 3.   f : it is the sum of g and h. So, f = g + h
# 

# <h3>Example: A*</h3>
# <h5>Initial State: 1,2,5,3,4,0,6,7,8</h5>
# 
# 
# <img src="https://sandipanweb.files.wordpress.com/2017/03/sol_b0.gif?w=676" width="250" align="center">
# 

# The path to the goal node with A* (also the nodes expanded by A*) is shown in the following figure:
# 
# <img src="https://sandipanweb.files.wordpress.com/2017/03/b_a0-gv.png" width="350" align="center">

# **Dear Students, in the code below there are few *TODO* task that you have to complete in this lab session.**

# In[1]:


from time import time
from queue import PriorityQueue
import math


# In[2]:


#Creating a class Puzzle
class Puzzle:
    #Setting the goal state of 8-puzzle
    goal_state=[1,2,3,8,0,4,7,6,5]
    #Setting up the members of a class
    heuristic=None
    evaluation_function=None
    needs_hueristic=True
    num_of_instances=0
    #constructor to initialize the class members
    def __init__(self,state,parent,action,path_cost,needs_hueristic=False):
        self.parent=parent
        self.state=state
        self.action=action
         #TODO: calculate the path_cost as the sum of its parent cost and path_cost
        if parent:
            self.path_cost = parent.path_cost+path_cost
        else:
            self.path_cost = path_cost
        if needs_hueristic:
            self.needs_hueristic=True
            self.generate_heuristic()
             #TODO: calculate the expression as f = g + h
            self.evaluation_function=self.path_cost+self.heuristic
        #TODO: incrementing the number of instance by 1
        Puzzle.num_of_instances+=1
    
    #method used to display a state of 8-puzzle
    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    #method used to generate a heuristic value
    def generate_heuristic(self):
        self.heuristic=0
        for num in range(1,9):
            #TODO: calculate the heuristic value as manhattan distance which is the absolute 
            
            #difference between current state and goal state. 
            #Use index() method to get the index of num in state
            distance=abs(self.state.index(num) -self.goal_state.index(num))
            i=int(distance/3)
            j=int(distance%3)
            self.heuristic=self.heuristic+i+j

    def goal_test(self):
        #TODO: include a condition to compare the current state with the goal state
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i,j):
        #find the legal actions as Up, Down, Left, Right based on each cell of state
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            # if row is 0 in board then up is disable
            legal_action.remove('U')
        elif i == 2:  
             legal_action.remove('D')
        if j == 0:
             legal_action.remove('L')
        elif j == 2:
             legal_action.remove('R')
         #TODO: return legal_action
        return legal_action

    #method to generate the child of the current state of the board
    def generate_child(self):
         #TODO: create an empty list
        children=[]
        x = self.state.index(0)
        #TODO: generate the row (i) & col (j) position based on the current index of 0 on the board 
        i = int(x/3)
        j = int(x%3)
        #TODO: call the method to find the legal actions based on i and j values
        legal_actions=self.find_legal_actions(i,j);

        for action in legal_actions:
            new_state = self.state.copy()
            #if the legal action is UP
            if action is 'U':
                #Swapping between current index of 0 with its up element on the board
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action is 'D':
                #TODO: Swapping between current index of 0 with its down element on the board
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action is 'L':
                #TODO: Swapping between the current index of 0 with its left element on the board
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action is 'R':
                #TODO: Swapping between the current index of 0 with its right element on the board
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            #TODO: Append the new_state of Puzzle object with parent, action,path_cost is 1, its needs_hueristic flag
            children.append(Puzzle(new_state,self,action,1,self.needs_hueristic ))
        
        #TODO: return the children
        return children
    
    #method to find the solution
    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution


# In[3]:


#method for A-star search
#TODO: pass the initial_state as parameter to the breadth_first_search method
def Astar_search(initial_state):
    count=0
    #TODO: create an empty list of explored nodes
    explored=[]
    #TODO: create a instance of Puzzle as initial_state, None, None, 0, True
    start_node=Puzzle(initial_state,None,None,0,True)
    q = PriorityQueue()
    #TODO: put a tuple with start_node.evaluation_function, count, start_node into PriorityQueue
    q.put((start_node.evaluation_function, count, start_node))

    while not q.empty():
        #TODO: get the current node of a queue. Use the get() method of Queue
        node=q.get() 
        #TODO: extract the current node of a PriorityQueue based on the index of a tuple. 
        #Refer a tuple format put in PriorityQueue  
        node=node[2]
        #TODO: Append the state of node in the explored list as node.state
        explored.append(node.state)
        if node.goal_test():
            return node.find_solution()
        #TODO: call the generate_child method to generate the child node of current node
        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                #TODO: put a tuple with child.evaluation_function, count, child into PriorityQueue
                q.put((child.evaluation_function,count, child))
    return


# In[4]:


#Start executing the 8-puzzle with setting up the initial state
#Here we have considered 3 initial state intitalized using state variable
from time import time
from queue import PriorityQueue
import math
state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]
#Iterate over number of initial_state
for i in range(0,3):
    #TODO: Initialize the num_of_instances to zero
    Puzzle.num_of_instances = 0
    #Set t0 to current time
    t0 = time()
    astar = Astar_search(state[i])
    #Get the time t1 after executing the breadth_first_search method
    t1 = time() - t0
    print('A*:',astar)
    print('space:', Puzzle.num_of_instances)
    print('time:', t1)
    print()
    print('------------------------------------------')


# **BONUS TASK:** Now, perform the following task before submitting the assignment:
# 
# Show the path in traversing the A-star algorithm of each state from intial_state to goal state.

# In[ ]:


yes


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




