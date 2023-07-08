for i in range(1, 11):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as files:
        files.write("- {0} 주차 주간보고 -".format(i))
        files.write("\n부서 : ")
        files.write("\n이름 : ")
        files.write("\n업무 요약 : ")