import math

n = input('Value of dot product of (a+b) and (a-b):')
k = input('If |a| = k|b|, then enter the value of k:')
mod_b = math.sqrt(int(n)/((int(k)**2)-1))
mod_a = int(k)*mod_b
print('|b| = ', mod_b)
print('|a| = ', mod_a)