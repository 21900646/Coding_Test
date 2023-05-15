# https://swexpertacademy.com/main/code/problem/problemDetail.do

import math

def change(T, price):
    changer = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = [0,0,0,0,0,0,0,0]

    for i in range(len(changer)):
        result[i] = math.floor(price / changer[i])
        price -= result[i] * changer[i]

    print('#{}'.format(T+1))
    result_str = list(map(str, result))
    print(' '.join(result_str))



if __name__ == '__main__':
    T = int(input())

    for i in range(int(T)):
        input_num = int(input().strip())
        change(i, input_num)
