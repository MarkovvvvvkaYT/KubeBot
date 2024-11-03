import telebot, random

teachers = {
    'Арина Атаманова' : 0,
    'Антон Белоус' : 0,
    'Максим Насонов' : 0,
    'Андрей Кин' : 0,
    'Дмитрий Грешных' : 0,
    'Дмитрий Шихотов' : 0,
    'Диана Шульга' : 0,
    'Игорь Гетто' : 0,
    'Илья Козлобродов' : 0,
    'Юрий Байдин' : 0
}


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
        sorted_people = sorted(teachers.items(), key=lambda item: item[1], reverse=True)
        ch = 0
        text = ''
        for prepod, likes in sorted_people:
            ch = ch + 1
            text += f'{ch}. {prepod}: {likes}\n'
        bot.send_message(message.chat.id, text)

#__________________________________________________________________________________________________________________

@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    global teachers
    if callback.data == "Поставить оценку":
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Python', callback_data="Python")
        button_2 = telebot.types.InlineKeyboardButton('Scratch', callback_data="Scratch")
        button_3 = telebot.types.InlineKeyboardButton('Roblox', callback_data="Roblox")
        button_4 = telebot.types.InlineKeyboardButton('WEB разработка', callback_data="WEB разработка")
        button_5 = telebot.types.InlineKeyboardButton('Game ART', callback_data="Game ART")
        keyboard.add(button_1, button_2, button_3, button_4, button_5)
        bot.send_message(callback.message.chat.id, 'Выберете курс👨‍💻', reply_markup=keyboard)
    elif callback.data == "Рейтинг":
        sorted_people = sorted(teachers.items(), key=lambda item: item[1], reverse=True)
        ch = 0
        text = ''
        for prepod, likes in sorted_people:
            ch = ch + 1
            text += f'{ch}. {prepod}: {likes}\n'
        bot.send_message(callback.message.chat.id, text)


    elif callback.data == 'Python':
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
    elif callback.data == 'Арина Атаманова':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeAA")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeAA")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/AA.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Арина Атаманова. Преподаватель программирования и робототехники. Обучает детей более 3 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Дмитрий Шихотов':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeDSH")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeDSH")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/DSH.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Дмитрий Шихотов. Преподаватель программирования, робототехники и разработки компьютерных игр. Обучает детей более 2 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Дмитрий Грешных':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeDG")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeDG")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/DG.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Дмитрий Шихотов. Преподаватель 3D-моделирования и разработки игр. Обучает детей более 3 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Юрий Байдин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeYB")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeYB")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/YB.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Юрий Байдин. Преподаватель 3D-моделирования. Обучает детей более 4 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Андрей Кин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeAK")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeAK")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/AK.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Андрей Кин. Преподаватель программирования. Обучает детей более 8 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Илья Козлобродов':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeIK")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeIK")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/IK.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Илья Козлобродов. Преподаватель программирования и разработки сайтов. Обучает детей более 3 лет.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Диана Шульга':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeDSH2")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeDSH2")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/DSH2.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Диана Шульга. Преподаватель игровой графики. Обучает детей более 1 года.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    elif callback.data == 'Антон Белоус':
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('👍', callback_data="likeAB")
        button_2 = telebot.types.InlineKeyboardButton('👎', callback_data="dislikeAB")
        keyboard.add(button_1, button_2)
        bot.send_photo(callback.message.chat.id, open('pictures/AB.png', 'rb'))
        bot.send_message(callback.message.chat.id, 'Антон Белоус. Преподаватель 3D-моделирования. Обучает детей более 1 года.')
        bot.send_message(callback.message.chat.id, 'Поставьте оценку❤️', reply_markup=keyboard)
    
#__________________________________________________________________________________________________________________

    elif callback.data == 'likeMN':
        teachers['Максим Насонов'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeAA':
        teachers['Арина Атаманова'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeAB':
        teachers['Антон Белоус'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeAK':
        teachers['Андрей Кин'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeDG':
        teachers['Дмитрий Грешных'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeDSH':
        teachers['Дмитрий Шихотов'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeDSH2':
        teachers['Диана Шульга'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeIG':
        teachers['Игорь Гетто'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeYB':
        teachers['Юрий Байдин'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'likeIK':
        teachers['Илья Козлобродов'] += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    

#________________________________________________________________________________________



    elif callback.data == 'dislikeMN':
        teachers['Максим Насонов'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeAA':
        teachers['Арина Атаманова'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeAB':
        teachers['Антон Белоус'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeAK':
        teachers['Андрей Кин'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeDG':
        RDG -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeDSH':
        teachers['Дмитрий Шихотов'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeDSH2':
        teachers['Диана Шульга'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeIG':
        teachers['Игорь Гетто'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeYB':
        teachers['Юрий Байдин'] -= 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)
    elif callback.data == 'dislikeIK':
        teachers['Илья Козлобродов'] -=1
        keyboard = telebot.types.InlineKeyboardMarkup()
        button_1 = telebot.types.InlineKeyboardButton('Поставить оценку', callback_data="Поставить оценку")
        button_2 = telebot.types.InlineKeyboardButton('Рейтинг', callback_data="Рейтинг")
        keyboard.add(button_1, button_2)
        bot.send_message(callback.message.chat.id, 'Спасибо🙏', reply_markup=keyboard)

    



bot.polling(
    non_stop=True,
    interval=1 
)