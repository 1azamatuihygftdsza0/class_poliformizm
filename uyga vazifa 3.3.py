import telebot
from telebot import types

# Bot tokeni
token = '7832465485:AAGjdU5hp1BRYu0oWDHwPEk2qRt-7OUYN68'
bot = telebot.TeleBot(token)

# Kanal ma'lumotlari
kanal_link = "https://t.me/ob_havobashorati"
kanal_name = "@ob_havobashorati"

# Kanalga ulanish uchun tugmalar
def kanallar():
    kanal_0 = types.InlineKeyboardMarkup(row_width=1)
    kanal_1 = types.InlineKeyboardButton("👉 1-Kanalga qo‘shiling 👈", url=kanal_link)
    kanal_2 = types.InlineKeyboardButton("✅ Tasdiqlash", callback_data="tasdiq")
    kanal_0.add(kanal_1, kanal_2)
    return kanal_0

# Obuna bo'lganlikni tekshirish
def azolik_aniqlovchi(user_id):
    try:
        status = bot.get_chat_member(kanal_name, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Xatolik: {e}")
        return False

# Tasdiqlash tugmasi bosilganda ishlovchi
@bot.callback_query_handler(func=lambda call: True)
def azolik_aniqlovchi_2(call):
    if call.data == "tasdiq":
        user_id = call.message.chat.id
        if azolik_aniqlovchi(user_id):
            bot.send_message(call.message.chat.id,
                             "Kanalimizga a'zo bo'lganingiz uchun tashakkur! Endi botimizdan foydalanishingiz mumkin.",
                             reply_markup=ob_havo_holati())
        else:
            bot.send_message(call.message.chat.id,
                             "Siz hali kanalga obuna bo‘lmadingiz! Iltimos, obuna bo‘ling.❗️❗️❗️",
                             reply_markup=kanallar())

# Start komandasi
@bot.message_handler(commands=['start'])
def start(xabar):
    user_id = xabar.chat.id
    if not azolik_aniqlovchi(user_id):
        bot.send_message(
            xabar.chat.id,
            "Iltimos, quyidagi kanallarga obuna bo‘ling va tasdiqlash tugmasini bosing:",
            reply_markup=kanallar()
        )
        return
    bot.send_message(
        xabar.chat.id,
        "Salom! Men sizga havo holati haqida ma'lumot bera olaman.\nQuyidagi tugmalardan foydalaning:",
        reply_markup=ob_havo_holati()
    )

# Havo holatini tanlash uchun tugmalar
def ob_havo_holati():
    belgi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    belgi.add("Tumanli🌫", "Sovuq❄️", "Issiq🌡", "Yomg'ir🌧")
    return belgi

# Havo holatini tanlash
@bot.message_handler(func=lambda xabar: xabar.text in ["Tumanli🌫", "Sovuq❄️", "Issiq🌡", "Yomg'ir🌧"])
def havo_holatini_qabul_qilish(xabar):
    ob_holati = xabar.text.split("🌫❄️🌡🌧")[0].lower()  # Emoji orqali tozalangan
    belgi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    belgi.add("O'rtacha", "Boshqa")
    bot.reply_to(xabar, "Havo harorati qanday?", reply_markup=belgi)
    bot.register_next_step_handler(xabar, harorat_holati, ob_holati)

# Harorat bosqichi
def harorat_holati(xabar, ob_holati):
    temperature = xabar.text.lower()
    belgi = types.ReplyKeyboardMarkup(resize_keyboard=True)
    belgi.add("Kuchli", "O'rtacha", "Yengil")
    bot.reply_to(xabar, "Shamol tezligi qanday?", reply_markup=belgi)
    bot.register_next_step_handler(xabar, shamol_tezligi, ob_holati, temperature)

# Shamol tezligini tanlash
def shamol_tezligi(xabar, ob_holati, temperature):
    shamol = xabar.text.lower()
    bashorat = bashorat_yaratish(ob_holati, temperature, shamol)
    bot.reply_to(xabar, bashorat)

# Bashorat yaratish
def bashorat_yaratish(ob_holati, temperature, shamol):
    advices = {
        "tumanli": "Tumanli havo, ehtiyotkorlik bilan harakat qiling.",
        "issiq": "Issiq havo, ko'p suyuqlik ichish kerak.",
        "sovuq": "Sovuq havo, issiq kiyimlar kiyish tavsiya etiladi.",
        "yomg'ir": "Yomg'irli havo, yomg'irlik kiyimlar kiyib chiqing."
    }
    bashorat = f"Havo holati: {ob_holati.capitalize()}\n{advices.get(ob_holati, '')}"
    if temperature == "o'rtacha":
        bashorat += "\nHavo harorati o'rtacha, o'rta darajadagi kiyimlar kiyishingiz mumkin."
    shamol_maslahatlari = {
        "kuchli": "Shamol kuchli, ehtiyot bo'ling.",
        "o'rtacha": "Shamol o'rtacha, ehtiyotkorlik bilan yuring.",
        "yengil": "Shamol yengil, hech qanday muammo yo'q."
    }
    bashorat += f"\n{shamol_maslahatlari.get(shamol, '')}"
    return bashorat

# Yordam bo'limi
@bot.message_handler(func=lambda xabar: xabar.text.lower() == "yordam")
def yordam_xabari(xabar):
    yordam_xabari = (
        "Botdan foydalanish uchun quyidagi amallarni bajarishingiz mumkin:\n"
        "1. Havo holatini bilish: Havo sharoitini tanlash orqali havo holatini bilib olishingiz mumkin.\n"
        "2. Yordam: Bu bo'lim orqali sizga yordam olishingiz mumkin.\n\n"
        "Shunchaki menyudan kerakli variantni tanlang."
    )
    bot.reply_to(xabar, yordam_xabari)

# Botni ishga tushirish
bot.polling()
