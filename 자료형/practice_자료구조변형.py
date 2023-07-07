# 자료구조의 변형
menu = {"coffee", "milk", "juice"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

#quiz

from random import *
users = range(1, 21) # 1부터 20까지의 숫자를 생성
print(type(users))
users = list(users)
print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print(" -- 당첨자 발표 -- ")
print("치킨 당점차 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
