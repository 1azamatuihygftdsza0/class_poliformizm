import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
bot = telebot.TeleBot("7609544102:AAE8VTk5W_WZz-Tuzt8jDvHl63NRa4I3mkE")
ruyxat = {}
kanal_link = "https://t.me/python_1_eng_kerakli"
kanal_user_name = "@python_1_eng_kerakli"
def menyu():
    tugmalar = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    xarajat_qushish = KeyboardButton("Xarajat qo‘shish")
    maslahat_olish = KeyboardButton("Tavsiyalar olish")
    ruyxatni_tozalash = KeyboardButton("Xarajatlarni tozalash")
    yordam = KeyboardButton("Yordam")
    tugmalar.add(xarajat_qushish, maslahat_olish, ruyxatni_tozalash, yordam)
    return tugmalar

def azolikni_tekshiruvchi(user_id):
    try:
        status = bot.get_chat_member(kanal_user_name, user_id).status
        return status in ['member', 'administrator', 'creator']
    except:
        print(f"Xatolik")
        return False

def kanal_tugma():
    kanallar = InlineKeyboardMarkup(row_width=1)
    kanal_1 = InlineKeyboardButton("👉 1-Kanalga qo‘shiling 👈", url=kanal_link)
    kanal_0 = InlineKeyboardButton(" ✅ Tasdiqlash", callback_data="tasdiq")
    kanallar.add(kanal_1,kanal_0)
    return kanallar

@bot.callback_query_handler(func=lambda call: True)
def azolik_2(call):
    if call.data == "tasdiq":
        user_id = call.message.chat.id
        if azolikni_tekshiruvchi(user_id):
            bot.send_message(call.message.chat.id, " Rahmat! Endi botdan foydalanishingiz mumkin.", reply_markup=menyu())
        else:
            bot.send_message(
                call.message.chat.id,
                "Siz hali kanalga obuna bo‘lmadingiz! Iltimos, obuna bo‘ling.❗️❗️❗️",
                reply_markup=kanal_tugma()
            )

@bot.message_handler(commands=['start'])
def tanishtiruv(message):
    user_id = message.chat.id
    if not azolikni_tekshiruvchi(user_id):
        bot.send_message(
            message.chat.id,
            "Iltimos, quyidagi kanallarga obuna bo‘ling va tasdiqlash tugmasini bosing:",
            reply_markup=kanal_tugma()
        )
        return

    bot.send_message(
        message.chat.id,
        "Salom! Men sizning xarajatlaringiz asosida byudjet tavsiyalarini bera olaman.\nQuyidagi tugmalardan foydalaning:",
        reply_markup=menyu()
    )

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
    except ValueError:
        bot.reply_to(message, "Xatolik! Iltimos, xarajatlaringizni to‘g‘ri formatda kiriting: \n`Ovqat:50000`")

@bot.message_handler(func=lambda message: message.text == "Tavsiyalar olish")
def vazir(message):
    user_id = message.chat.id

    if user_id not in ruyxat or not ruyxat[user_id]:
        bot.reply_to(message, "Sizda hozircha hech qanday xarajatlar qayd etilmagan.")
        return

    narx = sum(ruyxat[user_id].values())
    tahlil = ("Sizning xarajatlaringiz tahlili:\n"
        f"Jami xarajat: {narx} so‘m\n\n")

    for category, amount in ruyxat[user_id].items():
         tahlil += f" - {category}: {amount} so‘m\n"

    tahlil += "\nTavsiyalar:\n"
    if narx > 500000:
        tahlil += "Jami xarajatingiz yuqori. Iltimos, tejashni boshlang.\n"
    else:
        tahlil += "Xarajatingiz nazorat ostida. Ajoyib!\n"
    bot.reply_to(message, tahlil)
@bot.message_handler(func=lambda message: message.text == "Xarajatlarni tozalash")
def tozalovchi(message):
    user_id = message.chat.id
    ruyxat[user_id] = {}
    bot.reply_to(message, "Xarajatlaringiz tozalandi!")

@bot.message_handler(func=lambda message: message.text == "Yordam")
def kumak(message):
    bot.reply_to(message, "Bu bot sizga xarajatlaringizni nazorat qilishga yordam beradi.\nXizmatdan foydalanishda savollar tug‘ilsa, admin bilan bog‘laning.")
bot.polling()
