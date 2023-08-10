cabinet = {3:"유재석", 100:"김태호"}

# 3번 열쇠를 유재석이 받고 100번 열쇠를 김태호가 받음

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5]) 오류 출력 hi가 출력되지 x
#print(cabinet.get(5)) none 값을 출력 hi가 출력됨
print("hi")
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능")) #5가 없으면 뒤의 문장을 출력

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

#새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-3"] = "조세호"
print(cabinet)

#간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value값만 출력
print(cabinet.values())

#ket, value 창으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)