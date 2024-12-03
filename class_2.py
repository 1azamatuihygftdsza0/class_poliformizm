from class_1 import Hemis
class Hemis_2(Hemis):
    def __init__(self, age, password, phone_number):
        Hemis.__init__(self, age, password)
#        super().__init__(age, password)
     #  self.age = age
      # self.password = password
        self.phone_number = phone_number
      # self.determinant()
    def determinant(self):
       return f"{self.length_password()}$#@^&8{self.age_determiner()}telefon raqami {self.phone_number}"

Azamat = Hemis_2(18, 'qwertyue1234455', '95 072 04 06')
print(Azamat.determinant())
#print(Azamat.age_determiner())