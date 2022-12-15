from telebot.types import Message

from loader import bot


@bot.message_handler(commands=['start'])
def bot_start(message: Message):
    bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}! "
                                           f"Я помогу тебе выбрать наиболее подходящий отель. Тебе нужно "
                                           f"только задать необходимые параметры. Чтобы увидеть список доступных"
                                           f"комманд нажми /help")


