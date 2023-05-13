# A*day - B*(day-1) = V
# A*day - B*day + B = V
# day = (V - B) / (A - B)

import math

A, B, V = map(int, input().split())
print(math.ceil((V - B) / (A - B)))