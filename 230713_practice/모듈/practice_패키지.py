# import travel.thailand # 모듈이나 패키지만 import 가능 class는 불가
# import travel.thailand.ThailandPackage # 오류 발생
# trip_to = travel.thailand.ThailndPackage()
# trip_to.detail()

# from travel.thailand import ThailndPackage
# trip_to = ThailndPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
#trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))