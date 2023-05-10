# 삼각형 조건 : 제일 큰 길이 < 변1 + 변 2

side = sorted(list(map(int,input().split())))

if side[2] >= side[0] + side[1]:
  side[2] = side[0] + side[1] -1

print(side[0] + side[1] + side[2], end = '')