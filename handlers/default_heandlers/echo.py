from telebot.types import Message

from loader import bot


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@bot.message_handler(state=None)
def bot_echo(message: Message):
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help")
