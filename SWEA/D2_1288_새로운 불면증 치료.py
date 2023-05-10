# set으로 만들어서 비교하기.

T = int(input())
 
for test_case in range(1, T+1):
  num_check = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
  result = 0
 
  N = int(input())
 
  while num_check != set():
    new = set(str(N * (result+1)))
    num_check = num_check.difference(new)
    result += 1
   
  print('#{} {}'.format(test_case, N * result))
