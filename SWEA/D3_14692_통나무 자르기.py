# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AYJW0g-qlO8DFASv&categoryId=AYJW0g-qlO8DFASv&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1
  

def winner(T, num):
    if num % 2 == 0:
        print('#{} Alice'.format(T))
    else:
        print('#{} Bob'.format(T))


if __name__ == '__main__':
    T = int(input().strip())
    for i in range(1, T+1):
        winner(i, int(input().strip()))
