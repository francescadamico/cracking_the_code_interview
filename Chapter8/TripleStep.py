'''
A child is running up a staircase with n steps and can hop either 1, 2 or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
'''


steps_sum = {}

def ways_climb_steps(n):
  if n == 0:
    steps_sum[0] = 0   
  elif n == 1:
    steps_sum[1] = 1 
  elif n == 2:
    steps_sum[2] = 2 
  elif n == 3:
    steps_sum[3] = 4  
  else:
    if n not in steps_sum.keys():
      steps_sum[n] = ways_climb_steps(n-3) + ways_climb_steps(n-2)+ ways_climb_steps(n-1)
  return steps_sum[n]

t = 60
print(ways_climb_steps(t))
