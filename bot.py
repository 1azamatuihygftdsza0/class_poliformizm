import telebot

bot = telebot.TeleBot('7675837150:AAH3drIy9-bbtf6UY3-M1jhmZvfSH888HRE')

def transliterate(text, to_latin=True):
    krilldan_lotinga = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'Yo', 'Ж': 'J', 'З': 'Z', 'И': 'I', 'Й': 'Y',
        'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F',
        'Х': 'X', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Sch', 'Ъ': "'", 'Ы': 'Y', 'Ь': "'", 'Э': 'E', 'Ю': 'Yu',
        'Я': 'Ya',
        'Ғ': "Gʻ", 'Қ': 'Q', 'Ў': "Oʻ", 'Ҳ': 'H', 'Нг': 'Ng', 'нг': 'ng',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y',
        'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f',
        'х': 'x', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': "'", 'ы': 'y', 'ь': "'", 'э': 'e', 'ю': 'yu',
        'я': 'ya',
        'ғ': "gʻ", 'қ': 'q', 'ў': "оʻ", 'ҳ': 'h', 'нг': 'ng'
    }

    lotindan_krillga = {
        'A': 'А', 'B': 'Б', 'D': 'Д', 'E': 'Е', 'F': 'Ф', 'G': 'Г', 'H': 'Ҳ', 'I': 'И', 'J': 'Ж', 'K': 'К', 'L': 'Л',
        'M': 'М', 'N': 'Н', 'O': 'О', 'P': 'П', 'Q': 'Қ', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У', 'V': 'В', 'X': 'Х',
        'Y': 'Й', 'Z': 'З', 'Yo': 'Ё', 'Ts': 'Ц', 'Ch': 'Ч', 'Sh': 'Ш', 'Sch': 'Щ', "Gʻ": 'Ғ', "Oʻ": 'Ў', 'Ng': 'Нг',
        'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ', 'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л',
        'm': 'м', 'n': 'н', 'o': 'о', 'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в', 'x': 'х',
        'y': 'й', 'z': 'з', 'yo': 'ё', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'sch': 'щ', "gʻ": 'ғ', "oʻ": 'ў', 'ng': 'нг', 'yu': 'ю',
        'ya': 'я','Ya': 'Я','Yu': 'Ю', "g'": 'ғ',"G'": 'Ғ', "O'": 'Ў',"o'": 'ў'
    }

    translit_table = krilldan_lotinga if to_latin else lotindan_krillga
    result = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i:i + 2] in translit_table:
            result.append(translit_table[text[i:i + 2]])
            i += 2
        else:
            result.append(translit_table.get(text[i], text[i]))
            i += 1
    return ''.join(result)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Assalomu alaykum! Men kril-lotin va lotin-kril matnlarni o'zgartirish uchun botman. Matnni yuboring.")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text
    if any(ch in 'абвгдеёжзийклмнопрстуфхцчшщьыэюяғқўҳнг' for ch in text):
        translated_text = transliterate(text, to_latin=True)
    else:
        translated_text = transliterate(text, to_latin=False)
    bot.send_message(message.chat.id, f"`\n{translated_text}\n```", parse_mode="Markdown")
bot.infinity_polling()