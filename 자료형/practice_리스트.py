# 리스트 []

subway = [10, 20, 30]
print(subway)

# 20이 몇 번째 칸에 있는가?
print(subway.index(20))

# 40이 다음 칸에 탑승
subway.append(40)
print(subway)

# 50을 10과 20 사이에 탑승
subway.insert(1, 50)
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# print(subway.pop())
# print(subway)

# print(subway.pop())
# print(subway)

# 같은 숫자가 몇 개 있는지 확인하기
subway.append(10)
print(subway)
print(subway.count(10))

#정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#순서 뒤집기도 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용가능
mix_list = ["apple", 20, True]
print(mix_list)

#list 확장
num_list = [5,2,4,3,1]
num_list.extend(mix_list)
print(num_list)