import math
from math import pi
from math import floor
# Read user input
radians = float(input())
# Logic
degrees = radians * 180 / pi
# Output
print(floor(degrees))
print(math.ceil(degrees))
