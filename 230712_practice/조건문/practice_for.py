for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # 0,1,2,3,4
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["a", "b", "c"]
for customer in starbucks:
    print("{0}, coffee is ready".format(customer))

# 한 줄로 끝내는 for
# 출석번호가 1,2,3,4 앞에 100을 붙이기로 함 ->101,102,103,104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)