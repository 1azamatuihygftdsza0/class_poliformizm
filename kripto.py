# import telebot
# import requests
# from pprint import pprint as print
# API_KEY = '30cd2942e3de6994bbe456d576b8f4d1'
# url = f"https : //api.coinlayer.com/live ? {API_KEY}"
# response = requests.get(url)
# print(response.status_code)
# from aiogram import Bot, Dispatcher, types
# import telebot
#
#
# # Telegram bot tokeningizni shu yerga kiriting
# API_TOKEN = "787499fND2876:AAE6m3-sPZWy0mmgf3mf-lX88DCH2PYk"
#
# # Bot va Dispatcher obyektlarini yaratamiz
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher(bot)
#
# # Har qanday xabar uchun handler
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.reply(message.text)  # Foydalanuvchi yuborgan xabarni qaytarib yuboramiz
#
# # Botni ishga tushiramiz
# if __name__ == "__main__":
#     print("Bot ishga tushdi...")
#     executor.start_polling(dp, skip_updates=True)
# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
#
# # Telegram bot tokeningizni shu yerga kiriting
# API_TOKEN = "7874992876:AAE6m3-sPZWfNDy0mmgf3mf-lX88DCH2PYk"
#
# # Bot va Dispatcher obyektlarini yaratamiz
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
#
# # Har qanday xabar uchun handler
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.reply(message.text)  # Foydalanuvchi yuborgan xabarni qaytarib yuboramiz
#
# # Botni ishga tushiramiz
# if __name__ == "__main__":
#     print("Bot ishga tushdi...")
# #     executor.start_polling(dp, skip_updates=True)
# import os
# import telebot
#
# TOKEN = os.environ.get('787499fND2876:AAE6m3-sPZWy0mmgf3mf-lX88DCH2PYk')
# bot = telebot.TeleBot('TOKEN')
# @bot.message_handler(commands = ['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "assalomu alaykum")
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
# bot.polling()
# import os
# import telebot
#
# # Bot tokeningizni shu yerga yozing
# TOKEN = os.environ.get('7239820845:AAEkJxb-J2nsxe8coOTSBfrnWLR-zhMRWYs')
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Assalomu alaykum")
#
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
#
# if __name__ == "__main__":
#     try:
#         bot.polling()
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")
# import telebot
#
# # Tokeningizni shu yerga yozing
# TOKEN = "BOT_TOKEn_HERE"  # Bu yerda bot tokeningizni yozing
#
# bot = telebot.TeleBot(TOKEN)
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Assalomu alaykum")
#
# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)
# bot.polling()




