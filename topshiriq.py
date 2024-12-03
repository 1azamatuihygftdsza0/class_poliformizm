class click:
    def __init__(self, user_name, password, balans):
        self.user_name = user_name
        self.password = password
        self.balans = balans
        self.determiner()
    def determiner(self):
        if len(self.password) >= 8:
            return "Ro'yxatdan o'tdingiz va parolingiz kuchli"
        else:
            raise ValueError("Kodingizda kamida sakkizta element "
                             "ishtirok etishi kerak")
Azamat = click("azamat", "12345556666666", 800000)













