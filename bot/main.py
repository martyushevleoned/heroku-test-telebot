import telebot  # pip3 install PyTelegramBotAPI

bot = telebot.TeleBot('1212464853:AAGmGDrz0ud5SdHGlKZnOONzaBKCvSBH1aY')


# text
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
