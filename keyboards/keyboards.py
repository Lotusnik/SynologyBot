from aiogram import types

# Определение кнопок для клавиатур
button1 = types.KeyboardButton(text="Старт")
button2 = types.KeyboardButton(text="Выбор тарифа")
button3 = types.KeyboardButton(text="Информация")
button4 = types.KeyboardButton(text="Техническая поддержка")
button5 = types.KeyboardButton(text="Закрыть")

# Определение первой клавиатуры с пятью кнопками, разделенными на два ряда
keyboard1 = [
    [button1, button2, button3],
    [button4, button5],
]

# Определение второй клавиатуры с двумя кнопками в одном ряду
keyboard2 = [
    [button3, button4],
]

# Создание объектов ReplyKeyboardMarkup для использования в ответах
kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
