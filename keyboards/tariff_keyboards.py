from aiogram import types

# Функция для создания клавиатуры с кнопками в одном ряду из предоставленного списка названий
def make_row_keyboard(items: list[str]) -> types.ReplyKeyboardMarkup:
    # Создание списка кнопок на основе предоставленных названий
    row = [types.KeyboardButton(text=item) for item in items]
    # Возврат клавиатуры с одним рядом кнопок, клавиатура автоматически подгоняется под размер
    return types.ReplyKeyboardMarkup(keyboard=[row], resize_keyboard=True)
