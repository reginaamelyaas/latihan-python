import random
import datetime
from dateutil.relativedelta import relativedelta
from plan import basic_plan, standard_plan, premium_plan

class User:
  __secret_code = ('6jh7', 'abcd', '20a4', '97ny', 'ijkl', '90pj', '34gh')
  __list_refcode_user = {}


  def __init__(self, username, choosen_plan, register_date):
    self.username = username
    self.current_plan = choosen_plan
    self.register_date = register_date
    self.bill = choosen_plan.price

  # generate refferal code
    self.refferal_code= username + '-' + self.__secret_code[random.randint( 0, len(self.__secret_code)-1)]
    self.__list_refcode_user[self, username]= self.refferal_code


  def upgrade_plan(self, new_plan):
    if new_plan.price <= self.current_plan.price:
      print("Anda tidak dapat melakukan downgrade, pilih plan yang lebih tinggi")
      return

    difference_in_years = relativedelta(datetime.date.today(), self.register_date).years
    pay = 1

    if difference_in_years >= 1:
      pay = 0.95

    self.bill = pay * new_plan.price
    self.current_plan = new_plan
    return self.bill

  def redeem_code(self, code):
    if code in self.__list_refcode_user.values():
      self.bill = 0.96 * self.current_plan.price
      return True, self.bill
    else:
      return False, "Refferal code anda invalid"

  def check_all_plan(self):
    for plan in list_plan:
      plan.check_plan()

list_plan = [basic_plan, standard_plan, premium_plan]