# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq
# K 길이만큼 이어진 부분이 있는지 확인. (1 탐색)
# 가로일 경우, [동일][]
# 세로일 경우, [][동일]

T = int(input())

for test_case in range(1, T+1):
  N, K = map(int, input().split())
  result = 0

  puzzle = []

  # 퍼즐 판 제작(이중배열 입력받기)
  for N in range(1, N+1):
    puzzle.append(list(map(int, input().split())))

  # 1 탐색 (이중for문 활용)
  for i in range(0, N):
    count_x = 0
    count_y = 0
    
    for j in range(0, N):
      # 가로 탐색
      if puzzle[i][j] == 1:
        count_x += 1

      else: 
        if count_x == K:
          result += 1
        count_x = 0

      # 세로 탐색
      if puzzle[j][i] == 1:
        count_y += 1

      else:
        if count_y == K:
          result += 1
        count_y = 0


    # 엔터로 끝나는 경우, 추가 조건
    if count_x == K:
      result += 1
      
    if count_y == K:
      result += 1
  
  print('#{} {}'.format(test_case, result))


