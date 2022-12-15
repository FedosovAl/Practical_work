from telebot.handler_backends import State, StatesGroup


class UserData(StatesGroup):
    user_city = State()
    user_select_id = State()