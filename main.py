from funcs import *
import telebot
from telebot import types
from keyboards import *
import os
import logging
from config import *

explorer = 0
browser = 0

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_menu(message):
    bot.send_message(message.chat.id, "Главное меню", reply_markup=start_key())


# ---FUNCS-----
@bot.callback_query_handler(func=lambda call: call.data.startswith('open_'))
def open_app(call):
    app = call.data.split('_')[1]
    if globals()[app] == 0:
        globals()[app] += 1
        os.system(f"start {app}")
        if call.message.text.split()[1] == app:
            pass
        else:
            bot.edit_message_text(f"Открыт {app}",
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=menu_2_key())
    else:
        globals()[app] = 0
        


# ---MENU---
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    def volume(message):
        old = ''
        user_id = message.from_user.id
        bot.delete_message(user_id, message.id)
        current = get_brightness()
        change_brightness(str(message.text))
        new = get_brightness()
        if current != new:
            bot.edit_message_text(f"Вы изменили яркость. Текущая яркость: {get_brightness()}",
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=keyboard)
        bot.register_next_step_handler(call.message, volume)

    if call.data == 'menu_1':
        keyboard = types.InlineKeyboardMarkup()
        back_button = types.InlineKeyboardButton("Назад", callback_data='main_menu')
        keyboard.add(back_button)
        bot.edit_message_text("""Введите новую яркость в формате:
+ <число> - увеличить яркость на число
- <число> - уменьшить яркость на число
<число> - установить значение яркости на число""",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=keyboard)
        bot.register_next_step_handler(call.message, volume)

    elif call.data == 'menu_2':
        bot.edit_message_text("Чтобы запустить приложение, нажмите на соответствующую кнопку.",
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              reply_markup=menu_2_key())

    elif call.data == 'main_menu':
        bot.clear_step_handler_by_chat_id(call.message.chat.id)
        bot.edit_message_text("Главное меню:",
                              reply_markup=start_key(),
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id)


if __name__ == '__main__':
    print("starting polling...")
    bot.polling(none_stop=True)
