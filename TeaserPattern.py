import math
import numpy as np

# Here, r  = 2. N is any term?
# n=1
# r=0

# Just so it looks nice
np.set_printoptions(suppress=True)

def pat(n, r):
    try:
        return (6* math.pow(n, 2) + 6*n*r + math.pow(r, 2) - r) * math.factorial(n+r)/(math.factorial(r+3) * math.factorial(n-1))
    except:
        return 1


#List number of rows (r =142 max, ends 147:
r = 57

#List number of columns (numbers per series):
n = 7

# Array of patterns
a = np.ones((r, n))
for x in range(0, r):
    for y in range(0, n):
        a[x, y] = round(pat(y + 1, x-2))

print(a)
