from telebot.types import Message
from telebot import types
from loader import bot
from states.user_data import UserData
from utils.destination_id import destination_id


@bot.message_handler(commands=['lowprice'])
def get_city(message):
    bot.set_state(message.from_user.id, UserData.user_city, message.chat.id)
    bot.send_message(message.from_user.id, "В каком городе будем искать?")
    # bot.register_next_step_handler(message, get_city_count)


@bot.message_handler(state=UserData.user_city)
def find_city(message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['user_city'] = message.text
    bot.send_message(message.from_user.id, f"Ищем в городе {data['user_city']}")
    possible_options = destination_id(data['user_city'])
    print(possible_options)


# def get_city_count(message):
#     data.append(message.text)
#     bot.send_message(message.from_user.id, "Сколько отелей показать?")
#     bot.register_next_step_handler(message, city_photo)
#
#
# def city_photo(message):
#     data.append(message.text)
#     keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes', row_width=2)  # кнопка «Да»
#     keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#     text = "Показать фотографии отелей?"
#     bot.send_message(message.from_user.id, text=text, reply_markup=keyboard)
#     # bot.register_next_step_handler(message, print_info)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id, "Отлично! Сейчас я найду всю информацию и вернусь.")
#     elif call.data == "no":
#         pass
#
#
# def print_info(message):
#     data.append(message.text)
#     bot.send_message(message.from_user.id, "Отлично! Сейчас я найду всю информацию и вернусь.")
#     bot.send_message(message.from_user.id, f"Заданные параметры: {[value for value in data]}")
