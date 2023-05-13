# 7일로 나누기. 총 며칠 지났는지 계산해서

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
final_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total_day = 0

month, day = map(int, input().split())

for i in range (month):
  total_day += final_day[i]

print(week[(total_day + day)%7])