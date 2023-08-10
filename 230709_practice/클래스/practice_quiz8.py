class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    #매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}"\
              .format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))
        
h1 = House("강남", "아파트", "매매", "10악", "2010년")
h2 = House("마포", "오피스텔", "전세", "5억", "2007년")
h3 = House("송파", "빌라", "월세", "500/50", "2000년")

house = []
house.append(h1)
house.append(h2)
house.append(h3)

print("총 {0} 대의 메물이 있습니다.".format(len(house)))
for i in house:
    i.show_detail()