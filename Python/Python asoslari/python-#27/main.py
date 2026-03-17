from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot("8690987089:AAE00pMFI8ABXytOADVHmVxXR_DY2vaKLZM")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom!")

@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))

bot.infinity_polling()

# matn = input('Matnni kiriting:')

# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))