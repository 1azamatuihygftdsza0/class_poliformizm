# Chiroyli sonni tekshiruvchi funksiya (stringdan foydalanmasdan)
royli_sonmi(son):
    # To'rt xonali son bo'lishi kerak
    if son < 1000 or son > 9999:
        return False

    # Har bir raqamni alohida ajratib olamiz
    a = son // 1000  # minglar xonasi
    b = (son // 100) % 10  # yuzlar xonasi
    c = (son // 10) % 10  # o'nlar xonasi
    d = son % 10  # birliklar xonasi

    # Shartni tekshiramiz: a + d = b + c
    return a + d == b + c


# Foydalanuvchidan son kiritishni so'raymiz
son = int(input("Iltimos, to'rt xonali son kiriting: "))

# Chiroyli sonligini tekshiramiz va natijani chiqaramiz
if chiroyli_sonmi(son):
    print(f"{son} chiroyli son!")
else:
    print(f"{son} chiroyli son emas.")