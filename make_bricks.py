'''the aim of this function if to check if the small or big bricks 
can be used to reach the "goal" number small bricks are equal to 1
while big bricks are equal to 5.'''

def make_bricks(small, big, goal):
  #first define the true value of big bricks
  big_brick = big*5
  return (goal-big)<=small

