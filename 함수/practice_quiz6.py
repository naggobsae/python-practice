def std_weight(height, gender):
    if gender == "man":
        weight = round(((height*0.01)**2)*22, 2)
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다."\
              .format(height, weight))
    elif gender == "woman":
        weight = round(((height*0.01)**2)*21, 2)
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다."\
              .format(height,weight))
    else:
        print("잘못된 정보입니다.")

height = 175
gender = "man"
std_weight(height, gender)
