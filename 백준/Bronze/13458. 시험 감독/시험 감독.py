# 총감독관 1명 필수 + 부감독관 여러명
# 학생수 = 총감독관이 감시할 수 있는 수 + 부감독관이 감시할 수 있는 수 * X
# X = (학생수 - 총감독관 감시 수)/(부감독관이 감시할 수 있는 수) -> 0일때도 생각

import math

def count(A, n1, n2):
    result = 0
    for a in A:
        if a > n1:
            result += 1 + math.ceil((a-n1)/n2)
        else:
            result += 1
    print(result)


if __name__ == '__main__':
    N = int(input())
    A = map(int, input().split())
    n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    count(A, n1, n2)