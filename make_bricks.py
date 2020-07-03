'''the aim of this function if to check if the small or big bricks 
can be used to reach the "goal" number small bricks are equal to 1
while big bricks are equal to 5.'''

def make_bricks(small, big, goal):
  #first define the true value of big bricks
  big_brick = big*5
  #next check if all bricks are enough to reach the goal
  if big_brick + small < goal: 
    return False
  elif big_brick == goal: 
    return True #check if big bricks can be used to reach goal
  elif small == goal:
    return True #check if small bricks can be used to reach goal
  elif small + big_brick == goal:
    return True #check if all bricks can make the goal
  elif goal < small:
    return True #if there are enough small bricks to make the goal, this will naturally be True
  elif big and goal % 5 in range(0, (small+1)):
    return True #check if big bricks are enough, while checking if the goal is within the range of small bricks left over
  else:
    return False

