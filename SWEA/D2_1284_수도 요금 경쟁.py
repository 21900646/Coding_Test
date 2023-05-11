# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1
# A사 : W리터 * P원
# B사 : R리터 > W리터 = Q원 , 초과했으면 추가로 (W - R)리터 * S원
# 두 개 중 최소값으로

T = int(input())

for test_case in range(1, T+1):
  P, Q, R, S, W = map(int, input().split())
  
  A_cost = P * W
  
  if R > W:
    B_cost = Q
  else:
    B_cost = Q + (W-R)*S
  
  print('#{} {}'.format(test_case, min(A_cost, B_cost)))
