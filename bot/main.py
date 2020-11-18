import telebot  # pip3 install PyTelegramBotAPI

bot = telebot.TeleBot('1212464853:AAFo0jcVRi71sggAK0RD8c7aw3LMYB4Lp-w')


# text
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
