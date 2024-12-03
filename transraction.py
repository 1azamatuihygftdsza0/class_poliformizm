from urllib.parse import non_hierarchical

from class_2 import Azamat
from topshiriq import click
class user(click):
    def __init__(self, user_name, password, balans):
        click.__init__(self, user_name, password, balans)
        self.add_money_transfer(500000)
        self.transfer(500000)
    def add_money_transfer(self, money):
        if self.balans >= money:
            self.balans -= money
            return f"mablag'ngizda {self.balans} so'm qoldi"
        else:
            raise ValueError("Mablag'ingizda yetarli mablag' mavjud emas")
    def transfer(self, money):
        self.balans += money
        return f"Hisobingizda {self.balans} so'm pul bor"
    def information(self):
        return f"sizning pulingiz {self.balans} so'm "

Azamat = user("azamat", "324567897654", 800000)
print(Azamat.information())
