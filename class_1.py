 #   yosh qushamiz yosh un sakkizdan katta busa olish bumasa
 #   yuq loginda harf ham qatnashishi kerak l
# loginda [8 dan 20 gacha harf va so'z qatnashishi kerak
class Hemis:
    def __init__(self, age, password):
        self.age = age
        self.password = password
        # self.age_determiner()
        # self.length_password()
    def age_determiner(self):
        if self.age >= 18:
            return "Ro'yxatga olindingiz"
        else:
            raise ValueError("Yoshingiz 18 dan kichik")
            #print("Xato")
    def length_password(self):
       if 8 <= len(self.password) <=20 and not self.password.isalpha() and not self.password.isdigit():
           return "Parolingiz kuchli va siz ro'yxatdan o'tdingiz"
       else:
            return "Parol kuchsiz"
Azamat = Hemis(18, '455434vfvre65d77')
print(Azamat.length_password())
print(Azamat.age_determiner())
















