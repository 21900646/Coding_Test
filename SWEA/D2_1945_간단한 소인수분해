T = int(input())
prime = [2,3,5,7,11]

for test_case in range(1, T+1):
  num = int(input())
  result = [0,0,0,0,0]
  index = 0
  
  while num >= 2:
    if num % prime[index] == 0:
      num = num / prime[index]
      result[index] = result[index] + 1
      
    else:
      index += 1
      if index > len(prime)-1:
        break
  result_str = list(map(str, result))
  print('#{} {}'.format(test_case, ' '.join(result_str)))
