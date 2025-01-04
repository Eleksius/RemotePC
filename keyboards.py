from telebot import types


def start_key():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Изменить яркость", callback_data='menu_1')
    button2 = types.InlineKeyboardButton("Приложения", callback_data='menu_2')
    keyboard.add(button1, button2)
    return keyboard


def menu_2_key():
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Назад", callback_data='main_menu')
    open_1 = types.InlineKeyboardButton("Browser", callback_data='open_browser')
    open_2 = types.InlineKeyboardButton("Explorer", callback_data='open_explorer')
    keyboard.add(open_1, open_2)
    keyboard.add(back_button)
    return keyboard
