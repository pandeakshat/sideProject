
capacity = []
temp = int(input("Enter max jug volume (>1): "))
    
while temp < 1:
    temp = int(input("Enter a valid amount (>1): "))       
#TODO: Append the input quantity of jug into jugs list
capacity.append(temp)
    
temp = int(input("Enter second jug volume (>1): "))
while temp < 1:
    temp = int(input("Enter a valid amount (>1): "))     
    
#TODO: Append the input quantity of jug into jugs list
capacity.append(temp)
    
temp = int(input("Enter minimum jug volume (>1): "))
while temp < 1:
    temp = int(input("Enter a valid amount (>1): "))     
#TODO: Append the input quantity of jug into jugs list
capacity.append(temp)

# Maximum capacities of 3 jugs -> x,y,z
x = capacity[0]
y = capacity[1]
z = capacity[2]

# to mark visited states
memory = {}

print("Receiving the desired amount of the water...")
max_amount = max(capacity[1],capacity[2])
s = "Enter the desired amount of water (1 - {0}): ".format(max_amount)
ans = int(input(s))
#TODO: Accept the input again from the user if the bound of goal_amount is outside the limit between [1,max_amount]
while ans< 1 or ans>max_amount:
        ans = int(input("Enter a valid amount (1 - {0}): ".format(max_amount)


def get_all_states(state):
  # Let the 3 jugs be called a,b,c
  a = state[0]
  b = state[1]
  c = state[2]

  if(a==ans or b==ans):
      ans.append(state)
      return True

  # if current state is already visited earlier
  if((a,b,c) in memory):
      return False

  memory[(a,b,c)] = 1

  #empty jug a
  if(a>0):
      #empty a into b
      if(a+b<=y):
          if( get_all_states((0,a+b,c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(y-b), y, c)) ):
              ans.append(state)
              return True
      #empty a into c
      if(a+c<=z):
          if( get_all_states((0,b,a+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a-(z-c), b, z)) ):
              ans.append(state)
              return True

  #empty jug b
  if(b>0):
      #empty b into a
      if(a+b<=x):
          if( get_all_states((a+b, 0, c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b-(x-a), c)) ):
              ans.append(state)
              return True
      #empty b into c
      if(b+c<=z):
          if( get_all_states((a, 0, b+c)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, b-(z-c), z)) ):
              ans.append(state)
              return True

  #empty jug c
  if(c>0):
      #empty c into a
      if(a+c<=x):
          if( get_all_states((a+c, b, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((x, b, c-(x-a))) ):
              ans.append(state)
              return True
      #empty c into b
      if(b+c<=y):
          if( get_all_states((a, b+c, 0)) ):
              ans.append(state)
              return True
      else:
          if( get_all_states((a, y, c-(y-b))) ):
              ans.append(state)
              return True

  return False

initial_state = (12,0,0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()
for i in ans:
  print(i)
