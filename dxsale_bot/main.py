import dxsale_bot.config
import telebot

bot = telebot.TeleBot(dxsale_bot.config.token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "123")


bot.polling(none_stop=True)
