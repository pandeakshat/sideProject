#!/usr/bin/env python
# coding: utf-8

# <H1>WATER JUG PROBLEM USING BFS & DFS<H1>

# Given Problem: You are given a m liter jug and a n liter jug where $0 < m < n$. Both the jugs are initially empty. The jugs don't have markings to allow measuring smaller quantities. You have to use the jugs to measure $d$ liters of water where $d < n$. Determine the minimum no of operations to be performed to obtain $d$ liters of water in one of jug.

# <b>States:</b>  Amount of water in each respective jug, where the states are represented by [S(J1), S(J2)] and S(J1) is the amount in the first jug and S(J2) is the amount in the second jug 
# 
# <b>Capacity of Jug1 (J1):</b> 3 litres
# 
# <b>Capacity of Jug1 (J2):</b> 4 litres
# 
# <b>Initial State:</b> [0,0] 
# 
# <b>Goal state:</b> The user give the input the amount of water required in the jug (J2) i.e. [2,y] or [2,0] 
# 
# These are the initial operators used:
# 
# <b>Operators:</b>  
#             1. Fill the first jug   
#             2. Fill the second jug  
#             3. Empty the first jug
#             4. Empty the second jug
#             5. Pour the first jug into the second jug
#             6. Pour the second jug into the second jug
# 
# <b>Branching Factor:</b>   6 (because we have 6 operators)

# In[1]:


import collections


# In[2]:


#This method return a key value for a given node. 
#Node is a list of two integers representing current state of the jugs
def get_index(node):
    return pow(7, node[0]) * pow(5, node[1])


# In[3]:


#This method accepts an input for asking the choice for type of searching required i.e. BFS or DFS.
#Method return True for BFS, False otherwise
def get_search_type():
    s = input("Enter 'b' for BFS, 'd' for DFS: ")
    #TODO:convert the input into lowercase using lower() method
    s = None
    
    #TODO: Accept the input again if given input is not as 'b' for BFS, 'd' for DFS
    while None:
        s = input("The input is not valid! Enter 'b' for BFS, 'd' for DFS: ")
        s = s[0].lower()
    #TODO: Return True for BFS option selected     
    return None


# In[4]:


#This method accept volumes of the jugs as an input from the user.
#Returns a list of two integeres representing volumes of the jugs.
def get_jugs():
    print("Receiving the volume of the jugs...")
    #TODO: Create an empty list
    jugs = None
    
    temp = int(input("Enter first jug volume (>1): "))
    while temp < 1:
        temp = int(input("Enter a valid amount (>1): "))       
    #TODO: Append the input quantity of jug into jugs list
    None
    
    temp = int(input("Enter second jug volume (>1): "))
    while temp < 1:
        temp = int(input("Enter a valid amount (>1): "))     
    
    #TODO: Append the input quantity of jug into jugs list
    None
    
    #TODO: Return the list
    return None


# In[5]:


#This method accepts the desired amount of water as an input from the user whereas 
#the parameter jugs is a list of two integers representing volumes of the jugs
#Returns the desired amount of water as goal
def get_goal(jugs):
    
    print("Receiving the desired amount of the water...")

    #TODO: Find the maximum capacity of jugs using max()
    max_amount = None
    s = "Enter the desired amount of water (1 - {0}): ".format(max_amount)
    goal_amount = int(input(s))
    #TODO: Accept the input again from the user if the bound of goal_amount is outside the limit between [1,max_amount]
    while None:
        goal_amount = int(input("Enter a valid amount (1 - {0}): ".format(max_amount)))
    
    #TODO:Return the goal amount of water
    return None


# In[6]:


#This method checks whether the given path matches the goal node.
#The path parameter is a list of nodes representing the path to be checked
#The goal_amount parameter is an integer representing the desired amount of water
def is_goal(path, goal_amount):
    
    print("Checking if the goal is achieved...")
    
    #TODO: Return the status of the latest path matches with the goal_amount of another jug
    return path[-1][0] == goal_amount or None


# In[7]:


#This method validates whether the given node is already visited.
#The parameter node is a list of two integers representing current state of the jugs
#The parameter check_dict is   a dictionary storing visited nodes
def been_there(node, check_dict):
    
    print("Checking if {0} is visited before...".format(node))

    #TODO: Return True whether a given node already exisiting in a dictionary, otherwise False. Use get() method of dictionary
    return None


# In[8]:


