import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
API_TOKEN = "8066515295:AAHzscDqP-zd2ZwtJs3aHd1AfDFOYWayjfw"
bot = telebot.TeleBot(API_TOKEN)
DOWNLOADS_DIR = os.path.expanduser("C:/Users/Lenovo-PC/Downloads")
kanal_link = "https://t.me/avto_tuning_xushnudbek"
kanal_user_name = "@avto_tuning_xushnudbek"
def kanal_tugma():
    kanallar = InlineKeyboardMarkup(row_width=1)
    kanal_1 = InlineKeyboardButton("👉 1-Kanalga qo‘shiling 👈", url=kanal_link)
    kanal_0 = InlineKeyboardButton("✅ Tasdiqlash", callback_data="tasdiq")
    kanallar.add(kanal_1, kanal_0)
    return kanallar
def azolikni_tekshiruvchi(user_id):
    try:
        status = bot.get_chat_member(kanal_user_name, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception as e:
        print(f"Xatolik: {e}")
        return False
@bot.callback_query_handler(func=lambda call: True)
def azolik_2(call):
    if call.data == "tasdiq":
        user_id = call.message.chat.id
        if azolikni_tekshiruvchi(user_id):
            bot.send_message(call.message.chat.id, "Rahmat! Endi botdan foydalanishingiz mumkin.", reply_markup=main_keyboard())
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
        reply_markup=main_keyboard()
    )
def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    gentra_button = KeyboardButton('Gentra')
    malibu_button = KeyboardButton('Malibu')
    damas_button = KeyboardButton('Damas')
    baho_button = KeyboardButton('hammasini kurib bulib bosing NAMOZOV')
    coblt_button = KeyboardButton('Coblt')
    nexia_button = KeyboardButton('Nexia')
    back_button = KeyboardButton('Back')
    markup.add(gentra_button, malibu_button, coblt_button, baho_button, damas_button, nexia_button)
    markup.add(back_button)
    return markup
def send_photo(message, photo_path, description):
    try:
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(
                    message.chat.id,
                    photo,
                    caption=description
                )
        else:
            bot.send_message(
                message.chat.id,
                f"Fayl topilmadi: {photo_path}\nIltimos, rasmlar to‘g‘ri joylashganligini tekshiring."
            )
    except Exception as e:
        bot.send_message(
            message.chat.id,
            f"Xatolik yuz berdi: {e}"
        )
@bot.message_handler(func=lambda message: message.text == 'Gentra')
def gentra(message):
    photo_path = os.path.join(DOWNLOADS_DIR, 'Gentra.jpg')
    description = 'MALUMOT:\n☠️gentra 2024-yil\n✅prabeg=0km\n✅ranggi qora KOTTA BOLLA\n✅radnoy balon🛞\n✅lyuk\nAYBI:\nchexol polik qilinmagan📎\nnarxi:14000$💸\n📞+998931016078'
    send_photo(message, photo_path, description)
@bot.message_handler(func=lambda message: message.text == 'Coblt')
def coblt(message):
    photo_path = os.path.join(DOWNLOADS_DIR, 'Coblt.jpg')
    description = 'MALUMOT:\n☠️Coblt 2020-yil\n✅prabeg=7400km\n✅ranggi oq\n✅radnoy balon🛞\n✅tesla manitor\nAYBI:\nyuq📎\nnarxi:123 million💸\n📞 +998931016078'
    send_photo(message, photo_path, description)
@bot.message_handler(func=lambda message: message.text == 'Malibu')
def malibu(message):
    photo_path = os.path.join(DOWNLOADS_DIR, 'Malibu.jpg')
    description = 'MALUMOT:\n☠️Malibu 2021-yil\n✅prabeg=120000 km\n✅klimit cantrol\n✅mers rul\n✅kodja salon\nAYBI:\norqa bufer yorilgan📎\nnarxi:28000$💸\n📞+998931016078'
    send_photo(message, photo_path, description)
@bot.message_handler(func=lambda message: message.text == 'Damas')
def damas(message):
    photo_path = os.path.join(DOWNLOADS_DIR, 'Damas.jpg')
    description = 'MALUMOT:\n☠️Damas 2022-yil\n✅prabeg=4 krug\n✅balonlari bor\n✅ranggi oq\n✅magnitafon\nAYBI:\noldin laboy yuq\n🛞zapas baloni yuq📎\nnarxi:54 milion💸\n📞+998931016078'
    send_photo(message, photo_path, description)
@bot.message_handler(func=lambda message: message.text == 'Nexia')
def nexia(message):
    photo_path = os.path.join(DOWNLOADS_DIR, 'Nexia.jpg')
    description = 'MALUMOT:\n☠️Nexia 3 2021-yil\n✅prabeg=23545 km\n✅rangi chokolat\n✅LI 9 salon\n✅malibu 2 rul\nAYBI:\nIdeal📎\nnarxi:89,9 million💸\n📞+998931016078'
    send_photo(message, photo_path, description)
@bot.message_handler(func=lambda message: message.text == 'Back')
def back(message):
    bot.send_message(message.chat.id, "Bosh menyuga qaytdingiz.", reply_markup=main_keyboard())
@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "Kechirasiz, bu buyruqni tushunmadim. Bosh menyudan tanlang.", reply_markup=main_keyboard())

bot.polling()
