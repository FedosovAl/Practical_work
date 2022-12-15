from telebot import types
from loader import bot


def cities_buttons(message, cities):
    keyboard_cities = types.InlineKeyboardMarkup()
    for key, value in cities:
        keyboard_cities.add(types.InlineKeyboardButton(text=value, callback_data=str(key)))
    bot.send_message(message.from_user.id, 'Пожалуйста, уточни город, выбрав соответствующую кнопку:',
                     reply_markup=keyboard_cities)