#This method returns the list of all possible transitions
#The parameter jugs is a list of two integers representing volumes of the jugs
#The parameter path is a list of nodes represeting the current path
#The parameter check_dict is a dictionary storing visited nodes
def next_transitions(jugs, path, check_dict):
    
    print("Finding next transitions and checking for the loops...")
    
    #TODO: create an empty list
    result = None
    next_nodes = None
    node = None
    
    a_max = jugs[0]
    b_max = jugs[1]
    
    #TODO: initial amount in the first jug using path parameter
    a = None   
    #TODO: initial amount in the second jug using path parameter
    b = None 

    #Operation Used in Water Jug problem
    # 1. fill in the first jug
    node.append(a_max)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 2. fill in the second jug
    #TODO: Append with the initial amount of water in first jug
    node.append(None)
    #TODO: Append with the max amount of water in second jug
    node.append(None)
    #TODO: Check if node is not visited then append the node in next_nodes. Use been_there(..,..) method 
    if not None:
        next_nodes.append(node)
    node = []

    # 3. second jug to first jug
    node.append(min(a_max, a + b))
    node.append(b - (node[0] - a))  # b - ( a' - a)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 4. first jug to second jug
    #TODO: Append the minimum between the a+b and b_max
    node.append(None)
    node.insert(0, a - (node[0] - b))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 5. empty first jug
    #TODO: Append 0 to empty first jug
    node.append(None)
    #TODO:Append b amount for second jug
    node.append(None)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 6. empty second jug
    #TODO:Append a amount for first jug
    node.append(None)
    #TODO: Append 0 to empty second jug
    node.append(None)
    if not been_there(node, check_dict):
        next_nodes.append(node)

    # create a list of next paths
    for i in range(0, len(next_nodes)):
        temp = list(path)
        #TODO: Append the ith index of next_nodes to temp
        temp.append(None)
        result.append(temp)

    if len(next_nodes) == 0:
        print("No more unvisited nodes...\nBacktracking...")
    else:
        print("Possible transitions: ")
        for nnode in next_nodes:
            print(nnode)
    #TODO: return result
    return None


# In[9]:


# This method returns a string explaining the transition from old state/node to new state/node
# The parameter old is a list representing old state/node
# The parameter new is a list representing new state/node
# The parameter jugs is a list of two integers representing volumes of the jugs
     
def transition(old, new, jugs):
    
    #TODO: Get the amount of water from old state/node for first Jug
    a = None
    #TODO: Get the amount of water from old state/node for second Jug
    b = None
    #TODO: Get the amount of water from new state/node for first Jug
    a_prime = None
    #TODO: Get the amount of water from new state/node for second Jug
    b_prime = None
    #TODO: Get the amount of water from jugs representing volume for first Jug
    a_max = None
    #TODO: Get the amount of water from jugs representing volume for second Jug
    b_max = None

    if a > a_prime:
        if b == b_prime:
            return "Clear {0}-liter jug:\t\t\t".format(a_max)
        else:
            return "Pour {0}-liter jug into {1}-liter jug:\t".format(a_max, b_max)
    else:
        if b > b_prime:
            if a == a_prime:
                return "Clear {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Pour {0}-liter jug into {1}-liter jug:\t".format(b_max, a_max)
        else:
            if a == a_prime:
                return "Fill {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Fill {0}-liter jug:\t\t\t".format(a_max)


# In[10]:


#This method prints the goal path
#The path is a list of nodes representing the goal path
#The jugs is a list of two integers representing volumes of the jugs
     
def print_path(path, jugs):
    
    print("Starting from:\t\t\t\t", path[0])
    for i in  range(0, len(path) - 1):
        print(i+1,":", transition(path[i], path[i+1], jugs), path[i+1])


# In[11]:


#This method searches for a path between starting node and goal node
# The parameter starting_node is a list of list of two integers representing initial state of the jugs
#The parameter jugs a list of two integers representing volumes of the jugs
#The parameter goal_amount is an integer represting the desired amount
#The parameter check_dict is  a dictionary storing visited nodes
#The parameter is_breadth is implements BFS, if True; DFS otherwise
def search(starting_node, jugs, goal_amount, check_dict, is_breadth):
    
    if is_breadth:
        print("Implementing BFS...")
    else:
        print("Implementing DFS...")

    goal = []
    #TODO: SET accomplished to be False
    accomplished = None
    
    #TODO: Call a deque() using collections 
    q = None
    q.appendleft(starting_node)
    
    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True
        if len(path) >= 2:
            print(transition(path[-2], path[-1], jugs), path[-1])
        if is_goal(path, goal_amount):
            #TODO: Set accomplished to be True
            accomplished = None
            goal = path
            break

        #TODO: Call next_transitions method for generating the further nodes
        next_moves = None
        #TODO: Iterate over the next_moves list
        for i in None:
            if is_breadth:
                q.append(i)
            else:
                q.appendleft(i)

    if accomplished:
        print("The goal is achieved\nPrinting the sequence of the moves...\n")
        print_path(goal, jugs)
    else:
        print("Problem cannot be solved.")


# In[12]:


if __name__ == '__main__':
    starting_node = [[0, 0]]
    #TODO: Call the get_jugs() method
    jugs = None
    #TODO: Call the get_goal() method
    goal_amount = None
    #TODO: Create an empty dictionary
    check_dict = None
    #TODO: call the get_search_type() method 
    is_breadth = None
    #TODO: Call the search method with the required parameters
    search(starting_node, None, None, None, None)


# **BONUS:**
# 
# Include more operations as discussed in class and state your analysis depending on the upcoming 

# In[ ]:




