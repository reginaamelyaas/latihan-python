import datetime


from user import User
from plan import basic_plan, standard_plan, premium_plan




shandy = User('Shandy', basic_plan, datetime.date(2022,7,2))
cahya = User('Cahya', standard_plan, datetime.date(2021,7,2))
ana = User('Ana', standard_plan, datetime.date(2017,2,19))
bagus = User('Bagus', premium_plan, datetime.date(2022,8,22))

#case 1
cahya.check_all_plan()

#case 2
shandy.current_plan

#case 3
print(ana.upgrade_plan(premium_plan))

#case 4
faizal = User("faiza", standard_plan, datetime.date.today())
print(faizal.redeem_code(bagus.refferal_code))