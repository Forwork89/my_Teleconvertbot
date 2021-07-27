import telebot
bot = telebot.TeleBot("1907839541:AAGb9S_Gxbe7EqIZChmSxkwBADMNf-qiSSE")


@bot.message_handler(commands=['Привет', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Привет чем могу помочь")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)







bot.polling()