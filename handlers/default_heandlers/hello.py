from telebot.types import Message

from loader import bot


@bot.message_handler(func=lambda message: message.text in ['Привет', 'привет'])
def bot_hello(message: Message):
    bot.send_message(message.from_user.id, f"Привет, ты готов к поиску?")


@bot.message_handler(func=lambda message: message.text in ['Да', 'да'])
def bot_hello(message: Message):
    bot.send_message(message.from_user.id, f"Отлично! Нажми /help для вывода списка доступных команд.")


@bot.message_handler(func=lambda message: message.text in ['Нет', 'нет'])
def bot_hello(message: Message):
    bot.send_message(message.from_user.id, f"Приходи, когда будешь готов. Буду тебя ждать!")