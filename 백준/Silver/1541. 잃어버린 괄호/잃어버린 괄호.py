# '-'가 나온 이후부터는 모두 빼주면 됨.
# 괄호를 모두 지웠다 -> -( + ) - ( + +) 이렇게 하면 되기 때문에.

import re 

change = 0       # 0:+/ 1:-
result = 0

input = input()
num_list = re.split('([-|+])', input)

for i in num_list:
  if i == '-':
    change = 1

  elif i != '+':
    if change == 1:
      result -= int(i)
    else:
      result += int(i)

print(result)