import telebot, random



TOKEN = '8041460745:AAGCPja3t0Z4mhUBBXxVlT4Q6KpzxUPzPEQ'
bot = telebot.TeleBot(TOKEN)
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = telebot.types.KeyboardButton('Поставить оценку')
button_2 = telebot.types.KeyboardButton('Рейтинг')
keyboard.add(button_1, button_2)

#__________________________________________________________________________________________________________________

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Выберете действие снизу⬇️', reply_markup=keyboard)
    bot.register_next_step_handler(message, command) 

def command(message):
    print(message.text.strip().capitalize())
    if message.text.strip().capitalize() == "Поставить оценку":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Python', callback_data="Python")
        button_2 = telebot.types.InlineKeyboardButton('Scratch', callback_data="Scratch")
        button_3 = telebot.types.InlineKeyboardButton('Roblox', callback_data="Roblox")
        button_4 = telebot.types.InlineKeyboardButton('WEB разработка', callback_data="WEB разработка")
        button_5 = telebot.types.InlineKeyboardButton('Game ART', callback_data="Game ART")
        keyboard.add(button_1, button_2, button_3, button_4, button_5)
        bot.send_message(message.chat.id, 'Выберете курс👨‍💻', reply_markup=keyboard)
        bot.register_next_step_handler(message, handle_callback) 
    elif message.text.strip().capitalize() == "Рейтинг":
        bot.send_message(message.chat.id, f'1. ')

#__________________________________________________________________________________________________________________

@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    if callback.data == 'Python':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Максим Насонов', callback_data="Максим Насонов")
        button_2 = telebot.types.InlineKeyboardButton('Игорь Гетто', callback_data="Игорь Гетто")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Выберете преподавателя🙍‍♂️', reply_markup=keyboard)
    elif callback.data == 'Scratch':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Арина Атаманова', callback_data="Арина Атаманова")
        button_2 = telebot.types.InlineKeyboardButton('Дмитрий Шихотов', callback_data="Дмитрий Шихотов")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Выберете преподавателя🙍‍♂️', reply_markup=keyboard)
    elif callback.data == 'Roblox':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Дмитрий Грешных', callback_data="Дмитрий Грешных")
        button_2 = telebot.types.InlineKeyboardButton('Юрий Байдин', callback_data="Юрий Байдин")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Выберете преподавателя🙍‍♂️', reply_markup=keyboard)
    elif callback.data == 'WEB разработка':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Андрей Кин', callback_data="Андрей Кин")
        button_2 = telebot.types.InlineKeyboardButton('Илья Козлобродов', callback_data="Илья Козлобродов")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Выберете преподавателя🙍‍♂️', reply_markup=keyboard)
    elif callback.data == 'Game ART':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Диана Шульга', callback_data="Диана Шульга")
        button_2 = telebot.types.InlineKeyboardButton('Антон Белоус', callback_data="Антон Белоус")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Выберете преподавателя🙍‍♂️', reply_markup=keyboard)

#__________________________________________________________________________________________________________________

    elif callback.data == 'Максим Насонов':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeMN")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeMN")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/MN.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Максим Насонов. Преподаватель программирования. Обучает детей более 2 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Игорь Гетто':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeIG")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeIG")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/IG.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Игорь Гетто. Преподаватель программирования. Обучает детей более 2 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)


bot.polling(
    non_stop=True,
    interval=1 
)