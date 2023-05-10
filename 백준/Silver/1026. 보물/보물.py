# A와 B를 서로 반대로 sorting

result = 0

T = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse = True)

for i in range(T):
  result += A[i] * B[i]

print(result)