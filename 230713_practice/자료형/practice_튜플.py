# 튜플은 안의 내용을 변경 불가, 하지만 리스트보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선까스") 에러 발생

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name , age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)