from telebot.types import Message
from config_data.config import get_all_commands
from loader import bot


@bot.message_handler(commands=['help'])
def bot_help(message: Message):
    text = get_all_commands()
    bot.send_message(message.from_user.id, f'Все доступные команды:\n\n {text}')
