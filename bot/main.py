import telebot  # pip3 install PyTelegramBotAPI

bot = telebot.TeleBot('')


# text
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
