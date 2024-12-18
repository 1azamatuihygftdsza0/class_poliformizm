import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot("7609544102:AAE8VTk5W_WZz-Tuzt8jDvHl63NRa4I3mkE")
ruyxat = {}

def menyu():
    tugmalar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    xarajat_qushish = KeyboardButton("Xarajat qo‘shish")
    maslahat_olish = KeyboardButton("Tavsiyalar olish")
    ruyxatni_tozalash = KeyboardButton("Xarajatlarni tozalash")
    yordam = KeyboardButton("Yordam")
    tugmalar.add(xarajat_qushish, maslahat_olish,ruyxatni_tozalash, yordam)
    return tugmalar


@bot.message_handler(commands=['start'])
def tanishtiruv(message):
    bot.send_message(
        message.chat.id,"Salom! Men sizning xarajatlaringiz asosida byudjet tavsiyalarini bera olaman.\n"
        "Quyidagi tugmalardan foydalaning:",
        reply_markup=menyu())

@bot.message_handler(func=lambda message: message.text == "Xarajat qo‘shish")
def summa_qushuvchi(message):
    bot.reply_to(message, "Xarajatlar turini va summasini quyidagicha kiriting:\n\n`Ovqat: 50000`\n")
    bot.register_next_step_handler(message, malumot_oluvchi)

def malumot_oluvchi(message):
    try:
        xarajat, summa = message.text.split(":")
        summa = int(summa.strip())
        user_id = message.chat.id

        if user_id not in ruyxat:
            ruyxat[user_id] = {}

        if xarajat in ruyxat[user_id]:
            ruyxat[user_id][xarajat] += summa
        else:
            ruyxat[user_id][xarajat] = summa

        bot.reply_to(message, f"'{xarajat}' uchun {summa} so‘m qo‘shildi!")
    except:
        bot.reply_to(message, "Xatolik! Iltimos, xarajatlaringizni to‘g‘ri formatda kiriting: \n Ovqat:50000 ")


@bot.message_handler(func=lambda message: message.text == "Tavsiyalar olish")
def vazir(message):
    user_id = message.chat.id

    if user_id not in ruyxat or not ruyxat[user_id]:
        bot.reply_to(message, "Sizda hozircha hech qanday xarajatlar qayd etilmagan.")
        return

    total_expense = sum(ruyxat[user_id].values())
    recommendations = ("Sizning xarajatlaringiz tahlili:\n"
        f"Jami xarajat: {total_expense} so‘m\n\n")

    for category, amount in ruyxat[user_id].items():
        recommendations += f" - {category}: {amount} so‘m\n"

    recommendations += "\nTavsiyalar:\n"
    if total_expense > 500000:
        recommendations += "Jami xarajatingiz yuqori. Iltimos, tejashni boshlang.\n"
    else:
        recommendations += "Xarajatingiz nazorat ostida. Ajoyib!\n"

    bot.reply_to(message, recommendations)


@bot.message_handler(func=lambda message: message.text == "Xarajatlarni tozalash")
def tozalovchi(message):
    user_id = message.chat.id
    ruyxat[user_id] = {}
    bot.reply_to(message, "Xarajatlaringiz tozalandi!")
@bot.message_handler(func=lambda message: message.text == "Yordam")
def kumak(message):
    bot.reply_to(message, "Bu bot Namozovning bergan bilimlari asosida tayyorlandi.\n Shogirdlaringizni qo'llab quvvatlab 5 baho"
                          " qo'yasiz degan umiddamiz ➕5️⃣✅")
bot.polling()