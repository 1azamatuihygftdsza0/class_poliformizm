
import telebot
import requests
# TOKEN = '7226834091:AAENZxQNmVewzLq7ZAzUqp11zM7Ia0PYFLk'
bot = telebot.TeleBot("7226834091:AAENZxQNmVewzLq7ZAzUqp11zM7Ia0PYFLk")

#API_KEY = '30cd2942e3de6994bbe456d576b8f4d1'
def prognoz(kripto):
 #   API_KEY = '30cd2942e3de6994bbe456d576b8f4d1'
    url = f"http://api.coinlayer.com/api/live?access_key=30cd2942e3de6994bbe456d576b8f4d1"
    response = requests.get(url)
    h = response.json()
    kripto = kripto.upper()  # Kripto kodini katta harfga aylantiramiz
    if kripto in h['rates']:
        return f"{kripto} narxi: {h['rates']['kripto']} USD"
    else:
        return "Bunday kripto valyuta topilmadi. Iltimos, kodni to'g'ri kiriting"
@bot.message_handler(commands=['start'])
def salomlashuvchi(message):
    bot.reply_to(
        message,
        "Assalomu alaykum. Kripto valyuta botiga xush kelibsiz!\n"
        "Kripto valyuta narxini bilmoqchi bo'lsangiz, /price komandasi bilan kripto kodini kiriting.\n\n"
        "Masalan: /price BTC"
    )
@bot.message_handler(func = lambda message: True)
def javob_chiqaruvchi(message):
    kripto = message.text.upper()
    javob = prognoz(kripto)
    bot.reply_to(message, javob)
bot.polling()
















