python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java"))
#print(python.index("java"))
print("hi")

print(python.count("n"))




print("나는 %d살입니다" % 20)
print("나는 %s를 좋아해요." % "python")
print("apple은 %c로 시작해요." % "a")

print("나는 %s색과 %s색을 좋아해요." % ("blue", "red"))
print("나는 {}살입니다.".format(20))
print("나는 {} 색과 {} 색을 좋아해.".format("red", "blue"))
print("나는 {1} 색과 {0} 색을 좋아해.".format("red", "blue"))
print("나는 {0} 색과 {1} 색을 좋아해.".format("red", "blue"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "red"))



print("백문이 불여일견\n백견이 불여일타")
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

print("C:\\Users\\이동현\\OneDri")

print("Red Apple\rPine")

print("Redd\bApple")

print("Red\tApple")




site = "http://naver.com"

password1 = site.replace("http://", "")
password2 = password1.replace(password1[password1.index("."):], "")
password3 = password2[:3] + str(len(password2)) + str(password2.count("e")) + "!"

print("생성된 비밀번호 : %s" % password3)

