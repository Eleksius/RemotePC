from telebot import types


def start_key():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("🔆 Изменить яркость", callback_data='menu_1')
    button2 = types.InlineKeyboardButton("📦 Приложения", callback_data='menu_2')
    button3 = types.InlineKeyboardButton("🔋 Питание", callback_data='menu_3')
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    return keyboard


def menu_2_key():
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("◀ Назад", callback_data='main_menu')
    open_1 = types.InlineKeyboardButton("🌎 Browser", callback_data='open_browser')
    open_2 = types.InlineKeyboardButton("📁 Explorer", callback_data='open_explorer')
    keyboard.add(open_1)
    keyboard.add(open_2)
    keyboard.add(back_button)
    return keyboard


def menu_3_key():
    keyboard = types.InlineKeyboardMarkup()
    sh_now = types.InlineKeyboardButton("🛑 Выключить пк", callback_data='shutdown_now')
    sh_then = types.InlineKeyboardButton("⏳ Выключить через время", callback_data='shutdown_then')
    back = types.InlineKeyboardButton("◀ Назад", callback_data='main_menu')
    keyboard.add(sh_now)
    keyboard.add(sh_then)
    keyboard.add(back)
    return keyboard


def back_menu():
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("◀ Назад", callback_data='main_menu')
    keyboard.add(back_button)
    return keyboard


def back_menu3():
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("◀ Назад", callback_data='menu_3')
    keyboard.add(back_button)
    return keyboard
