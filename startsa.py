import telebot
bot = telebot.TeleBot("7505646394:AAEjacgjsSM96m84LIX2hKdx6gxAFOLMx2k")

books = ["Alisher Navoiy - Xamsa",
    "Abdulla Qodiriy - O'tgan kunlar",
    "Chingiz Aytmatov - Asrga tatigulik kun",
    "Umar Xayyom - Ruboiylar",
    "Islom Karimov - O'zbekiston mustaqillik yo'lida",
    "Jules Verne - Yer markaziga sayohat",
    "Fyodor Dostoevsky - Jinoyat va jazo",
    "Erkin Vohidov - Tong nafasi",]

# /start yoki /help komandasi
@bot.message_handler(commands=['start', 'help'])
def salomlashuv(message):
    javob = ("Assalomu alaykum! 📚\n\n"
        "Men sizga quyidagi imkoniyatlarni beraman:\n"
        "1. Kitoblarni ko'rish uchun /kitoblar yozing.\n"
        "2. Kitob qidirish uchun kitob nomining bir qismini yozing.")
    bot.reply_to(message, javob)

@bot.message_handler(commands=['kitoblar'])
def kitoblar_ruyxati(message):
    javob = "📚 Mavjud kitoblar ro'yxati:\n\n"
    for idx, book in enumerate(books, start=1):
        javob += f"{idx}. {book}\n"
    bot.reply_to(message, javob)



@bot.message_handler(func=lambda message: True)
def qidiruv(message):
    surov = message.text.lower()
    natijalar = [book for book in books if surov in book.lower()]
    if natijalar:
        surov = "🔍 Qidiruv natijalari:\n\n"
        for idx, book in enumerate(natijalar, start=1):
            surov += f"{idx}. {book}\n"
    else:
        surov = "❌ Afsuski, qidiruv bo'yicha hech narsa topilmadi."
    bot.reply_to(message, surov)
bot.polling()
# # Botni ishga tushirish
# if __name__ == "__main__":
#     try:
#         bot.polling()
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")

